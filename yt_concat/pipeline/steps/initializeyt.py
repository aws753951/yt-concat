from .step import Step
from yt_concat.model.yt import YT

class InitializeYT(Step):

    def process(self, inputs, data, utils):
        return [YT(url) for url in data]