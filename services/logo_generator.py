import io
import uuid
import base64
import asyncio
import logging
from typing import Optional

import vtracer
import vertexai
from bs4 import BeautifulSoup
from PIL import Image
from vertexai.preview.vision_models import ImageGenerationModel

import config
from common import openai_constants
from common.utils import retry


async def generate_prompt(business_name: str, style_type: str, keywords: list, colors: list) -> str:
    """
    Generate prompt for imagen3 model
    :param business_name: Name of the business or brand.
    :param style_type: Chosen style type.
    :param keywords: List of keywords that describe user's business.
    :param colors: Chosen color palette.
    :return: Generated prompt
    """
    prompt_generator = await config.ASYNC_OPENAI_INSTANCE.chat.completions.create(
        model=openai_constants.GPT_4O_MINI,
        messages=[
            {"role": "system", "content": openai_constants.PROMPT_GENERATOR.strip()},
            {
                "role": "user",
                "content": f"Business Name: {business_name}, Style Type: {style_type}, Keywords: {keywords}, Colors: {colors}",
            },
        ],
        temperature=0.9,
    )

    generated_prompt = prompt_generator.choices[0].message.content.strip()

    return generated_prompt


def convert_image_to_svg(image_b64: str) -> Optional[str]:
    """
    Convert generated image to svg format
    :param image_b64: Bytes format of an image
    :return: Generated icon svg paths
    """
    try:
        if image_b64.startswith("data:image/png;base64,"):
            image_b64 = image_b64.replace("data:image/png;base64,", "")

        image_bytes = base64.b64decode(image_b64)
        with Image.open(io.BytesIO(image_bytes)) as image:
            if image.mode != "RGBA":
                image = image.convert("RGBA")

            bbox = image.getbbox()
            image = image.crop(bbox)

            scaling_factor = 1

            # Calculating the new size
            new_width = int(image.width * scaling_factor)
            new_height = int(image.height * scaling_factor)
            new_size = (new_width, new_height)
            image = image.resize(new_size, Image.Resampling.LANCZOS)

            data = image.getdata()
            new_data = []
            for item in data:
                r, g, b = item[:3]
                if item[3] >= 160:
                    new_data.append((r, g, b, 255))
                else:
                    new_data.append((r, g, b, 0))
            image.putdata(new_data)

            size = image.size
            svg = vtracer.convert_pixels_to_svg(
                rgba_pixels=image.getdata(),
                size=size,
                color_precision=8,
                mode="spline",
                filter_speckle=4,
                layer_difference=60,
            )

            with open(f"logo-{str(uuid.uuid4())}.svg", mode="w") as file:
                file.write(svg)

            parser = BeautifulSoup(svg, "xml")
            paths = parser.find_all("path")
            icon_svg_paths = ""
            for path in paths:
                icon_svg_paths += str(path)

        return icon_svg_paths
    except Exception as e:
        logging.error(f"Failed to convert the png to svg, error message: {e}")


@retry(3, 1)
def generate_image(prompt: str) -> str:
    """
    Generating image from imagen3 using generated prompts.
    :param prompt: Generated prompts
    :return: Generated image in base64 format.
    """
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
    imagen_model = ImageGenerationModel.from_pretrained(model_name=openai_constants.IMAGEN_3_MODEL)

    image_generator = imagen_model.generate_images(
        prompt=prompt,
        aspect_ratio="1:1",
        person_generation="allow_all",
        negative_prompt="TYPO IN TEXT, DO NOT GENERATE ANY OTHER TEXT THAN THE BUSINESS NAME",
        guidance_scale=100.0,
    )

    image_generator.images[0]._pil_image.show()
    generated_image_bytes = image_generator.images[0]._image_bytes
    image_b64 = base64.b64encode(generated_image_bytes).decode("utf-8")

    image_id = str(uuid.uuid4())[:5]

    with open(f"logos/{image_id}.png", mode="wb") as image:
        image.write(generated_image_bytes)

    return image_b64


async def generate_logo(business_name: str, style_type: str, keywords: list, colors: list) -> dict:
    """
    Generate logo
    :param business_name: Name of the business or brand.
    :param style_type: Chosen style type.
    :param keywords: List of keywords that describe user's business.
    :param colors: Chosen color palette.
    :return: Generated logo in PNG format
    """
    logging.info("Starting to generate logo...")
    prompt = await generate_prompt(business_name=business_name, style_type=style_type, keywords=keywords, colors=colors)
    logo_b64 = generate_image(prompt=prompt)
    logo_svg = convert_image_to_svg(image_b64=logo_b64)

    return {"logo_b64": logo_b64, "logo_svg": logo_svg}


async def generate_logo_set(business_name: str, style_type: str, keywords: list, colors: list, amount: int):
    """
    Generate set of logos
    :param business_name: Name of the business or brand.
    :param style_type: Chosen style type.
    :param keywords: List of keywords that describe user's business.
    :param colors: Chosen color palette.
    :param amount: number of logos to generate.
    :return: Generated logo in PNG format status
    """
    coros = [
        generate_logo(business_name=business_name, style_type=style_type, keywords=keywords, colors=colors)
        for _ in range(amount)
    ]

    generated_logos = await asyncio.gather(*coros)

    return generated_logos
