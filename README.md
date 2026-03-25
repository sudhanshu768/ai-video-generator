# 🎬 AI Video Generator

An automated pipeline that converts a simple idea into a complete video using AI — including script generation, voice narration, and video creation.

---

## 🚀 Features

* 🧠 Script generation using local LLM
* 🎤 Voice narration generation
* 🖼️ Scene-based video creation
* 🎥 Automated video rendering
* ⚡ End-to-end pipeline (idea → video)

---

## 🏗️ Architecture

```
User Input
   ↓
Ollama (Script + Scenes)
   ↓
Image Generation (Placeholder)
   ↓
Text-to-Speech (gTTS)
   ↓
MoviePy + FFmpeg
   ↓
Final Video 🎬
```

---

## 🔌 APIs & Tools Used

This project was designed with a **cost-optimized approach**, minimizing paid API usage.

### ✅ APIs / Tools Used in Final Output

| Component         | Tool Used        | Type           | Status |
| ----------------- | ---------------- | -------------- | ------ |
| Script Generation | Ollama (Mistral) | Local LLM      | ✅ Used |
| Text-to-Speech    | gTTS             | Free API       | ✅ Used |
| Video Creation    | MoviePy          | Python Library | ✅ Used |
| Video Processing  | FFmpeg           | Local Tool     | ✅ Used |

---

### ⚠️ APIs Considered (Not Used in Final Version)

| Component         | Tool          | Reason                  |
| ----------------- | ------------- | ----------------------- |
| Script Generation | OpenAI API    | Paid / cost constraints |
| Image Generation  | DALL·E        | Paid                    |
| Video Generation  | Runway / Pika | Expensive APIs          |
| Voice Generation  | ElevenLabs    | Paid                    |

---

### 💡 Design Philosophy

* ❌ Avoid expensive APIs
* ✅ Prefer local models
* ✅ Build fully offline-capable pipeline
* ⚡ Optimize for scalability and cost

---

## 📁 Project Structure

```
ai-video-generator/
│
├── main.py
├── gpt_module.py
├── audio_module.py
├── video_module.py
│
├── assets/
│   ├── images/
│   ├── audio/
│
└── output/
```

---

## ⚙️ Setup

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/ai-video-generator.git
cd ai-video-generator
```

---

### 2. Create virtual environment

```
python3 -m venv ai-video-generator
source ai-video-generator/bin/activate
```

---

### 3. Install dependencies

```
pip install moviepy gtts pillow ollama
```

---

### 4. Start Ollama

```
ollama pull mistral
ollama serve
```

---

## ▶️ Usage

```
python main.py
```

Example input:

```
"Impact of AI on future jobs"
```

---

## 🎬 Output

Final video:

```
output/final.mp4
```

---

## 🧠 Tech Stack

* Python
* Ollama (Mistral)
* MoviePy
* FFmpeg
* gTTS

---

## 🔐 Security Note

* `.env` files are excluded using `.gitignore`
* No API keys are stored in the repository

---

## 🚀 Future Improvements

* Stable Diffusion for real images
* Whisper for subtitles
* Coqui TTS for better voice
* Scene transitions & animations
* YouTube auto-upload

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
