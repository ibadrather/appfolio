from PIL import Image
import PIL


def resize_image_based_on_aspect_ratio(
    image: Image, output_image_width: int = 400
) -> Image:
    """
    Resize image based on aspect ratio
    """
    # Get image size
    image_width, image_height = image.size

    # If image width is less than output image width, return original image
    if image_width < output_image_width:
        return image

    # Calculate aspect ratio
    aspect_ratio = image_width / image_height

    # Calculate new height
    new_height = int(output_image_width / aspect_ratio)

    # Resize image
    image = image.resize((output_image_width, new_height), PIL.Image.Resampling.LANCZOS)

    return image
