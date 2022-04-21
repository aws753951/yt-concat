from pytube import YouTube

from .step import Step



class DownloadCaption(Step):

    def process(self, inputs, data, utils):

        for YT in data:
            url = YT.url

            if utils.get_captions_exist(url):
                print('found- ' + utils.get_id(url) + ' -captions')
                continue

            print('writing captions ' + url + ' here')
            try:
                source = YouTube(url)

                en_caption = source.captions.get_by_language_code('a.en')

                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                continue

            with open(utils.get_captions_path(url), "w", encoding='utf-8') as f:
                f.write(en_caption_convert_to_srt)

            print('caption files has been written down')

        return data
