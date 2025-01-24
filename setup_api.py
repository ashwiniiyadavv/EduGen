import pandas as pd
import numpy as np
import os
from logger import logger


def api_calls(file):
    try:
        api = pd.read_excel(file,sheet_name="Sheet1",index_col="model")
        text_api = api.loc["text generation","api_link"]
        image_api = api.loc["text to image generation","api_link"]
        video_api = api.loc["text to video generation","api_link"]
        if type(video_api) != str:
                video_api = ""
        if type(text_api) != str:
                text_api = ""
        if type(image_api) != str:
                image_api = ""
        os.environ["text_api"] = text_api
        os.environ["image_api"] = image_api
        os.environ["video_api"] = video_api
        # # return api
    except Exception as e:
        logger.error("Check File Path or Format",exc_info=True)
