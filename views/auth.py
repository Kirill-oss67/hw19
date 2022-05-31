from flask import request
from flask_restx import Resource, Namespace, abort
from app.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)
        tokens = auth_service.generate_tokens(username, password)
        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        if refresh_token is None:
            abort(400)
        tokens = auth_service.refresh_token(refresh_token)
        return tokens, 201
