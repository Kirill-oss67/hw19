import calendar
import datetime

import jwt
from flask_restx import abort

from app.constants import algo, secret


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def generate_tokens(self, username, password):
        user = self.user_service.get_by_name(username)
        if user is None:
            return {"error": "Несуществующий логин"}, 401
        password_hash = self.user_service.get_hash(password)
        if password_hash != user.password:
            return {"error": "Неверный пароль"}, 401
        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens

    def refresh_jwd(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=secret, algorithms=algo)
        except Exception:
            abort(400)

        username = data.get("username")
        user = self.user_service.get_by_name(username)
        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens
