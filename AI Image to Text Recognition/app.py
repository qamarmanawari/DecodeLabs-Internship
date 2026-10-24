
import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

# -------------------------------
# 1. Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Text Recognition",
    page_icon="🔍",
    layout="centered"
)

# -------------------------------
# 2. Application Heading
# -------------------------------

st.title("AI Image to Text Recognition")
st.write(
    "Upload an image and let AI recognize "
    "the text inside it."
)

st.markdown("---")

# -------------------------------
# 3. Load Pre-trained AI Model
# -------------------------------

@st.cache_resource
def load_model():
    reader = easyocr.Reader(['en'], gpu=False)
    return reader

reader = load_model()

# -------------------------------
# 4. Upload Image
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "bmp"]
)

# -------------------------------
# 5. Image Recognition
# -------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Uploaded Image")

    st.image(
        image,
        caption="Input Image",
        use_container_width=True
    )

    if st.button("Recognize Text"):

        with st.spinner("AI is recognizing text..."):

            # Convert image to NumPy array
            image_array = np.array(image)

            # Convert RGB image to BGR
            image_array = cv2.cvtColor(
                image_array,
                cv2.COLOR_RGB2BGR
            )

            # Perform OCR
            results = reader.readtext(
                image_array,
                detail=0,
                paragraph=True
            )

            # Convert results into text
            extracted_text = "\n".join(results)

        # -------------------------------
        # 6. Display Output
        # -------------------------------

        st.subheader("Recognized Text")

        if extracted_text.strip():

            st.text_area(
                "Extracted Text",
                value=extracted_text,
                height=250
            )

            st.download_button(
                label="Download Recognized Text",
                data=extracted_text,
                file_name="recognized_text.txt",
                mime="text/plain"
            )

            st.success("Text recognition completed!")

        else:

            st.warning(
                "No text was detected in this image."
            )

else:

    st.info("Please upload an image to get started.")
