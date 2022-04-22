from pytube import YouTube

from .step import Step
from yt_concat.setting import VIDEOS_DIR


class DownloadVideo(Step):

    def process(self, inputs, data, utils):

        yt_set = set([found.YT for found in data])
        for YT in yt_set:
            url = YT.url
            if utils.download_video_exist(url):
                print('found the same video', YT)
                continue

            print('downloading vidoes - ', YT)
            YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR,
                                                                   filename=utils.get_id(url) + '.mp4')

        print('downloaded videos')

        return data
