from gpt_module import generate_script, refine_image_prompt
from audio_module import generate_audio
from video_module import create_video
from image_module import generate_images
import re


# -------------------------------
# 🧹 Clean script for audio
# -------------------------------
def clean_script_for_audio(script):
    script = re.sub(r"\[.*?\]", "", script)
    script = re.sub(r"\*\*.*?\*\*", "", script)
    script = script.replace('"', "")
    return script.strip()


# -------------------------------
# 🎬 Split into scenes
# -------------------------------
def split_scenes(script):
    lines = script.split("\n")
    scenes = []

    for line in lines:
        clean = line.strip()
        if len(clean) > 20:
            scenes.append(clean)

    return scenes[:5]  # limit


# -------------------------------
# ⏱️ Estimate duration per scene
# -------------------------------
def estimate_durations(scenes):
    durations = []

    for scene in scenes:
        words = len(scene.split())
        duration = max(2, words * 0.4)
        durations.append(duration)

    return durations


# -------------------------------
# 🚀 MAIN
# -------------------------------
if __name__ == "__main__":
    print("🚀 AI Video Generator Started")

    user_input = input("Enter video idea: ")

    # 1. Script
    script = generate_script(user_input)
    print("\nGenerated Script:\n", script)

    # 2. Scenes
    scenes = split_scenes(script)

    # 3. Image prompts
    prompts = [refine_image_prompt(scene) for scene in scenes]

    print("\n🧠 Image Prompts:")
    for p in prompts:
        print("-", p)

    # 4. Images
    image_files = generate_images(prompts)

    if not image_files:
        print("❌ No images generated.")
        exit()

    # 5. Audio
    clean_script = clean_script_for_audio(script)
    audio_file = generate_audio(clean_script)

    # 6. Durations
    durations = estimate_durations(scenes)

    # 7. Video
    create_video(image_files, audio_file, durations)

    print("\n✅ Video created successfully!")