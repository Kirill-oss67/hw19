import jwt
from flask import request
from flask_restx import abort
from app.constants import secret, algo


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer')[-1]
        try:
            jwt.decode(token, secret, algorithms=algo)
        except Exception:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            user = jwt.decode(token, secret, algorithms=algo)
            role = user.get('role')

        except Exception:
            abort(401)

        if role != 'admin':
            abort(401)

        return func(*args, **kwargs)

    return wrapper
