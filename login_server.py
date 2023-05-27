from flask import Flask
from flask_restful import Api, Resource, reqparse
from DatabaseConnector import insert_to_db, select_from_db

app = Flask(__name__)
api = Api()
users = []


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password_hash', type=str)
        parser.add_argument('role', type=str)
        data = parser.parse_args()

        query = f'''SELECT * FROM user WHERE email = "{data['email']}"'''
        info = select_from_db(query)
        print(info)
        if len(info) != 0:
            return 'already used'
        query = f'''INSERT INTO user(username, email, password_hash, role)
                VALUES (
                "{data['username']}",
                "{data['email']}",
                "{data['password_hash']}",
                "{data['role']}"
                );'''
        insert_to_db(query)
        return 'ok'


class Server(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password_hash', type=str)
        data = parser.parse_args()

        query = f'''SELECT * FROM user WHERE email = "{data['email']}"'''
        info = select_from_db(query)
        print(info)
        if len(info) != 1 or len(info[0]) < 4 or info[0][3] != data['password_hash']:
            return 'error'
        return 'ok'


api.add_resource(Register, "/api/register")
api.add_resource(Server,   "/api/login")
api.init_app(app)

app.run(debug=True, port=3000, host="localhost")
