import streamlit as st
import PIL
from PIL import Image
import requests
import io
from dotenv import load_dotenv
import os

load_dotenv()


def app():
    st.title("RevSearch: Reverse Image Search Engine")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image of a car", type=["jpg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Resize image
        resized_image = image.resize((224, 224), PIL.Image.ANTIALIAS)

        # Encode resized_image as jpeg to send it to API
        image_byte_arr = io.BytesIO()
        resized_image.save(image_byte_arr, format="JPEG")
        encoded_image = image_byte_arr.getvalue()

        # Select the number of similar images to display
        num_similar_images = st.slider(
            "Select the number of similar images to display", 2, 6, 2
        )

        # API call
        REVERSE_IMAGE_SEARCH_API_URL = os.environ.get("REVERSE_IMAGE_SEARCH_API_URL")
        response = requests.post(
            REVERSE_IMAGE_SEARCH_API_URL,
            files={"image": encoded_image},
            data={"number_of_images": num_similar_images},
        )

        if response.status_code == 200:
            # Get the similar images from API response
            similar_images = response.json()["similar_images"]

            # Display similar images
            st.header("Similar Images")
            for idx, similar_image_url in enumerate(similar_images):
                st.image(
                    similar_image_url,
                    caption=f"Similar Image {idx+1}",
                    use_column_width=True,
                )
        else:
            st.error("Error retrieving similar images. Please try again.")


if __name__ == "__main__":
    app()
