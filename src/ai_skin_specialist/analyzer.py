import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

client = genai.Client(api_key=api_key)


def analyze_skin(
    image_path: str | None = None,
    user_question: str | None = None,
) -> str:

    prompt = """
You are an AI Skin Specialist assistant.

You provide general skincare information and AI-assisted skin concern
screening. You are NOT a doctor and must NOT provide a definitive
medical diagnosis.

If a skin image is provided, carefully describe only visible observations.

If the user asks a general skincare question without an image, answer
the question normally.

If both an image and a question are provided, use the image and question
together.

Please follow these guidelines:

1. Clearly explain what you observe.
2. Mention possible skin concerns only when appropriate.
3. Never claim certainty or provide a definitive diagnosis.
4. Give practical and general skincare recommendations.
5. Mention when consulting a dermatologist may be appropriate.
6. If an image is unclear, say that reliable visual analysis is not possible.
7. Keep the language simple and understandable.
8. Do not unnecessarily scare the user.
"""

    if user_question:
        prompt += f"""

User's question:

{user_question}
"""

    contents = []

    if image_path:
        with open(image_path, "rb") as f:
            image_data = f.read()

        contents.append(
            types.Part.from_bytes(
                data=image_data,
                mime_type="image/jpeg",
            )
        )

    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-3.8-flash",

        contents=contents,
    )

    return response.text
