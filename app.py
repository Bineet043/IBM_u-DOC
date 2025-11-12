import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import io
import tempfile
import fitz  
import time

load_dotenv()

# Try to get API key from Streamlit secrets first (for cloud), then .env (for local)
api_key = None
try:
    # Streamlit Cloud uses st.secrets
    api_key = st.secrets.get("GOOGLE_API_KEY")
except:
    # Local development uses .env
    api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found! Please set it in Streamlit secrets or .env file.")
    st.stop()

genai.configure(api_key=api_key)

def find_img(prompt, image_data):
    # Use a model available to your API key.
    model = genai.GenerativeModel('models/gemini-2.5-flash-lite')

    # Helper to detect quota/rate-limit errors from exceptions
    def _is_quota_error(exc):
        s = str(exc).lower()
        return any(tok in s for tok in ("429", "quota", "rate limit", "exceeded"))

    # If the user requested a stub response (useful for local testing when quota
    # is exhausted), return a canned response instead of calling the API.
    try:
        if st.session_state.get("use_stub_response"):
            return "[STUB] Simulated response: the model would process the image and prompt."
    except Exception:
        # session_state may not be set when called outside Streamlit context; ignore.
        pass

    # Convert image bytes into a PIL Image when needed
    try:
        if isinstance(image_data, bytes):
            image = Image.open(io.BytesIO(image_data))
        else:
            image = image_data
    except Exception as e:
        return f"Error preparing image: {e}"

    # Retry loop with exponential backoff for transient quota/rate-limit errors
    max_retries = 3
    backoff_base = 1.0
    for attempt in range(1, max_retries + 1):
        try:
            response = model.generate_content([prompt, image])
            # The client may return an object with .text or similar; handle robustly
            try:
                return response.text
            except Exception:
                return str(response)
        except Exception as e:
            # If it's a quota/rate-limit error, retry with backoff up to max_retries
            if _is_quota_error(e) and attempt < max_retries:
                delay = backoff_base * (2 ** (attempt - 1))
                time.sleep(delay)
                continue
            # For quota / rate-limit final failure, return a friendly error message
            if _is_quota_error(e):
                return (
                    "Quota or rate-limit error from the Gemini API: your project appears to "
                    "have insufficient quota or billing. Please check billing/quotas."
                )
            # Other exceptions: show a concise error
            return f"Error processing image: {e}"


def input_img_setup(uploaded_file):
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            
            with tempfile.TemporaryDirectory() as temp_folder:
                images = []
                pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                for page_number in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_number)
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    images.append(img)
            
            image = images[0]
            
            with io.BytesIO() as output:
                image.save(output, format="JPEG")
                return output.getvalue()
        else:
            
            return uploaded_file.getvalue()
    else:
        raise FileNotFoundError("No File Uploaded")

st.title(":red[U-DOC] ")
st.header("Upload Image or PDF of your prescription or report")
uploaded_file = st.file_uploader(type=["jpg", "jpeg", "png", "webp","pdf"], label="")

if uploaded_file is not None:
    try:
        if uploaded_file.type != "application/pdf":
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error processing file: {e}")

imp = st.text_input("Chat with Presciption")

if imp:
    if uploaded_file is None:
        st.error("Please upload a file before submitting.")
    else:
        image_data = input_img_setup(uploaded_file)
        with st.spinner('Just a moment...'):
            # Removed long sleep for debugging to avoid blocking the UI
            pass
        prompt = imp
        response = find_img(prompt, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.")

res = st.button("Explore Prescription")
submit = st.button("Generate Data Report")
submit1 = st.button("Collect Medicine Names")

prompt1 = """
    accurately scan all text, regardless of whether it's typed or handwritten. The output should be a brief, detailed description that systematically breaks down and explains every key component of the prescription, including (but not limited to): medication names, dosages, frequencies, duration, route of administration, and any specific instructions or warnings and explain only what is written
    """

prompt2 = """
    Generate a Comprehensive Exploratory Data Analysis (EDA) Report for the uploaded dataset. The analysis must discover every structural component, statistical property, and underlying pattern. The final output must be delivered in a structured, hierarchical format, complete with relevant data visualizations
    """
prompt3 = """ 
    Extract all medicine names from the report/prescription, then search reputable online pharmacy sources to find their current price. Display the final list of medicines and their prices, sorted alphabetically (A-Z), in a clear table format."
    """

if submit1:
    if uploaded_file is None:
        st.error("Please upload a file before submitting.")
    else:
        image_data = input_img_setup(uploaded_file)
        with st.spinner('Just a moment...'):
          time.sleep(15)
        response = find_img(prompt3, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")

        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.")

if res:
    if uploaded_file is None:
        st.error("Please upload a file before submitting.")
    else:
        image_data = input_img_setup(uploaded_file)
        with st.spinner('Just a moment...'):
            # Removed long sleep for debugging to avoid blocking the UI
            pass
        response = find_img(prompt2, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.")

if submit:
    if uploaded_file is None:
        st.error("Please upload a file before submitting.")
    else:
        image_data = input_img_setup(uploaded_file)
        with st.spinner('Just a moment...'):
            # Removed long sleep for debugging to avoid blocking the UI
            pass
        response = find_img(prompt1, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.")


# Footer CSS removed for debugging (may cause rendering issues in some browsers)
footer = ""
# st.markdown(footer, unsafe_allow_html=True)