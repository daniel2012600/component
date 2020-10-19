# -*- coding: utf-8 -*-
# ==============================[引用]==============================
from library.main_global import *
from library.main_help import *




@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=1)


# Daniel 測試
# ========== Component Demo頁 ==========
@app.route('/')
def layout():
    return render_template('component-layout.html')
@app.route('/board-item') #未完成
def board_item():
    return render_template('v-board-item-demo.html')

@app.route('/echarts-bar') #確認說明是否需修正
def echarts_bar():
    return render_template('v-echarts-bar-demo.html')

@app.route('/echarts-areastack') #確認說明是否需修正
def echarts_areastack():
    return render_template('v-echarts-areastack-demo.html')

@app.route('/echarts-barstack-dt')  #確認說明是否需修正
def echarts_barstack_dt():
    return render_template('v-echarts-barstack-dt-demo.html')

@app.route('/echarts-barstack')  #確認說明是否需修正
def echarts_barstack():
    return render_template('v-echarts-barstack-demo.html')

@app.route('/echarts-dataset-bar') #未完成
def echarts_dataset_bar():
    return render_template('v-echarts-dataset-bar-demo.html')    

@app.route('/echarts-grid-line') #確認說明是否需修正
def echarts_grid_line():
    return render_template('v-echarts-grid-line-demo.html')

@app.route('/echarts-large-trend') #確認說明是否需修正
def echarts_large_trend():
    return render_template('v-echarts-large-trend-demo.html')

@app.route('/echarts-mixlinebar-compare-dt') #確認說明是否需修正
def echarts_mixlinebar_compare_dt():
    return render_template('v-echarts-mixlinebar-compare-dt-demo.html')

@app.route('/echarts-mixlinebar-dt') #確認說明是否需修正
def echarts_mixlinebar_dt():
    return render_template('v-echarts-mixlinebar-dt-demo.html')

@app.route('/echarts-mixlinebar') #確認說明是否需修正
def echarts_mixlinebar():
    return render_template('v-echarts-mixlinebar-demo.html')

@app.route('/echarts-paytype') #確認說明是否需修正
def echarts_paytype():
    return render_template('v-echarts-paytype-demo.html')

@app.route('/echarts-pie') #確認說明是否需修正
def echarts_pie():
    return render_template('v-echarts-pie-demo.html')

@app.route('/linear-regression') #確認說明是否需修正
def linear_regression():
    return render_template('v-linear-regression-demo.html')

@app.route('/echarts-rfm') #確認說明是否需修正
def echarts_rfm():
    return render_template('v-echarts-rfm-demo.html')

@app.route('/echarts-rfm-lmh') #確認說明是否需修正
def echarts_rfm_lmh():
    return render_template('v-echarts-rfm-lmh-demo.html')

@app.route('/echarts-scatter-life-dt') #未完成
def echarts_scatter_life_dt():
    return render_template('v-echarts-scatter-life-dt-demo.html')

@app.route('/echarts-scattersingleaxis-dt') #未完成
def echarts_scattersingleaxis_dt():
    return render_template('v-echarts-scattersingleaxis-dt-demo.html')

@app.route('/echarts-taiwan') #確認說明是否需修正
def echarts_taiwan():
    return render_template('v-echarts-taiwan-demo.html')

@app.route('/echarts-waterfall') #確認說明是否需修正
def echarts_waterfall():
    return render_template('v-echarts-waterfall-demo.html')

@app.route('/echarts-year') #確認說明是否需修正
def echarts_year():
    return render_template('v-echarts-year-demo.html')

@app.route('/echarts.heatmap') #確認說明是否需修正
def echarts_heatmap():
    return render_template('v-echarts.heatmap-demo.html')

@app.route('/el-card') #確認說明是否需修正
def el_card():
    return render_template('v-el-card-demo.html')

@app.route('/el-cascader') #確認說明是否需修正
def el_cascader():
    return render_template('v-el-cascader-store.html')



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    socketio.run(app)
    # app.run()

