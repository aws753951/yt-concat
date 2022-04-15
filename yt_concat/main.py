import os
import urllib.request
import json

from yt_concat.setting import DOWNLOAD_DIR, VIDEOS_DIR, CAPTIONS_DIR


def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyD2vqQeukSQHObfv6bCw8cJn5JScPbKMSs'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

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

    # id = []
    # for line in video_links:
    #     line = line.split('/watch?v=')[-1]
    #     id.append(line)

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    temp = os.path.join(DOWNLOAD_DIR, channel_id + '.txt')

    with open(temp, 'w', encoding='utf-8') as f:
        for url in video_links:
            f.write(url + '\n')

    return video_links


get_all_video_in_channel('UCIEv3lZ_tNXHzL3ox-_uUGQ')
