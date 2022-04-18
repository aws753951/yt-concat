from .step import Step

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
                for line in f:
                    if '-->' in line:
                        time = line.strip()
                        continue
                    caption = line.strip()
                    captions[caption] = time
            YT.captions = captions
            print(YT.captions)

        return data

