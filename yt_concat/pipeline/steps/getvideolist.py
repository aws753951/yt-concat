import urllib.request
import json

from .step import Step
from yt_concat.setting import DOWNLOAD_DIR, api_key


class GetVideoList(Step):

    def process(self, inputs, data, utils):

        if utils.get_videos_exist(inputs):
            print('video list file exists')
            return self.read_file(utils.get_videos_path(inputs))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            inputs[
                                                                                                                'channel_id'])
        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:  # the outcome of trying
                break

        self.write_file(video_links, utils.get_videos_path(inputs))
        return video_links

    def write_file(self, video_links, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            video_links = []
            for url in f:
                video_links.append(url.strip())
        return video_links
