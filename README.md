# 🎬 AI Video Generator

An end-to-end AI pipeline that converts a simple idea into a cinematic video using multiple AI services — including script generation, image synthesis, voice narration, and video rendering.

---

## 🚀 Features

* 🧠 **AI Script Generation** (OpenRouter API)
* 🎨 **AI Image Generation** (Hugging Face – Stable Diffusion XL)
* 🎤 **Text-to-Speech Narration** (gTTS)
* 🎥 **Automated Video Creation** (MoviePy + FFmpeg)
* ⚡ Fully automated pipeline (idea → video)

---

## 🏗️ Architecture

```
User Input
   ↓
OpenRouter API (Script Generation)
   ↓
Scene Processing + Prompt Engineering
   ↓
Hugging Face API (Image Generation)
   ↓
gTTS (Audio Narration)
   ↓
MoviePy + FFmpeg (Video Creation)
   ↓
Final Output 🎬
```

---

## 🔌 APIs & Tools Used

### ✅ APIs Used in Final Output

| Component         | Tool                               | Type                | Status |
| ----------------- | ---------------------------------- | ------------------- | ------ |
| Script Generation | OpenRouter API                     | LLM API             | ✅ Used |
| Image Generation  | Hugging Face (Stable Diffusion XL) | Diffusion Model API | ✅ Used |
| Text-to-Speech    | gTTS                               | Free API            | ✅ Used |
| Video Creation    | MoviePy                            | Python Library      | ✅ Used |
| Video Processing  | FFmpeg                             | Local Tool          | ✅ Used |

---

### 🧪 Engineering Notes

* Uses **OpenRouter (`openrouter/auto`)** for flexible model selection
* Uses **Stable Diffusion XL (SDXL)** via Hugging Face for high-quality images
* Combines **scene-level prompts → image synthesis → timed video clips**
* Fully automated pipeline with minimal manual intervention

---

### 🔐 Security & API Handling

* API keys stored using `.env` file
* `.env` excluded via `.gitignore`
* Sensitive tokens are **not committed to repository**

---

## 📁 Project Structure

```
ai-video-generator/
│
├── main.py              # Main pipeline controller
├── gpt_module.py        # Script generation (OpenRouter)
├── image_module.py      # Image generation (Hugging Face)
├── audio_module.py      # Voice generation (gTTS)
├── video_module.py      # Video rendering
│
└── output.mp4           # Final generated video
```

---

## ⚙️ Setup

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/ai-video-generator.git
cd ai-video-generator
```

---

### 2. Create Virtual Environment

```
python3 -m venv ai-video-generator
source ai-video-generator/bin/activate
```

---

### 3. Install Dependencies

```
pip install requests python-dotenv gtts moviepy pillow huggingface_hub tqdm
```

---

### 4. Setup Environment Variables

Create a `.env` file:

```
OPENROUTER_API_KEY=your_openrouter_api_key
HF_TOKEN=your_huggingface_token
```

---

## ▶️ Usage

Run the project:

```
python main.py
```

Enter a prompt:

```
"AI discovering human emotions"
```

---

## 🎬 Output

* Final video saved as:

```
output.mp4
```

---

## 🧠 How It Works

### 1. Script Generation

* Uses OpenRouter API to generate a cinematic multi-scene script

### 2. Scene Processing

* Splits script into scenes
* Cleans text for narration
* Generates image prompts

### 3. Image Generation

* Uses Stable Diffusion XL via Hugging Face
* Generates one image per scene

### 4. Audio Generation

* Converts full script into narration using gTTS

### 5. Video Creation

* Combines images into clips
* Matches durations based on scene length
* Merges with audio using MoviePy

---

## ⚡ Key Features

* Scene-based storytelling pipeline
* Automatic duration estimation
* Prompt engineering for better visuals
* Modular architecture (easy to extend)

---

## 🚀 Future Improvements

* Add subtitles (Whisper)
* Replace gTTS with neural TTS (Coqui / ElevenLabs)
* Add transitions & animations
* Improve prompt engineering
* Add YouTube auto-upload

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
