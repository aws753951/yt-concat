import os


from yt_concat.setting import DOWNLOAD_DIR, VIDEOS_DIR, CAPTIONS_DIR, api_key
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.getvideolist import GetVideoList



def main():
    inputs = {
        'channel_id': 'UCIEv3lZ_tNXHzL3ox-_uUGQ'
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)



if __name__ == '__main__':
    main()

# id = []
# for line in video_links:
#     line = line.split('/watch?v=')[-1]
#     id.append(line)

# os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#
# temp =
#
# with open(temp, 'w', encoding='utf-8') as f:
#     for url in video_links:
#         f.write(url + '\n')
#
# get_all_video_in_channel()
