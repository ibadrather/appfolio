import streamlit as st
from PIL import Image
import requests
from url import BASE_URL

# Set page tab display
st.set_page_config(
    page_title="Captioning Images",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.header("Captioning my friends in photos! 📸")
st.markdown(
    """
            > This is a simple image uploader app that uses a custom model to caption my friends in images.

            > Currently it is only trained on 3 people, but I plan to expand it to more people in the future.

            > I am continiously developing this app to learn more about machine learning and deployment.
            """
)

st.markdown("---")

### Create a native Streamlit file upload input
st.markdown("### Let's see if it captions my friends correctly. 👇")
img_file_buffer = st.file_uploader("Upload an image")

if img_file_buffer is not None:

    col1, col2 = st.columns(2)

    with col1:
        ### Display the image user uploaded
        st.image(
            Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️"
        )

    with col2:
        with st.spinner("Wait for it..."):
            ### Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()

            ### Make request to  API (stream=True to stream response as bytes)
            res = requests.post(
                BASE_URL + "/people_recognition_caption", files={"img": img_bytes}
            )

            if res.status_code == 200:
                ### Display the image returned by the API
                st.image(res.content, caption="Captioned Image! ☝️")
            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")
                print(res.status_code, res.content)
