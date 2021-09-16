from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'RedStore',
        'items': [
            {
                'name': 'flowers',
                'price': 100
            }
        ]
    },
    {
        'name': 'BlueStore',
        'items': [
            {
                'name': 'books',
                'price': 100
            }
        ]
    }
]

@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['name'])
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"