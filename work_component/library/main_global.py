# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import abort
from flask import Blueprint
from flask import session
from flask import redirect
from flask import url_for
from flask import jsonify
from flask import g
from flask_socketio import SocketIO
from flask_caching import Cache
from werkzeug.contrib.cache import SimpleCache
import os
import sys
import arrow
import json
import datetime as dt
import requests
import threading
import base64
import pandas as pd
import numpy as np
import time
import decimal
import functools
import string
import random
import logging
import datetime
import pytz
import google.cloud.logging
import pydash as py_
import re
from io import BytesIO
from dateutil import tz
from functools import wraps
from time import time, struct_time, mktime




app = Flask(__name__, template_folder = '../templates', static_folder = '../static')

cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# app.config.from_object('config.ProdConfig')
app.secret_key = pd.util.testing.rands(24)  # 使用session必要初始值

# socketio = SocketIO(app, async_mode='threading')

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  app.config['GCS_JSONKEY']


# web_url = app.config['WEB_URI']
# sqlconfig = app.config['SQL_CONFIG']
# bqgcs_config = app.config['BQGCS_CONFIG']
# mail_sender = app.config['MAIL_CONFIG']['EMAIL_SENDER']
# mail_key = app.config['MAIL_CONFIG']['SEND_GRID_KEY']
# sendinblue_sender = app.config['MAIL_CONFIG']['SEND_IN_BLUE_SENDER']
# sendinblue_key = app.config['MAIL_CONFIG']['SEND_IN_BLUE_KEY']

list_page_size = 10
tw_zone = pytz.timezone('Asia/Taipei')

