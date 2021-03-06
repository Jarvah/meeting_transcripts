import os
import psycopg2
from app import db
# import subprocess
# proc = subprocess.Popen('heroku config:get DATABASE_URL -a meeting-transcript', stdout=subprocess.PIPE, shell=True)
# DATABASE_URL = proc.stdout.read().decode('utf-8').strip()
# conn = psycopg2.connect(str(DATABASE_URL), sslmode='require')


class Transcript(db.Model):
    __tablename__ = 'transcriptions'

    id = db.Column(db.Integer, primary_key=True)
    meeting_id = db.Column(db.String(10))
    speaker_name = db.Column(db.String())
    message = db.Column(db.Text())
    spoken_at = db.Column(db.DateTime())

    def __init__(self, meeting_id, speaker_name, message, spoken_at):
        self.meeting_id = meeting_id
        self.speaker_name = speaker_name
        self.message = message
        self.spoken_at = spoken_at



