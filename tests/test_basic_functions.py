import pytest
from PIL import Image
from datetime import datetime, timedelta

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.RevSearchEngine.utils.request_limiter import RequestLimiter
from pages.RevSearchEngine.utils.image_utils import resize_image_based_on_aspect_ratio


@pytest.fixture
def request_limiter():
    return RequestLimiter(requests_per_day=2)


@pytest.fixture
def image():
    return Image.new("RGB", (600, 400))


def test_check_request_limit_within_limit(request_limiter):
    request_limiter.check_request_limit()
    assert request_limiter.requests_per_day_counter == 2


def test_check_request_limit_exceed_limit(request_limiter):
    request_limiter.requests_per_day_counter = 2
    with pytest.raises(
        Exception,
        match="You have reached the limit of requests per day. Please try again tomorrow.",
    ):
        request_limiter.check_request_limit()


def test_check_request_limit_new_day(request_limiter):
    request_limiter.requests_per_day_counter = 2
    request_limiter.last_request_date = datetime.now().date() - timedelta(days=1)
    request_limiter.check_request_limit()
    assert request_limiter.requests_per_day_counter == 1


def test_resize_image_based_on_aspect_ratio(image):
    resized_image = resize_image_based_on_aspect_ratio(image, output_image_width=200)
    assert resized_image.size == (200, 133)
