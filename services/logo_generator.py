import uuid
import asyncio
import logging

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

import config
from common import openai_constants


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
        temperature=0.5,
    )

    generated_prompt = prompt_generator.choices[0].message.content.strip()

    return generated_prompt


async def generate_logo(business_name: str, style_type: str, keywords: list, colors: list) -> str:
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
    vertexai.init(project=config.PROJECT_ID, location=config.LOCATION)
    imagen_model = ImageGenerationModel.from_pretrained(model_name=openai_constants.IMAGEN_3_MODEL)

    image_generator = imagen_model.generate_images(
        prompt=prompt,
        aspect_ratio="1:1",
        person_generation="allow_all",
        negative_prompt="typo in text",
        guidance_scale=100.0,
    )

    image_generator.images[0]._pil_image.show()
    generated_image_bytes = image_generator.images[0]._image_bytes
    image_id = str(uuid.uuid4())[:5]

    with open(f"logos/{image_id}.png", mode="wb") as image:
        image.write(generated_image_bytes)

    return "image saved successfully."


async def generate_logo_set(business_name: str, style_type: str, keywords: list, colors: list):
    """
    Generate set of logos
    :param business_name: Name of the business or brand.
    :param style_type: Chosen style type.
    :param keywords: List of keywords that describe user's business.
    :param colors: Chosen color palette.
    :return: Generated logo in PNG format status
    """
    coros = [
        generate_logo(business_name=business_name, style_type=style_type, keywords=keywords, colors=colors)
        for _ in range(6)
    ]

    generated_logos = await asyncio.gather(*coros)

    return generated_logos
