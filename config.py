import subprocess
import os
basedir = os.path.abspath(os.path.dirname(__file__))

MEETING_ID_PATTERN = '^meet-[a-z]{5}$'
TIMESTAMP_PATTERN = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z'
TRANSCRIPTIONS_TABLE_COLUMNS = ['meeting_id', 'speaker_name', 'message', 'spoken_at']

class Config():
    # proc = subprocess.Popen('heroku config:get DATABASE_URL -a meeting-transcript', stdout=subprocess.PIPE, shell=True)
    # DATABASE_URL = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
    # print(DATABASE_URL)
    SQLALCHEMY_DATABASE_URI = os.environ.get['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False