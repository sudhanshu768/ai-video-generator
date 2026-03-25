from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def create_video(image_files, audio_file, durations, output="output.mp4"):
    if not image_files:
        print("❌ No images found.")
        return

    audio = AudioFileClip(audio_file)

    clips = []

    for img, dur in zip(image_files, durations):
        clips.append(ImageClip(img).set_duration(dur))

    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)

    video.write_videofile(output, fps=24)