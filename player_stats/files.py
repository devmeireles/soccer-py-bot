import requests
from PIL import Image
from io import BytesIO

class Files(object):
    def __init__ (self, image_url):
        self.image_url = image_url
        
    @staticmethod
    def open_url(image_url):
        response = requests.get(image_url)
        return Image.open(BytesIO(response.content))

    @staticmethod
    def open_local(image_url):
        return Image.open(image_url)