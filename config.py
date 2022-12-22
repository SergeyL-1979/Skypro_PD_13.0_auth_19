#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = True
    JSON_AS_ASCII = False
    SECRET_KEY = '249y823r9v8238r9u'  # Так и не пойму как генерить данный код для сессии?
    SQLALCHEMY_DATABASE_URI = "sqlite:///movies.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'order.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
