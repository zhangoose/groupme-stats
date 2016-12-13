from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

import requests

from client import GroupmeAPI
from helpers import validate_list_messages_args, filter_messages
from bucket import bucket_by_user, bucket_by_user_day
from contextmanagers import call_api
from errors import GroupmeAPIError


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/groups', methods=['GET'])
def list_groups():
    access_token = request.headers.get('Authorization')

    with call_api(access_token) as api:
        try:
            response = api.get_groups()
        except GroupmeAPIError:
            return jsonify({
                "status": 400,
                "title": "Groupme API Error"
            })
        
    return jsonify({
        "data": response.get('response')
    })


@app.route('/groups/<group_id>/messages', methods=['GET'])
def list_messages(group_id):
    # validation
    if not validate_list_messages_args(request.args):
        return jsonify({
            "status": 400,
            "title": "Bad URL params"
        })
    
    # parameters for this API endpoint
    bucket_by = request.args.get('bucket_by')
    start_date = int(request.args['start_date'])
    end_date = int(request.args['end_date'])

    # setting up the client
    access_token = request.headers.get('Authorization')

    with call_api(access_token) as api:
        messages = filter_messages(api, group_id, start_date, end_date)

    data = []
    if bucket_by == "user":
        data = bucket_by_user(messages)
    elif bucket_by == "user_day":
        data = bucket_by_user_day(messages)
    else:
        data = messages

    return jsonify({"data": data})


if __name__ == "__main__":
    app.debug = True
    app.run()

