import io
import requests
from PIL import Image
from requests.models import Response
import os
from dotenv import load_dotenv

load_dotenv()


def create_image_url_for_s3_lambda_api_gateway(
    base_url: str, bucket_name: str, image_path: str
) -> str:
    """Creates an image API URL for S3 reverse image search.

    Args:
        base_url (str): The base URL for the API Gateway.
        bucket_name (str): The S3 bucket name.
        image_path (str): The path to the image within the S3 bucket.

    Returns:
        str: The API URL to access the image.
    """
    return f"{base_url}/{bucket_name}?file={image_path}"


def fetch_image_api_response(image_api_url: str) -> Response:
    """Fetches the API response for the provided image API URL.

    Args:
        image_api_url (str): The API URL for accessing the image.

    Returns:
        Response: The requests.models.Response object containing the image data.
    """
    return requests.get(image_api_url)


def convert_response_to_pil_image(response: Response) -> Image.Image:
    """Converts the API response to a PIL.Image object.

    Args:
        response (Response): The requests.models.Response object containing the image data.

    Returns:
        Image.Image: The PIL.Image object representing the image.
    """
    image_data = response.content
    return Image.open(io.BytesIO(image_data))


def get_image_from_s3_bucket(image_api_url: str) -> Image.Image:
    """Fetches an image from an S3 bucket using the provided API URL.

    Args:
        image_api_url (str): The API URL for accessing the image.

    Returns:
        Image.Image: The PIL.Image object representing the image.
    """
    response = fetch_image_api_response(image_api_url)
    return convert_response_to_pil_image(response)


def lambda_api():
    BASE_S3_LAMDA_API_GATEWAY_URL = os.environ.get("BASE_S3_LAMDA_API_GATEWAY_URL")
    BUCKET_NAME_REV_SEARCH_DATABASE_IMAGES = os.environ.get(
        "BUCKET_NAME_REV_SEARCH_DATABASE_IMAGES"
    )

    image_path = "images/000001_jpg.rf.5182495727dae412fdb258232cd8a86a.jpg"
    image_api_url = create_image_url_for_s3_lambda_api_gateway(
        BASE_S3_LAMDA_API_GATEWAY_URL, BUCKET_NAME_REV_SEARCH_DATABASE_IMAGES, image_path
    )
    image = get_image_from_s3_bucket(image_api_url)
    image.show()


if __name__ == "__main__":
    lambda_api()
