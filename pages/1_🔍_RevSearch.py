import streamlit as st
import PIL
from PIL import Image
import requests
from dotenv import load_dotenv
import os
from pages.RevSearchEngine.SearchEngine import ImageSearchEngine
from pages.RevSearchEngine.utils.image_utils import resize_image_based_on_aspect_ratio
from pages.RevSearchEngine.utils.request_limiter import RequestLimiter
import io
import base64

load_dotenv()

# Create an instance of ImageSearchEngine with the necessary configurations
MODEL_PATH = "pages/RevSearchEngine/models/efficientnet_feature_encoder.onnx"
MODE = "search"
IMAGES_DIR = "/home/ibad/Desktop/RevSearch/Car196_Combined/images/"
METADATA_DIR = "pages/RevSearchEngine/cars_dataset_metadata_dir"
FEATURE_EXTRACTOR_NAME = "efficientnet_onnx"

OUTPUT_IMAGE_WIDTH = 400

limiter = RequestLimiter(requests_per_day=300)


def app():
    st.title("RevSearch: Reverse Image Search Engine")

    st.markdown(
        """
### Introducing RevSearch: A Car Reverse Image Search Engine MVP

RevSearch is an initial MVP developed for demonstrating a car reverse image search engine app. It's a work in progress that employs cutting-edge technologies, making it an excellent addition to your portfolio. The app utilizes machine learning, computer vision, Facebook AI Similarity Search, FastAPI, Onnxruntime, AWS S3, Lambda, API Gateway, and Heroku to provide users with a seamless and efficient reverse image search experience.

"""
    )

    # Upload image
    st.subheader("Upload an Image of a Car")
    uploaded_image = st.file_uploader(
        "The encoder is trained on a dataset containing images of 196 cars",
        type=["jpg", "png", "jpeg", "ppm", "bmp", "tiff"],
    )

    if uploaded_image is not None:
        image = (
            Image.open(uploaded_image)
            .convert("RGB")
            .resize((224, 224), PIL.Image.Resampling.LANCZOS)
        )

        # resize the image based on aspect ratio for display
        dispaly_image = resize_image_based_on_aspect_ratio(
            image, output_image_width=OUTPUT_IMAGE_WIDTH
        )

        st.image(dispaly_image, caption="Uploaded Image", use_column_width=False)

        # Get similar image
        # Select the number of similar images to display
        number_of_images_to_get = st.slider(
            "Select the number of similar images to display", 2, 6, 2
        )

        # if it is greater than 6, set it to 6
        if number_of_images_to_get > 6:
            number_of_images_to_get = 6

        # Check if the API call limit has been reached
        try:
            limiter.check_request_limit()
            print("Current: ", limiter.requests_per_day_counter)
        except Exception as e:
            st.warning(str(e))
            return

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
            col1, col2 = st.columns(2)  # Create two columns
            columns = [col1, col2]

            for idx, similar_image_base64 in enumerate(similar_images):
                # convert to image
                simialr_image_to_display = Image.open(
                    io.BytesIO(base64.b64decode(similar_image_base64))
                )

                simialr_image_to_display = resize_image_based_on_aspect_ratio(
                    simialr_image_to_display, output_image_width=OUTPUT_IMAGE_WIDTH
                )
                columns[idx % 2].image(  # Display image in alternating columns
                    simialr_image_to_display,
                    caption=f"Similar Image {idx+1}",
                    use_column_width=False,
                )
        else:
            st.error("Error retrieving similar images. Please try again.")

    # technologies used
    st.markdown(
        """
## Technologies Used

| Category                             | Technologies                                |
|--------------------------------------|---------------------------------------------|
| **Core Technologies**                | Python, PyTorch, ONNX, ONNX Runtime, Pandas |
| **Data Preprocessing & Augmentation**| Albumentations                              |
| **Model Optimization & Tracking**    | MLflow, Optuna                              |
| **Web App & Deployment**             | Streamlit, FastAPI, Docker, Heroku          |
| **Cloud Services**                   | AWS S3, AWS API Gateway, AWS Lambda         |
| **CI/CD & Code Quality**             | Github Actions, Black, Pytest               |
| **Image Processing**                 | PIL                                         |


"""
    )

    # Information about the app
    st.markdown(
        """
#### Features:

* Upload car images in various formats (jpg, png, jpeg, ppm, bmp, tiff) and let RevSearch find similar images from a comprehensive dataset.
* Interactive slider to select the number of similar images to display (up to 6).
* EfficientNet feature extractor for accurate search results.
* Fast API integration for seamless user experience.

As an early-stage MVP, RevSearch showcases your skills and expertise in advanced technologies and offers a solid foundation for further improvements and refinements. Give it a try and explore the potential of visual search in the automotive domain!

## About the Dataset

RevSearch is fueled by the Cars dataset, an engaging collection of 16,185 images across 196 car classes, which originated from Stanford University AI Lab. 

The feature extractor (Encoder) at the core of RevSearch is trained using this comprehensive dataset. The training process was carried out with Pytorch and optimized using Optuna, while progress was diligently tracked with MLflow.

At present, our training dataset and image database comprise 16,185 images. As a work in progress, we are dedicated to expanding the dataset by adding more images in the future, continually improving the performance of our reverse image search engine. 

## App Limitations

Although the Cars dataset provides a solid foundation for RevSearch, it is essential to acknowledge its limitations:

1. **Limited and outdated data**: The dataset was collected in 2016, making it relatively old and potentially less relevant for today's car models. This limitation may affect the accuracy of the search results, particularly for newer vehicles.

2. **Future data additions**: While we are dedicated to expanding the dataset with more recent images, this process is slow and iterative. It will take time to gather, preprocess, and integrate new data into the existing database, which may affect the timeliness of the app's enhancements.

3. **MVP status**: The current version of RevSearch is an early-stage Minimum Viable Product (MVP). It demonstrates the potential of visual search in the automotive domain and our expertise in advanced technologies. However, as an MVP, it might not provide the complete set of features and capabilities users may expect from a fully developed product.

4. **Potential biases**: The dataset's origin from Stanford University AI Lab may introduce geographical biases, as the majority of the images might be from the United States. This limitation could affect the accuracy and diversity of search results for car models that are more prevalent in other regions.

As I continue to improve and refine RevSearch, we will address these limitations by expanding the dataset, incorporating user feedback, and refining the feature extraction and search algorithms. This iterative process will help me create a more accurate and comprehensive reverse image search engine for the automotive domain.

### DeepSearchLite: A Lightweight and Versatile Library for Efficient Similarity Searches

DeepSearchLite, a custom lightweight library I developed, efficiently finds similar items in large datasets across various data types. With a lean design, minimal dependencies, and a versatile feature set, it is ideal for deployment in applications like RevSearch.

**Key Advantages of DeepSearchLite:**

* **Minimal Dependencies**: Simplifies deployment and integration into projects.
* **Versatility**: Supports a range of data types, including images, text, and other feature vector-representable data.
* **Efficient Similarity Search**: Utilizes advanced techniques like FAISS indexing for fast, accurate results, especially useful in projects like RevSearch.
* **Easy Integration**: Seamless integration with custom feature encoders, streamlining the incorporation process and enhancing utility.


### DeepSearchLite in RevSearch

I leveraged DeepSearchLite's capabilities to power RevSearch's core functionality, enabling efficient similarity searches within a large dataset and providing flexibility for various data types and encoders. DeepSearchLite's minimal dependencies and easy integration made it the perfect choice for implementing RevSearch's similarity search process.

By using DeepSearchLite in RevSearch, I demonstrated the library's effectiveness and showcased its potential for various applications. Its lean design and versatile feature set make it an invaluable asset for projects requiring efficient and accurate similarity searches across different data types. The development and deployment of DeepSearchLite highlight my ability to create custom solutions that enhance the performance and adaptability of my projects.
"""
    )


if __name__ == "__main__":
    app()
