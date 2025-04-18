import requests
import os
from text_api import text_api
import io
from PIL import Image
import cv2
import time
import numpy as np
# api = os.environ["image_api"]
# api_text = os.environ["text_api"]
def image_api(api,prompt):
    API_URL = api
    headers = {"Authorization": "Bearer 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"}

    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    
    prompts = prompt
    picture = 0
    for i in prompts:    
        image_raw_bytes = query({
            "inputs": i,
        })
        byte_array = np.frombuffer(image_raw_bytes, dtype=np.uint8)
        image = cv2.imdecode(byte_array, cv2.IMREAD_COLOR)
        #image = cv2.imread(image_bytes)
        #image = Image.open(io.BytesIO(image_bytes))
        print()
        print(image)
        print(image.shape)

        cv2.imwrite(str(picture)+"Output.jpg",image)
        picture += 1
        time.sleep(2)
