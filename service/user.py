#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Метод хеширование пароля
import hashlib
import base64
import hmac

from dao.user import UserDAO

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_username(self, name):
        return self.dao.get_username(name)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data_user):
        data_user["password"] = self.get_hash(data_user["password"])
        return self.dao.create(data_user)

    def update(self, data):
        uid = data.get("id")
        user = self.get_one(uid)
        user.username = data.get("username")
        user.password = self.get_hash(data.get("password"))
        user.role = data.get("role")
        self.dao.update(user)
    # def update(self, data):
    #     data["password"] = self.get_hash(data["password"])
    #     self.dao.update(data)

    def get_hash(self, password):
        hash_digets = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Преобразовать пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64decode(hash_digets)
        # return hashlib.pbkdf2_hmac(
        #     'sha256',
        #     password.encode('utf-8'),  # Преобразовать пароль в байты
        #     PWD_HASH_SALT,
        #     PWD_HASH_ITERATIONS
        # ).decode("utf-8", "ignore")

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64encode(password_hash)

        hash_digets = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),  # Преобразовать пароль в байты
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digets)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            # user.password = data.get("password")
            user.password = self.get_hash(data.get("password"))
        if "role" in data:
            user.role = data.get("role")

        self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)
