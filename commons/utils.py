import cloudinary
from cloudinary.api import resource, delete_resources

def get_public_id_from_url(image_url):

    # Get the public ID from the Cloudinary API
    response = resource(image_url)
    public_id = response.get('public_id')

    return public_id

def delete_cloudinary_image(image_url):

    # Get the public ID from the Cloudinary API
    public_id = get_public_id_from_url(image_url)
    if public_id:
        # Delete the image by its public ID
        delete_resources([public_id])
