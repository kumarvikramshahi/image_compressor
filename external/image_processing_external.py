import requests
from PIL import Image
from io import BytesIO

def compress_image_in_memory(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Create a BytesIO object to hold the compressed image data
    output_img = BytesIO()

    # Save the image to the BytesIO object with reduced quality (50%)
    img.save(output_img, format='JPEG', quality=50)

    # Get the compressed image data as bytes
    output_img_bytes = output_img.getvalue()

    return output_img_bytes

# Example usage:
image_url = 'https://example.com/image.jpg'  # Replace with your image URL
compressed_image_bytes = compress_image_in_memory(image_url)

# Now you can use `compressed_image_bytes` as needed, such as sending it over a network or processing further.
