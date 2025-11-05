
## 🗣️ **Multilingual Text-to-Speech & Voice Cloning System**

### 🚀 Built with FastAPI · Streamlit · Coqui YourTTS



### 📘 **Overview**

This project integrates **Text-to-Speech (TTS)** and **Voice Cloning** capabilities into one multilingual system.
It allows users to input text in any language, automatically translate it (if unsupported), and generate realistic speech output — including cloned voices from short audio samples.
The system runs **locally on CPU** and supports **English, French, and Portuguese**, with automatic translation for other languages.


### 🌍 **Key Features**

✅ **Multilingual Text-to-Speech** — Converts text into human-like speech in multiple languages.
✅ **Voice Cloning** — Clone a speaker’s voice from a short sample (e.g., `.wav`, `.mp3`).
✅ **Auto-Translation** — Detects unsupported languages and translates them using Deep Translator.
✅ **FastAPI Backend** — Provides REST APIs for `/tts/` and `/clone/` endpoints.
✅ **Streamlit Frontend** — Simple and elegant UI for interactive text or file input.
✅ **Runs on CPU** — Fully functional without GPU dependency.
✅ **Open Source** — Built using the Coqui `TTS` library and Python ecosystem.

---

### 🧠 **Model Used**

**Model:** `tts_models/multilingual/multi-dataset/your_tts`
**Library:** [Coqui TTS](https://github.com/coqui-ai/TTS)

* Architecture: Based on **VITS (Variational Inference Text-to-Speech)**
* Features:

  * Zero-shot **Voice Cloning**
  * **Multilingual** synthesis (English 🇬🇧, French 🇫🇷, Portuguese 🇧🇷)
  * Real-time inference
  * Runs locally without GPU

---

### ⚙️ **System Architecture**

```
┌──────────────────────────────────────┐
│           Streamlit Frontend         │
│──────────────────────────────────────│
│ • User inputs text or uploads audio  │
│ • Sends requests to FastAPI backend  │
│ • Plays or downloads generated audio │
└──────────────────────────────────────┘
│
▼
┌──────────────────────────────────────┐
│            FastAPI Backend            │
│──────────────────────────────────────│
│ • Handles /tts/ and /clone/ endpoints │
│ • Uses Deep Translator for languages  │
│ • Invokes YourTTS model for inference │
└──────────────────────────────────────┘
│
▼
┌──────────────────────────────────────┐
│             YourTTS Model             │
│──────────────────────────────────────│
│ • Multilingual TTS + Voice Cloning    │
│ • Generates human-like audio output   │
└──────────────────────────────────────┘
│
▼
┌──────────────────────────────────────┐
│        Output and Storage Layer       │
│──────────────────────────────────────│
│ • Saves generated .wav files locally  │
│ • Returns path or audio to frontend   │
└──────────────────────────────────────┘
```

---

### 🧩 **Folder Structure**

```
tts_multilang_clone/
│
├── app.py                # FastAPI backend
├── app_ui.py             # Streamlit frontend
├── requirements.txt      # Required libraries
│
├── src/
│   ├── tts_engine.py     # Handles TTS generation
│   ├── voice_cloning.py  # Handles cloning logic
│   ├── preprocessing.py  # Cleans and converts audio
│   └── utils.py
│
├── config/
│   └── settings.py       # Global configuration
│
├── outputs/              # Generated speech files
├── uploads/              # Uploaded audio samples
└── README.md
```

---

### 🛠️ **Installation Guide**

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rishabhupadhyay28/TTS_Multilang_clone.git
cd multilingual-voice-cloning-tts
```

#### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

#### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Backend (FastAPI)

```bash
uvicorn app:app --reload
```

Backend will start at → `http://127.0.0.1:8000`

#### 5️⃣ Run the Frontend (Streamlit)

Open a new terminal and run:

```bash
streamlit run app_ui.py
```

Frontend will open in browser → `http://localhost:8501`

---

### 🎤 **How It Works**

1. **Text-to-Speech Mode**

   * Enter any text → select language → click **Generate Speech**
   * Output speech plays automatically or can be downloaded.

2. **Voice Cloning Mode**

   * Upload a voice sample (WAV/MP3)
   * Enter any text to be spoken
   * The model clones the voice and speaks the text naturally.

3. **Language Auto-Translation**

   * If a user inputs Hindi or other unsupported text, it’s automatically translated to English before speech generation.

---

### 🧩 **Libraries Used**

| Library             | Purpose                            |
| ------------------- | ---------------------------------- |
| **FastAPI**         | Backend API framework              |
| **Streamlit**       | Frontend UI                        |
| **Coqui TTS**       | Speech synthesis & voice cloning   |
| **Deep Translator** | Automatic translation              |
| **Pydub**           | Audio conversion and preprocessing |
| **Uvicorn**         | ASGI server for FastAPI            |

---

### ⚙️ **System Requirements**

* Python 3.10 or 3.11
* 8GB+ RAM recommended
* Windows / macOS / Linux
* No GPU required (runs fully on CPU)

---

### 📊 **Results**

* Natural and fluent speech output in supported languages.
* High-quality zero-shot voice cloning with short input samples.
* Runs efficiently on CPU-based systems without CUDA dependencies.

---

### 🧭 **Future Enhancements**

* Add **Hindi, Spanish, and German** support.
* Integrate **XTTS** for broader multilingual synthesis.
* Implement **speaker emotion control** (happy, sad, neutral).
* Deploy on web using **Render / Hugging Face Spaces**.

---

### 👨‍💻 **Author**

**Rishabh Upadhyay**
🎓 M.Tech Artificial Intelligence – Amity University Noida
📧 [GitHub Profile](https://github.com/Rishabhupadhyay28)
