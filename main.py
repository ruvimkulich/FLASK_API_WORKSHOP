from flask import Flask, json, jsonify, request
from model.twit import Twit

app = Flask(__name__)

# Временные хранилища для постов и счетчик идентификаторов
twits = []
next_twit_id = 1


# Создание поста
@app.route('/twit', methods=['POST'])
def creat_twit():
    global next_twit_id
    '''{"body": "Hello World", "author": "@aqaguy"}
    '''
    twit_json = request.get_json()
    twit = Twit(next_twit_id, twit_json['body'], twit_json['author'])
    twits.append(twit)
    next_twit_id += 1
    return jsonify({'status': 'success'}), 201


# Получение всех постов
@app.route('/twit', methods=['GET'])
def read_twits():
    serialized_twits = [twit.to_dict() for twit in twits]
    return jsonify({'twits': serialized_twits}), 200


# Получение одного поста по ID
@app.route('/twit/<int:twit_id>', methods=['GET'])
def get_twit(twit_id):
    twit = next((t for t in twits if t.id == twit_id), None)
    if not twit:
        return jsonify({'status': 'not found'}), 404
    return jsonify(twit.to_dict()), 200


# Редактирование поста
@app.route('/twit/<int:twit_id>', methods=['PUT'])
def update_twit(twit_id):
    twit = next((t for t in twits if t.id == twit_id), None)
    if not twit:
        return jsonify({'status': 'not found'}), 404

    twit_json = request.get_json()
    twit.body = twit_json.get('body', twit.body)
    twit.author = twit_json.get('author', twit.author)
    return jsonify({'status': 'success'}), 200


# Удаление поста
@app.route('/twit/<int:twit_id>', methods=['DELETE'])
def delete_twit(twit_id):
    global twits
    twit = next((t for t in twits if t.id == twit_id), None)
    if not twit:
        return jsonify({'status': 'not found'}), 404

    twits = [t for t in twits if t.id != twit_id]
    return jsonify({'status': 'success'}), 204


if __name__ == '__main__':
    app.run(debug=True)
