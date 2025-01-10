import asyncio

from services import logo_generator

business_name = "Pizzeria"
style = "Badge"
keywords = ["pizza", "pasta", "italian"]
colors = ["#250902", "#640d14", "#ad2831"]

logo = asyncio.run(
    logo_generator.generate_logo_set(
        business_name=business_name, style_type=style, keywords=keywords, colors=colors, amount=1
    )
)
