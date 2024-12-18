import asyncio

from services import logo_generator

business_name = "Norvik"
style = "Character"
keywords = ["burger", "cheese burger", "fast-food"]
colors = ["#6f1d1b", "#708d81", "#8d0801"]

logo = asyncio.run(
    logo_generator.generate_logo(business_name=business_name, style_type=style, keywords=keywords, colors=colors)
)
