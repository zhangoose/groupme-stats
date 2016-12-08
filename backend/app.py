from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

import requests

from client import GroupmeAPI
from helpers import validate_list_messages_args
from bucket import bucket_by_person, no_bucket
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
    offset = request.args.get('offset')
    bucket_by = request.args.get('bucket_by')

    # setting up the client
    access_token = request.headers.get('Authorization')

    with call_api(access_token) as api:
        try:
            response = api.get_messages(group_id, limit=offset)
        except GroupmeAPIError:
            return jsonify({
                "status": 400,
                "title": "Groupme API Error"
            })

    data = None
    if bucket_by == "user":
        data = bucket_by_person(response)
    else:
        data = no_bucket(response)

    return jsonify({"data": data})



if __name__ == "__main__":
    app.debug = True
    app.run()

