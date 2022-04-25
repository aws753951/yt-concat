import logging

def logger_yt(level):

    logger = logging.getLogger('yt')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
    file_handler = logging.FileHandler('logger.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)


