import os

from dotenv import load_dotenv
load_dotenv()  # 純讀取，還要定義變數才行
api_key = os.getenv('API_KEY')


DOWNLOAD_DIR = 'download'
VIDEOS_DIR = os.path.join(DOWNLOAD_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOAD_DIR, 'captions')
