from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(api_key=HF_TOKEN)


def generate_images(prompts):
    image_files = []

    print("\n🎨 Generating images...")

    for i, prompt in enumerate(tqdm(prompts)):
        try:
            image = client.text_to_image(
                prompt,
                model="stabilityai/stable-diffusion-xl-base-1.0"
            )

            filename = f"img{i+1}.png"
            image.save(filename)

            image_files.append(filename)

        except Exception as e:
            print(f"❌ Error generating image {i+1}: {e}")

    return image_files