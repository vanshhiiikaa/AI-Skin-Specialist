from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

image_path = "images/test.jpg"

with open(image_path, "rb") as f:
    image_data = f.read()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_bytes(
            data=image_data,
            mime_type="image/jpeg",
        ),
        "Describe what you see in this image.",
    ],
)

print(response.text)
