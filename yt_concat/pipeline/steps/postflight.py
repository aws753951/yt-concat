import shutil

from .step import Step
from yt_concat.setting import DOWNLOAD_DIR, VIDEOS_DIR, CAPTIONS_DIR, OUTPUT_DIR


class Postflight(Step):
    def process(self, inputs, data, utils):
        if inputs['cleanup'] == True:
            shutil.rmtree(VIDEOS_DIR)
            shutil.rmtree(CAPTIONS_DIR)

        print('delete videos and captions')
