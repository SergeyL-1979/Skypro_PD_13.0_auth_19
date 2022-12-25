#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dao.model.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_username(self, user_name):
        return self.session.query(User).filter(User.username == user_name).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user_data):
        self.session.add(user_data)
        self.session.commit()

        return user_data

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

        return user
