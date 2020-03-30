<h> Meeting-Transcripts </h>

app depolyed on https://meeting-transcript.herokuapp.com/

/submit endpoint

* Method: POST
* url: <base_url>/submit
* Headers:
  * KEY:Content-Type:application/json
* Body:
```json
{
    "meeting_id": "meet-hello",
    "speaker_name": "jarvah",
    "message": "Hello",
    "spoken_at": "2020-03-21T18:01:52Z"
}
```
Server will return 200 if the info successfully stored in the database
If 400, check the error message. Make sure there is no missing field and the format for `meeting_id` and `spoken_at` is correct.
