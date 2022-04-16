import urllib.request
import json

from .step import Step
from yt_concat.setting import api_key


class GetVideoList(Step):

    def process(self, inputs):

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=2'.format(api_key,
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
            break
        print(video_links)

        return video_links
