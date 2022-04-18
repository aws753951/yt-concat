import os
from pytube import YouTube

from .step import Step
from yt_concat.setting import CAPTIONS_DIR


class DownloadCaption(Step):

    def process(self, inputs, data):

        for url in data:
            print(url)
            id = url.split('watch?v=')[-1]
            filepath = os.path.join(CAPTIONS_DIR, id + '.txt')

            if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
                print('found- ' + id + ' -captions')
                continue

            try:
                source = YouTube(url)

                en_caption = source.captions.get_by_language_code('a.en')

                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                continue

            with open(filepath, "w", encoding='utf-8') as f:
                f.write(en_caption_convert_to_srt)

        print(data)
        return data
