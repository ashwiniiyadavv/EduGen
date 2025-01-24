import requests
import pandas as pd
import os
from setup_api import api_calls

# api_calls("models.xlsx")
def text_api(api):
    url = api
    headers = {
        'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxx',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'Qwen/QwQ-32B-Preview',
        'messages': [
            {
                'role': 'user',
                'content': 'Create a sequence of image generation prompt to text to image to explain the concept of vehicle driving. Break the process into clear steps, ensuring each image represents one stage of the process with visual effects that are easy to understand and engaging for students. Each image should be visually appealing with clear labels and vibrant colors to make the learning process fun. The style should be cartoonish and vibrant to appeal to high school students, with bright greens, yellows, and blues to reflect nature and energy. give only images prompt only in points and no other text, just images prompt line by line thats it, max to max 10 lines'
            }
        ],
        'max_tokens': 500,
        'stream': False
    }

    response = requests.post(url, json=data, headers=headers)
    # return (response.json())
    return text_cleaning(response.json())


def text_cleaning(data):
    data = dict(data)
    model = data["model"]
    temp = data["choices"][0]["message"]["content"]
    temp = temp.split("\n")
    temp = [i for i in temp if i != ""]
    prompt = []
    for text in temp:
        for j in range(len(text)):
            if text[j] == " ":
                prompt.append(text[j+1:])
                break
    return prompt
