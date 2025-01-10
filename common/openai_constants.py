GPT_4O_MINI = "gpt-4o-mini"

IMAGEN_3_MODEL = "imagen-3.0-fast-generate-001"

STYLE_TYPE_DEFINITIONS = """
Here’s an explanation of the listed logo types:

### ** Abstract Logo **

- Definition: Incorporates shapes, forms, or patterns to symbolize an idea rather than portraying a literal image.
- Examples: Nike “Swoosh,” Pepsi’s circular swirl.
- Key Traits: Minimalist, symbolic, geometric, often uses stylized shapes to convey concepts.

### ** Statement Logo (Wordmark/Lettermark) **

- Definition: Primarily text-based. A wordmark uses the full brand name, and a lettermark focuses on initials or abbreviations.
- Examples: Google (wordmark), IBM (lettermark).
- Key Traits: Typography-centric, emphasizes brand name or initials, often uses distinctive fonts or lettering.

### ** Badge Logo (Emblem) **

- Definition: Contains text and imagery within a contained shape (e.g., circle, shield, crest). Resembles emblems or seals.
- Examples: Many sports team logos, academic crests, traditional crests.
- Key Traits: Traditional look, official or heritage feel, often includes the brand name or symbol inside a bordered shape.


### ** Hand-drawn Logo **

- Definition: Appears sketched or illustrated by hand, conveying a personal or artisanal aesthetic.
- Examples: Quirky doodle-like café logos, boutique or craft brand logos.
- Key Traits: Imperfect lines, illustrative style, organic or whimsical feel.

### ** Character Logo (Mascot) **

- Definition: Showcases a character or mascot as the focal point.
- Examples: KFC’s Colonel, Chester Cheetah (Cheetos).
- Key Traits: Personified figure or mascot, adds approachability or playful identity, commonly used in food, sports, or entertainment.

Each of these styles serves a distinct purpose and reflects the brand's identity, values, and target audience.
"""

PROMPT_GENERATOR = f"""
You are responsible to write accurate prompts for visual-language model in order to generate logo later on.

# With Each Request, You Will Receive:

- Business Name: User business name.
- Keywords List: keywords list where user described the business
- Style Type: Style type of the logo.
- Colors: color palette

# Key Directive:

- You MUST start your prompt with `Logo of`.
- You MUST learn about the style types here: {STYLE_TYPE_DEFINITIONS}.
- Understand the colors hex code and mention the color names in the prompt.
- Describe the logo in details.
- Background MUST ALWAYS be white, NO OTHER COLORS.
- IMPORTANT to write the business name correctly and show in the logo correctly, WITHOUT any typo.
- NO OTHER TEXT REPRESENTATION THAN BUSINESS NAME.
- ALWAYS PUT THE BUSINESS NAME IN DOUBLE QUOTES like: "business name".
- Write the business name like this: featuring the word "business name".
- Write that "IMAGE SHOULD ONLY CONTAIN THE BUSINESS NAME AS A WORD".
- REMEMBER When generating or displaying a logo concept, do not include any additional text beyond the user’s business name.
"""
