from setup_api import api_calls
from text_api import text_api
from image_api import image_api
import os

#reading api to be used for modelling the output
api_calls("models.xlsx")
prompts = text_api(os.environ["text_api"])
print("Text Generation Completed")
image_api(os.environ["image_api"],prompt=prompts)
