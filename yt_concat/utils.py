import os

from .setting import DOWNLOAD_DIR, VIDEOS_DIR, CAPTIONS_DIR, OUTPUT_DIR


class Utils:

    def get_videos_path(self, inputs):
        return os.path.join(DOWNLOAD_DIR, inputs['channel_id'] + '.txt')

    def get_videos_exist(self, inputs):
        return os.path.exists(self.get_videos_path(inputs)) and os.path.getsize(self.get_videos_path(inputs)) > 0

    def get_captions_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_id(url) + '.txt')

    def get_id(self, url):
        return url.split('watch?v=')[-1]

    def get_captions_exist(self, url):
        return os.path.exists(self.get_captions_path(url)) and os.path.getsize(self.get_captions_path(url)) > 0

    def download_video_path(self, url):
        return os.path.join(VIDEOS_DIR, self.get_id(url) + '.mp4')

    def download_video_exist(self, url):
        return os.path.exists(self.download_video_path(url)) and os.path.getsize(self.download_video_path(url)) > 0

    def download_out_path(self, inputs):
        search_word = inputs['word']
        channel_id = inputs['channel_id']
        return os.path.join(OUTPUT_DIR, channel_id + '_' + search_word + '.mp4')