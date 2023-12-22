from flask import Blueprint, jsonify, request

routes = Blueprint('api_routes', __name__)

@routes.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


#receive code from client and print the code
@routes.route('/api/code', methods=['POST'])
def code():
    text_data = request.data.decode('utf-8')
    processed_data = f"You sent: {text_data}"
    print(text_data)


    return jsonify({'message': 'Code received!'})