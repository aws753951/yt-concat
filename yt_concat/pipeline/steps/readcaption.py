from .step import Step
import logging

class ReadCaption(Step):

    def process(self, inputs, data, utils):
        for YT in data:
            url = YT.url
            captions = {}
            if not utils.get_captions_exist(url):
                continue

            with open(utils.get_captions_path(url), 'r', encoding='utf-8') as f:
                time = None
                caption = None
                time_check = False
                for line in f:
                    if '-->' in line:
                        time = line.strip()
                        time_check = True
                        continue
                    if time_check:
                        caption = line.strip()
                        captions[caption] = time
                        time_check = False

            YT.captions = captions
        logging.getLogger('yt').info('yt class save dict of captions')

        return data

