from flask import request
from flask_restx import Resource, Namespace, abort
from app.implemented import user_service
from service.auth import generate_tokens
auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)
        if None in [username, password]:
            abort(400)
        user = user_service.get_by_name(username)
        if user is None:
            return {"error": "Неверные учётные данные"}, 401
        password_hash = user_service.get_hash(password)
        if password_hash != user.password:
            return {"error": "Неверные учётные данные"}, 401
        data = {
            "username": user.username,
            "role": user.role
        }
        tokens = generate_tokens(data )
        return tokens, 201

    def put(self):
        req_json = request.json
