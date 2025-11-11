# Smartscript

## Prerequisites

- Python 3.x
- Set up a .env file with your Gemini API key.
- Install dependencies by running:
  bash
  pip install -r requirements.txt



## Description
"Smartscript" is a Streamlit web application for identifying images using the Google Generative AI API. It provides informative summary, formula, questionnaire for uploaded images/pdf on any topic .

## Features
- Upload images,pdf of any topic.
- Receive summary,questionnaire,formula, and an interactive chatspace as per your choice.
- Handwritten notes are also uploadable and you will get the same desired output.

## Usage
1. Visit the application [here](https://note-extractor-generator.streamlit.app/).
2. Upload an image/pdf on any topic.
3. You can click on "Explore","questionnaire","formula" buttons, and also interact in the chatspace with any quesions related to the uploaded file.
4. Wait for the AI to process the image and provide info.
5. Review the generated content and explore the insights.

## U-DOC — Streamlit prescription & report assistant

A small Streamlit app that accepts an image or PDF of a prescription/report and uses the Google Generative AI (Gemini) API to extract summaries, medicine names, and structured information.

This repository contains a ready-to-run prototype. Use it locally for testing and development.

## Features
- Upload images (jpg, png, webp) or PDFs
- Generates a short description and extracts medicine names, dosages, frequencies, and other prescription details
- Simple chat-style text input to ask questions about the uploaded file
- PDF → image conversion using PyMuPDF

## Prerequisites
- Python 3.10+ (3.13 used by the developer environment)
- A Google Generative API key (Gemini) with sufficient quota and billing enabled

## Quick setup (Windows PowerShell)
1. Create & activate a virtual environment
```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```
2. Install dependencies
```powershell
pip install -r requirements.txt
```
3. Create a `.env` file in the project root and add your API key
```
GOOGLE_API_KEY=sk-...your_key_here...
```

Notes:
- The app reads the `GOOGLE_API_KEY` environment variable via `python-dotenv`.
- If you don't have quota or you want offline testing, there is a stub response mode in the code (toggle via Streamlit session state) — see `app.py` for details.

## Run the app
Default Streamlit port is 8501. To run locally:
```powershell
streamlit run app.py
# or choose a different port, e.g. 8502
streamlit run app.py --server.port 8502
```

### Smoke test
If the UI renders blank/black, try the included lightweight smoke app:
```powershell
streamlit run streamlit_smoke.py
```
If the smoke app works, the issue is likely in `app.py` (heavy client-side CSS or long blocking operations).

## Files of interest
- `app.py` — main Streamlit application
- `requirements.txt` — pip dependencies
- `streamlit_smoke.py` — minimal Streamlit page for debugging rendering issues
- `.env` — environment variables (not committed to GitHub; keep secret)

## Troubleshooting
- "No API_KEY or ADC found": ensure `GOOGLE_API_KEY` is present in `.env` and that you restarted Streamlit after creating `.env`.
- "429 / quota" errors: check Google Cloud Console → IAM & Admin → Quotas and Billing. Enable billing and increase quota or use a smaller model.
- Streamlit black screen or blank page: open browser DevTools (F12) and look for WebSocket/connect errors, check the terminal logs where Streamlit is running, and try `streamlit_smoke.py` to isolate the problem.

## Security & privacy
- Do NOT commit your API keys. Keep `.env` out of Git with `.gitignore` (the repo already contains a `.env` placeholder committed; replace it locally and avoid pushing secrets).

## License & author
Developed by Bineet (Bineet043). Use as-is for experimentation. Replace this line with a formal license if you intend to publish.

If you'd like, I can:
- Add a proper `README.md` to the repo (this file), commit it, and push; or
- Add a GitHub Actions workflow to run basic linting or a smoke test on push.

