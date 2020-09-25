import requests
from PIL import Image
from io import BytesIO
import os
import unidecode
import re
import json


class Files(object):
    def __init__(self, image_url):
        self.image_url = image_url

    @staticmethod
    def slugfy(text):
        text = unidecode.unidecode(text).lower()
        return re.sub(r'[\W_]+', '-', text)

    @staticmethod
    def open_url(image_url):
        response = requests.get(image_url)
        return Image.open(BytesIO(response.content))

    @staticmethod
    def open_local(image_url):
        return Image.open(image_url)

    @staticmethod
    def save(im, folder, file_name):
        folder = f"./output/{folder}"
        if not os.path.exists(folder):
            os.makedirs(folder)

        out_file = f"{folder}/{file_name}.png"
        print(out_file)

        im.save(out_file)

    @staticmethod
    def get_file_name(input1, input2):
        return f"{Files.slugfy(input1)}-{Files.slugfy(input2)}"

    @staticmethod
    def write_json(file, data):
         with open(file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def save_json(file, data):
        with open(file) as json_file: 
            temp = json.load(json_file) 
            temp.append(data)
            
        Files.write_json(file, temp) 
