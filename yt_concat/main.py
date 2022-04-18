
from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.getvideolist import GetVideoList
from yt_concat.pipeline.steps.building import Building
from yt_concat.pipeline.steps.downloadcaption import DownloadCaption
from yt_concat.utils import Utils
from yt_concat.pipeline.steps.initializeyt import InitializeYT
from yt_concat.pipeline.steps.readcaption import ReadCaption


def main():
    inputs = {
        'channel_id': 'UCIEv3lZ_tNXHzL3ox-_uUGQ'
    }

    steps = [
        Building(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaption(),
        ReadCaption()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)



if __name__ == '__main__':
    main()




