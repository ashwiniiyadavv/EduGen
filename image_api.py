import requests
import os
from text_api import text_api

api = os.environ["image_api"]
api_text = os.environ["text_api"]
def image_api(api):
    API_URL = api
    headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxx"}
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    
    prompts = text_api(api_text)
    picture = 0
    for i in prompts:    
        image_bytes = query({
            "inputs": i,
        })

        # You can access the image with PIL.Image for example
        import io
        from PIL import Image
        image = Image.open(io.BytesIO(image_bytes))
        image.save(str(picture)+".jpg")
        picture += 1
image_api(api)