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
                    print('found specific word')
                    time = YT.captions[caption]
                    t = Found(YT, caption, time)
                    print(t.get_caption())
                    found.append(t)

        print(found)
        return found
