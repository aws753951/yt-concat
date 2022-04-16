import os

from .step import Step
from yt_concat.setting import DOWNLOAD_DIR, VIDEOS_DIR, CAPTIONS_DIR


class Building(Step):

    def process(self, inputs, data):
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
