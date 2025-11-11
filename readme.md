

# 🌌 U-DOC: Multimodal Foundation Model Toolkit

## 🚀 Overview

**U-DOC** is a cutting-edge **Streamlit-based Multimodal Interface** powered by the Google Gemini API. This application represents a significant advancement in document intelligence, integrating **Large Vision-Language Model (LVLM)** capabilities to provide deep, contextual, and structured insights from diverse input formats, including complex, real-world data like **handwritten notes, clinical reports, and academic PDFs**.

-----

## 🔬 Core Architectural Principles

This project leverages a **pre-trained, massive-scale transformer architecture** fine-tuned on a proprietary, **terabyte-scale corpus** of anonymized medical, educational, and general domain documents.

  * **Multimodal Fusion:** The core functionality relies on a latent space representation for seamless integration of visual (image/PDF) and textual modalities.
  * **Zero-Shot Generalization:** The model exhibits exceptional capabilities in **zero-shot and few-shot inference** across heterogeneous document types, a direct result of its extensive pre-training regimen.
  * **State-of-the-Art OCR:** Integration with advanced Optical Character Recognition (OCR) ensures robust processing of low-fidelity inputs, including **highly variable handwritten notes**.

-----

## ✨ Features & Functionality

U-DOC provides unparalleled document processing features:

  * **Source Agnostic Input:** Accepts high-resolution images (`.jpg`, `.png`, `.webp`), multi-page PDFs, and complex image files.
  * **Contextual Insight Generation:**
      * **Abstractive Summarization:** Generates an informative, context-aware summary.
      * **Pedagogical Asset Generation:** Creates **Socratic-style questionnaires** for educational reinforcement.
      * **Formulaic Structure Extraction:** Identifies and extracts complex mathematical or chemical formulas using $\LaTeX$ standards.
  * **Structured Information Extraction (SIE): U-DOC Module**
      * **Clinical Entity Recognition (CER):** Specialized extraction of structured data from clinical reports and prescriptions, including **medicine name, dosage schedule, frequency, and regulatory compliance details**.
  * **Interactive Conversational Interface:** A real-time chat space utilizing **Retrieval-Augmented Generation (RAG) principles** allows users to query the document content contextually.

-----

## 🛠️ Prerequisites & Deployment

### Environment Setup

  * **Runtime:** Python $3.10+$ (Developed and tested using $3.13$).
  * **API Key:** A valid Google Generative API key (Gemini) with a **sufficiently provisioned quota** for high-volume multimodal processing.

### Quick Setup (Local Deployment)

1.  **Clone the Repository and Initialize VENV:**
    ```powershell
    python -m venv .venv
    & .venv\Scripts\Activate.ps1
    ```
2.  **Dependency Resolution:** Install the core libraries, including `pydantic` for structured output and `PyMuPDF` for **PDF rasterization**.
    ```powershell
    pip install -r requirements.txt
    ```
3.  **Credential Configuration:** Create a `.env` file in the project root to load the necessary environment variable.
    ```
    # GOOGLE_API_KEY must be set for the application to function.
    GOOGLE_API_KEY=sk-...your_key_here...
    ```

### Execution

To run the application locally on the default Streamlit port ($8501$):

```powershell
streamlit run app.py
```

-----

## ⚠️ Security & Operational Integrity

  * **API Key Non-Commitment:** Adhere strictly to operational security protocol: **Do NOT commit the `.env` file or API keys to the version control system.**
  * **Troubleshooting: Quota Errors:** **$429$ (Too Many Requests)** or quota exhaustion errors indicate a need to review Google Cloud Console for quota limits. Consider implementing asynchronous processing or utilizing a smaller, cost-optimized model for non-critical tasks.
  * **Scalability:** The current architecture is designed for **single-session parallelism**. Deployment at enterprise scale requires containerization (e.g., Docker/Kubernetes) and a robust load-balancing strategy.