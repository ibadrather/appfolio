import streamlit as st
import PIL
from PIL import Image
import requests
from dotenv import load_dotenv
import os
from pages.RevSearchEngine.SearchEngine import ImageSearchEngine

load_dotenv()

# Create an instance of ImageSearchEngine with the necessary configurations
MODEL_PATH = "pages/RevSearchEngine/models/efficientnet_feature_encoder.onnx"
MODE = "search"
IMAGES_DIR = "/home/ibad/Desktop/RevSearch/Car196_Combined/images/"
METADATA_DIR = "pages/RevSearchEngine/cars_dataset_metadata_dir"
FEATURE_EXTRACTOR_NAME = "efficientnet_onnx"


def app():
    st.title("RevSearch: Reverse Image Search Engine")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image of a car", type=["jpg", "png", "jpeg", "ppm", "bmp", "tiff"])

    if uploaded_image is not None:
        image = (
            Image.open(uploaded_image)
            .convert("RGB")
            .resize((224, 224), PIL.Image.Resampling.LANCZOS)
        )

        st.image(image, caption="Uploaded Image", use_column_width=False)

        # Get similar image
        # Select the number of similar images to display
        number_of_images_to_get = st.slider(
            "Select the number of similar images to display", 2, 6, 2
        )

        # if it is greater than 6, set it to 6
        if number_of_images_to_get > 6:
            number_of_images_to_get = 6

        image_search_engine = ImageSearchEngine(
            model_path=MODEL_PATH,
            images_dir=IMAGES_DIR,
            mode=MODE,
            metadata_dir=METADATA_DIR,
            feature_extractor_name=FEATURE_EXTRACTOR_NAME,
        )
        similar_images_names_list = (
            image_search_engine.get_similar_images_list_from_image(
                image,
                number_of_images_to_get,
            )
        )

        # Jus keep the base name of the images
        similar_images_names_list = [
            os.path.basename(image_name) for image_name in similar_images_names_list
        ]

        # API call
        DEEP_IMAGE_SEARCH_WEBSITE_URL = os.environ.get("DEEP_IMAGE_SEARCH_WEBSITE_URL")
        ENDPOINT = os.environ.get("REVERSE_IMAGE_SEARCH_API_ENDPOINT")
        REVERSE_IMAGE_SEARCH_API_URL = DEEP_IMAGE_SEARCH_WEBSITE_URL + ENDPOINT

        # Create SimilarImagesRequest object
        similar_images_request = {
            "similar_images_names_list": similar_images_names_list
        }

        response = requests.post(
            REVERSE_IMAGE_SEARCH_API_URL,
            json=similar_images_request,
        )

        if response.status_code == 200:
            # Get the similar images from API response
            similar_images = response.json()["similar_images"]

            # Display similar images
            st.header("Similar Images")
            for idx, similar_image_base64 in enumerate(similar_images):
                st.image(
                    # similar_image_base64,
                    f"data:image/jpeg;base64,{similar_image_base64}",
                    caption=f"Similar Image {idx+1}",
                    use_column_width=False,
                    # format="JPEG",  # Change this to "PNG" if the images are in PNG format
                )
        else:
            st.error("Error retrieving similar images. Please try again.")


if __name__ == "__main__":
    app()
