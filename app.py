from flask import Flask, request, jsonify, render_template, abort, make_response
import json
import re
from flask_sqlalchemy import SQLAlchemy
import os
import subprocess
from config import *
import datetime
app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)

import model


@app.route("/")
def index():
    meeting_ids = []
    meeting_id_query_result = db.session.query(model.Transcript.meeting_id).distinct()
    print("sql")
    print(meeting_id_query_result)
    for mid in meeting_id_query_result:
        print(mid)
        meeting_ids.append(mid[0])
    print(meeting_ids)

    return render_template('index.html', meeting_ids=meeting_ids)


@app.route("/meetings", methods=["GET"])
def meeting():
    meeting_id = request.args.get('id')
    transcripts = db.session.query(model.Transcript).filter(model.Transcript.meeting_id == meeting_id)\
        .order_by(model.Transcript.spoken_at.asc())

    return render_template('transcript.html', meeting_id=meeting_id, transcripts=transcripts)


@app.route("/submit", methods=["POST"])
def submit():

    # data = request.get_json()
    try:
        data = json.loads(request.data)
    except json.decoder.JSONDecodeError:
        abort(400, "Request body not in JSON")

    print(data)
    for col in TRANSCRIPTIONS_TABLE_COLUMNS:
        if col not in data:
            abort(400, "Missing field: {}".format(col))

    if not (type(data["meeting_id"]) == str and re.match(MEETING_ID_PATTERN, data["meeting_id"])):
        abort(400, description="Wrong format for meeting_id. The format is '{}'".format(MEETING_ID_PATTERN))

    if not (type(data["spoken_at"]) == str and re.match(TIMESTAMP_PATTERN, data["spoken_at"])):
        abort(400, "Wrong format for spoken_at. The format is '{}'".format(TIMESTAMP_PATTERN))
    try:
        data["spoken_at"] = datetime.datetime.strptime(data["spoken_at"], "%Y-%m-%dT%H:%M:%Sz")
    except ValueError:
        abort(400, "Invalid datetime")

    data = model.Transcript(meeting_id=data["meeting_id"],
                            speaker_name=data["speaker_name"],
                            message=data['message'],
                            spoken_at=data["spoken_at"])
    db.session.add(data)
    db.session.commit()

    return make_response(jsonify(data.to_dict()), 201)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
