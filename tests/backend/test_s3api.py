import os
from PIL import Image
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from Backend.get_objects_from_aws_s3_bucket import create_image_url_for_s3_lambda_api_gateway, get_image_from_s3_bucket

def test_lambda_api() -> None:
    base_url = os.environ["BASE_S3_LAMBDA_API_GATEWAY_URL"]
    bucket_name = os.environ["BUCKET_NAME_REV_SEARCH_DATABASE_IMAGES"]
    image_path = "images/000001_jpg.rf.5182495727dae412fdb258232cd8a86a.jpg"

    image_api_url = create_image_url_for_s3_lambda_api_gateway(base_url, bucket_name, image_path)
    image = get_image_from_s3_bucket(image_api_url)

    assert isinstance(image, Image.Image), "Image object not returned"

    print("Test passed")
