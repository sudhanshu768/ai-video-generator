from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

prompt = "A futuristic cyberpunk city at night, neon lights, ultra realistic, cinematic, 4k"

print("Generating image...")

image = client.text_to_image(
    prompt,
    model="stabilityai/stable-diffusion-xl-base-1.0"
)

image.save("test_image.png")

print("✅ Image saved as test_image.png")