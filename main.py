from flask import Flask, json, jsonify, request

from model.twit import Twit

twits = []

app = Flask(__name__)




@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def creat_twit():
    '''{"id": 1, "body": "Hello World", "author": "@aqaguy"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['id'], twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    serialized_twits = [twit.to_dict() for twit in twits]
    return jsonify({'twits': serialized_twits})


if __name__ == '__main__':
    app.run(debug=True)
