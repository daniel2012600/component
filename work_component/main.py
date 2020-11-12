# -*- coding: utf-8 -*-
# ==============================[引用]==============================
import os
import sys
import datetime
import pandas as pd
import re
from service.lookup_service import LookupService
from flask import Flask
from flask import render_template
from flask import session

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




app = Flask(__name__, template_folder = './templates', static_folder = './static')
app.secret_key = pd.util.testing.rands(24)  # 使用session必要初始值

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=1)

# # ========== Component Demo頁 ==========
@app.route('/')
def layout():
    return render_template('component-layout.html')

@app.route('/board-item') 
def board_item():
    return render_template('v-board-item-demo.html')

@app.route('/echarts-bar') 
def echarts_bar():
    return render_template('v-echarts-bar-demo.html')

@app.route('/echarts-areastack') 
def echarts_areastack():
    return render_template('v-echarts-areastack-demo.html')

@app.route('/echarts-barstack-dt')  
def echarts_barstack_dt():
    return render_template('v-echarts-barstack-dt-demo.html')

@app.route('/echarts-barstack')  
def echarts_barstack():
    return render_template('v-echarts-barstack-demo.html')

@app.route('/echarts-dataset-bar') #未完成
def echarts_dataset_bar():
    return render_template('v-echarts-dataset-bar-demo.html')    

@app.route('/echarts-grid-line') 
def echarts_grid_line():
    return render_template('v-echarts-grid-line-demo.html')

@app.route('/echarts-large-trend') 
def echarts_large_trend():
    return render_template('v-echarts-large-trend-demo.html')

@app.route('/echarts-mixlinebar-compare-dt') 
def echarts_mixlinebar_compare_dt():
    return render_template('v-echarts-mixlinebar-compare-dt-demo.html')

@app.route('/echarts-mixlinebar-dt') 
def echarts_mixlinebar_dt():
    return render_template('v-echarts-mixlinebar-dt-demo.html')

@app.route('/echarts-mixlinebar') 
def echarts_mixlinebar():
    return render_template('v-echarts-mixlinebar-demo.html')

@app.route('/echarts-paytype') 
def echarts_paytype():
    return render_template('v-echarts-paytype-demo.html')

@app.route('/echarts-pie') 
def echarts_pie():
    return render_template('v-echarts-pie-demo.html')

@app.route('/linear-regression') 
def linear_regression():
    return render_template('v-linear-regression-demo.html')

@app.route('/echarts-rfm') 
def echarts_rfm():
    return render_template('v-echarts-rfm-demo.html')

@app.route('/echarts-rfm-lmh') 
def echarts_rfm_lmh():
    return render_template('v-echarts-rfm-lmh-demo.html')

@app.route('/echarts-scatter-life-dt')
def echarts_scatter_life_dt():
    return render_template('v-echarts-scatter-life-dt-demo.html')

@app.route('/echarts-scattersingleaxis-dt') 
def echarts_scattersingleaxis_dt():
    return render_template('v-echarts-scattersingleaxis-dt-demo.html')

@app.route('/echarts-taiwan') 
def echarts_taiwan():
    return render_template('v-echarts-taiwan-demo.html')

@app.route('/echarts-waterfall') 
def echarts_waterfall():
    return render_template('v-echarts-waterfall-demo.html')

@app.route('/echarts-year') 
def echarts_year():
    return render_template('v-echarts-year-demo.html')

@app.route('/echarts.heatmap') 
def echarts_heatmap():
    return render_template('v-echarts.heatmap-demo.html')

@app.route('/el-card') 
def el_card():
    return render_template('v-el-card-demo.html')

@app.route('/el-cascader') 
def el_cascader():
    return render_template('v-el-cascader-store-demo.html')

@app.route('/el-date-picker') 
def el_date_picker():
    return render_template('v-el-date-picker-demo.html')

@app.route('/el-select-dr') 
def el_select_dr():
    return render_template('v-el-select-dr-demo.html')

@app.route('/el-select-multi') 
def el_select_multi():
    return render_template('v-el-select-multi-demo.html')

@app.route('/leaflet') 
def leaflet():
    return render_template('v-leaflet-demo.html')

@app.route('/morris-area')
def morris_area():
    return render_template('v-morris-area-demo.html')
# ==============================[篩選器相關]==============================
@app.route('/lookup/area_store', methods=['POST'])
def lookup_area_store():
    ser = LookupService()
    data = ser.get_lookup_area_store()
    return json.dumps(data)


@app.route('/lookup/area_store_by_role', methods=['POST'])
def lookup_area_store_by_role():
    ser = LookupService()
    data = ser.get_lookup_area_store()
    return json.dumps(data)


@app.route('/lookup/bhv', methods=['POST'])
def lookup_bhv():
    ser = LookupService()
    data = ser.get_lookup_bhv()
    return json.dumps(data)


@app.route('/lookup/ord_type', methods=['POST'])
def lookup_ord_type():
    ser = LookupService()
    data = ser.get_lookup_ord_type()
    return json.dumps(data)


@app.route('/lookup/ord_paytype', methods=['POST'])
def lookup_ord_paytype():
    ser = LookupService()
    data = ser.get_lookup_ord_paytype()
    return json.dumps(data)


@app.route('/lookup/prd_cat', methods=['POST'])
def lookup_prd_cat():
    ser = LookupService()
    data = ser.get_lookup_prd_cat()
    return json.dumps(data)


@app.route('/lookup/touch', methods=['POST'])
def lookup_touch():
    ser = LookupService()
    data = ser.get_lookup_touch()
    return json.dumps(data)


@app.route('/orderfilter')
def orderfilter():
    return render_template('v-orderfilter-demo.html')

@app.route('/page-title')
def page_title():
    return render_template('v-page-title-demo.html')

@app.route('/sparkline-dt')
def sparkline_dt():
    return render_template('v-sparkline-dt-demo.html')

@app.route('/sparkline-pie')
def sparkline_pie():
    return render_template('v-sparkline-pie-demo.html')

@app.route('/table-info')
def table_info():
    return render_template('v-table-info-demo.html')

@app.route('/value-card-subtext')
def value_card_subtext():
    return render_template('v-value-card-subtext-demo.html')

@app.route('/value-card')
def value_card():
    return render_template('v-value-card-demo.html')



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run()

