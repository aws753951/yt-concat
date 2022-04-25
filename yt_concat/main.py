import sys
import getopt
import logging


sys.path.append('../')

from yt_concat.pipeline.pipeline import Pipeline
from yt_concat.pipeline.steps.getvideolist import GetVideoList
from yt_concat.pipeline.steps.building import Building
from yt_concat.pipeline.steps.downloadcaption import DownloadCaption
from yt_concat.utils import Utils
from yt_concat.pipeline.steps.initializeyt import InitializeYT
from yt_concat.pipeline.steps.readcaption import ReadCaption
from yt_concat.pipeline.steps.searchword import SeachWord
from yt_concat.pipeline.steps.download_video import DownloadVideo
from yt_concat.pipeline.steps.edit_video import EditVideo
from yt_concat.pipeline.steps.postflight import Postflight
from yt_concat.yt_log import yt_log




def main():
    inputs = {
        'channel_id': 'UCYvCbycHNeNiVOSvPhRy9lQ',
        'word': 'comparison',
        'limit': 5,
        'cleanup': True,
        'stream_logger': logging.INFO,
    }


    def print_usage():
        print('python main.py OPTTIONS')
        print('OPTTIONS:')
        print('{:>6} {:<20}{}'.format('-i', '--id', 'channel id of YT'))
        print('{:>6} {:<20}{}'.format('-w', '--word', 'the word we want'))
        print('{:>6} {:<20}{}'.format('-l', '--limit', 'the limit number of videos combined'))
        print('{:>6} {:<20}{}'.format('-c', '--cleanup', 'whether clean captions and video ingredients: True, False'))
        print('{:>6} {:<20}{}'.format('-s', '--stream_logger', 'level of streaming: DEBUG, INFO, WARNING, ERROR, CRITICAL'))

    short_opts = 'hi:w:l:c:s:'
    long_opts = 'help id= word= limit= cleanup= stream_logger= '.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ("-i", "--id"):
            inputs['channel_id'] = arg
        elif opt in ("-w", "--word"):
            inputs['word'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = arg
        elif opt in ("-c", "--cleanup"):
            inputs['cleanup'] = eval(arg)
        elif opt in ("-s", "--stream_logger"):
            inputs['stream_logger'] = eval(f'logging.{arg}')



    steps = [
        Building(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaption(),
        ReadCaption(),
        SeachWord(),
        DownloadVideo(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    yt_log(inputs['stream_logger'])
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
