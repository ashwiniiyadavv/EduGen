import requests
import os
from text_api import text_api

# api = os.environ["image_api"]
# api_text = os.environ["text_api"]
def image_api(api,prompt):
    API_URL = api


    headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxx"}


    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    
    prompts = prompt
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
