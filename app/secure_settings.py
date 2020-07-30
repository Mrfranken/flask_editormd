# -*- coding: utf-8 -*-
import os

# -*- coding: utf-8 -*-
# 千万千万不要将 127.0.0.1 写成 localhost
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8823443wsj_WIN@127.0.0.1:3306/taf_blog'  # pip install cymysql 是否可以加密数据库登录密码
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = '8823443wsj_WIN'

CHANGELOG_DIR = 'changelog'
CHANGELOG_PATH = os.path.join(os.path.dirname(__file__), CHANGELOG_DIR)

TASK_DIR = 'task'
TASK_PATH = os.path.join(os.path.dirname(__file__), TASK_DIR)
