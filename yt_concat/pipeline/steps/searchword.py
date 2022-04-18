from .step import Step
from yt_concat.model.found import Found

class SeachWord(Step):
    def process(self, inputs, data, utils):

        found = []
        for YT in data:
            url = YT.url
            if not utils.get_captions_exist(url):
                continue
            for caption in YT.captions:
                if inputs['word'] in caption:
                    time = YT.captions[caption]
                    t = Found(YT, caption, time)
                    found.append(t)

        return found
