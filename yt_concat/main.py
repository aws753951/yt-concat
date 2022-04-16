
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.getvideolist import GetVideoList
from yt_concat.pipeline.steps.building import Building



def main():
    inputs = {
        'channel_id': 'UCIEv3lZ_tNXHzL3ox-_uUGQ'
    }

    steps = [
        Building(),
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
#

#
# get_all_video_in_channel()
