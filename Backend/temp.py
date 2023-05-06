import io
import os
import requests
from PIL import Image
from typing import Union
from requests.models import Response
from dotenv import dotenv_values

# Load environment variables
config = dotenv_values(".env")


def create_image_url_for_s3_rev_image_search_lamda_api_gateway(
    base_url: str, bucket_name: str, image_path: str
) -> str:
    """Creates an image API URL for S3 reverse image search.

    Args:
        bucket_name (str): The S3 bucket name.
        image_path (str): The path to the image within the S3 bucket.

    Returns:
        str: The API URL to access the image.
    """
    image_api_url = f"{base_url}/{bucket_name}?file={image_path}"

    return image_api_url


def create_image_url_for_direct_s3_api_gateway_url(
    base_url: str, bucket_name: str, image_path: str
) -> str:
    """Creates an image URL for S3 reverse image search.

    Args:
        bucket_name (str): The S3 bucket name.
        image_path (str): The path to the image within the S3 bucket.

    Returns:
        str: The URL to access the image.
    """
    image_url = f"{base_url}/s3?key={bucket_name}/{image_path}"

    return image_url


def get_image_from_s3_bucket_via_lambda_gateway_api(image_api_url: str) -> Image.Image:
    """Fetches an image from an S3 bucket using the provided API URL.

    Args:
        image_api_url (str): The API URL for accessing the image.

    Returns:
        Image.Image: The PIL.Image object representing the image.
    """
    response = _fetch_image_api_response(image_api_url)

    # Convert response to image
    image = _convert_response_to_pil_image(response)

    return image


def get_image_from_s3_bucket_via_direct_api(image_url: str) -> Image.Image:
    """Fetches an image from an S3 bucket using the provided API URL.

    Args:
        image_api_url (str): The API URL for accessing the image.

    Returns:
        Image.Image: The PIL.Image object representing the image.
    """
    response = _fetch_image_api_response(image_url)

    image = response

    # Convert response to image
    # image = _convert_response_to_pil_image(response)

    return image


def _fetch_image_api_response(image_api_url: str) -> Response:
    """Fetches the API response for the provided image API URL.

    Args:
        image_api_url (str): The API URL for accessing the image.

    Returns:
        Response: The requests.models.Response object containing the image data.
    """
    response = requests.get(image_api_url)
    return response


def _convert_response_to_pil_image(response: Response) -> Image.Image:
    """Converts the API response to a PIL.Image object.

    Args:
        response (Response): The requests.models.Response object containing the image data.

    Returns:
        Image.Image: The PIL.Image object representing the image.
    """
    image = response.content

    # Convert image from bytes to PIL image
    image = Image.open(io.BytesIO(image))

    return image


BASE_S3_LAMDA_API_GATEWAY_URL = config["BASE_S3_LAMDA_API_GATEWAY_URL"]
BUCKET_NAME_REV_SEARCH_DATABSE_IMAGES = config["BUCKET_NAME_REV_SEARCH_DATABSE_IMAGES"]
BASE_S3_DIRECT_API_GATEWAY_URL = config["BASE_S3_DIRECT_API_GATEWAY_URL"]

image_path = "images/000001_jpg.rf.5182495727dae412fdb258232cd8a86a.jpg"


def direct_api():
    image_api_url = create_image_url_for_direct_s3_api_gateway_url(
        BASE_S3_DIRECT_API_GATEWAY_URL,
        BUCKET_NAME_REV_SEARCH_DATABSE_IMAGES,
        image_path,
    )
    image = get_image_from_s3_bucket_via_direct_api(image_api_url)
    print(image)
    # image.show()


def lamda_api():
    image_api_url = create_image_url_for_s3_rev_image_search_lamda_api_gateway(
        BASE_S3_LAMDA_API_GATEWAY_URL, BUCKET_NAME_REV_SEARCH_DATABSE_IMAGES, image_path
    )
    image = get_image_from_s3_bucket_via_lambda_gateway_api(image_api_url)

    image.show()


if __name__ == "__main__":
    # direct_api()
    lamda_api()
