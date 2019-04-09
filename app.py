from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hello, world!'

class Testing(Resource):
    def get(self):
        return 'GET message received'
    
    def post(self):
        return 'POST message received: ' + request.data


    # @app.route('/hello', methods=['GET'])
    # def hello(self):
    #     return 'Hello, world!'

    # @app.route('/test', methods=['GET','POST'])
    # def test(self):
    #     if request.method == 'GET':
    #         return 'GET message received'
    #     elif request.method == 'POST':
    #         return 'POST message received: ' + request.data

api.add_resource(HelloWorld, '/hello')
api.add_resource(Testing, '/test')


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8081)
    app.run(host='0.0.0.0')