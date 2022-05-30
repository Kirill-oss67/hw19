from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from app.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        response = UserSchema(many=True).dump(all_users)
        return response, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/movies/{user.id}"}


@user_ns.route('/<int:id>')
class UserView(Resource):
    def get(self, id):
        user = user_service.get_one(id)
        response = UserSchema().dump(user)
        return response, 200

    def put(self, id):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = id
        user_service.update(req_json)
        return "", 204

    def delete(self, id):
        user_service.delete(id)
        return '', 204
