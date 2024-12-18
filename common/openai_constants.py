GPT_4O_MINI = "gpt-4o-mini"

IMAGEN_3_MODEL = "imagen-3.0-fast-generate-001"

STYLE_TYPE_DEFINITIONS = """
Here’s an explanation of the listed logo types:

### 1. **Combo Logo**
- **Definition**: A logo that combines text and imagery or symbols.
- **Details**:
  - Often includes the company name along with a visual icon or illustration.
  - The text and the visual elements can be used together or separately.
  - **Examples**: Burger King (text + visual icon).

### 2. **Abstract Logo**
- **Definition**: A logo that uses geometric or abstract shapes that do not directly represent a recognizable object.
- **Details**:
  - Focuses on creating a unique visual identity using abstract design.
  - Relies on symbolism and association rather than literal representation.
  - **Examples**: Nike swoosh, Pepsi.

### 3. **Statement Logo**
- **Definition**: A logo designed to convey a bold, impactful message or reflect the brand’s core identity in a prominent way.
- **Details**:
  - Often text-heavy or slogan-driven, focusing on the brand's name or mission.
  - Sometimes integrates minimal graphic elements to support the message.
  - **Examples**: Supreme (simple text conveying exclusivity and boldness).

### 4. **Badge Logo**
- **Definition**: A logo that resembles a traditional emblem or crest.
- **Details**:
  - Features a contained design often circular, shield-shaped, or badge-like in structure.
  - Typically used for sports teams, breweries, or heritage brands.
  - **Examples**: Starbucks, Harley-Davidson.

### 5. **Hand-drawn Logo**
- **Definition**: A logo that features custom-drawn elements to give a personal, organic feel.
- **Details**:
  - Emphasizes authenticity and creativity.
  - Often used by artisanal, creative, or niche brands.
  - **Examples**: Brands in food, craft, and artistic industries (e.g., bakeries, handmade goods).

### 6. **Character Logo**
- **Definition**: A logo that features a mascot or character representing the brand.
- **Details**:
  - Helps create a friendly and approachable brand personality.
  - Often used in family-friendly or food-related businesses.
  - **Examples**: KFC (Colonel Sanders), Michelin (Michelin Man).

### 7. **Stamp Logo**
- **Definition**: A logo designed to look like a stamp or seal.
- **Details**:
  - Often features circular or rectangular designs with text around the border and a central element.
  - Used to convey trust, authenticity, or vintage style.
  - **Examples**: Logos for coffee brands, craft breweries, or boutique brands.

Each of these styles serves a distinct purpose and reflects the brand's identity, values, and target audience.
"""

PROMPT_GENERATOR = f"""
You are responsible to write accurate prompts for visual-language model in order to generate logo later on.

# With Each Request, You Will Receive:

- Business Name: User business name.
- Keywords List: keywords list where user described the business
- Style Type: Style type of the logo.
- Colors: color palette

You MUST start your prompt with `Logo of`.
You can learn about the style types here: {STYLE_TYPE_DEFINITIONS}.
Understand the colors hex code and mention the color names in the prompt.
Write the prompt in 2, 3 sentences.
Describe the logo in details.
Background MUST ALWAYS be white, NO OTHER COLORS.
"""
