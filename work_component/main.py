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
    return render_template('v-el-cascader-store-demo.html')

@app.route('/el-date-picker') #確認說明是否需修正
def el_date_picker():
    return render_template('v-el-date-picker-demo.html')

@app.route('/el-select-area') #未完成，
def el_select_area():
    return render_template('v-el-select-area-demo.html')

@app.route('/el-select-dr') #未完成，
def el_select_dr():
    return render_template('v-el-select-dr-demo.html')

@app.route('/el-select-multi') #確認說明是否需修正
def el_select_multi():
    return render_template('v-el-select-multi-demo.html')

@app.route('/leaflet') #確認說明是否需修正
def leaflet():
    return render_template('v-leaflet-demo.html')

@app.route('/ma-properties-action-sms')
def ma_properties_action_sms():
    return render_template('v-ma-properties-action-sms-demo.html')

@app.route('/ma-properties-birthday-after')
def ma_properties_birthday_after():
    return render_template('v-ma-properties-birthday-after-demo.html')

@app.route('/ma-properties-buy-name')
def ma_properties_buy_name():
    return render_template('v-ma-properties-buy-name-demo.html')

@app.route('/ma-properties-card')
def ma_properties_card():
    return render_template('v-ma-properties-card-demo.html')

@app.route('/ma-properties-click-link')
def ma_properties_click_link():
    return render_template('v-ma-properties-click-link-demo.html')

@app.route('/ma-properties-coupon')
def ma_properties_coupon():
    return render_template('v-ma-properties-coupon-demo.html')

@app.route('/ma-properties-example')
def ma_properties_example():
    return render_template('v-ma-properties-example-demo.html')

@app.route('/ma-properties-line')
def ma_properties_line():
    return render_template('v-ma-properties-line-demo.html')
@app.route('/ma-properties-no-buy-name')
def ma_properties_no_buy_name():
    return render_template('v-ma-properties-no-buy-name-demo.html')

@app.route('/ma-properties-no-click-link')
def ma_properties_no_click_link():
    return render_template('v-ma-properties-no-click-link-demo.html')

@app.route('/ma-properties-target-custom')
def ma_properties_target_custom():
    return render_template('v-ma-properties-target-custom-demo.html')

@app.route('/ma-properties-wait')
def ma_properties_wait():
    return render_template('v-ma-properties-wait-demo.html')

@app.route('/ma-task-card')
def ma_task_card():
    return render_template('v-ma-task-card-demo.html')

@app.route('/morris-area')
def morris_area():
    return render_template('v-morris-area-demo.html')

@app.route('/orderfilter')
def orderfilter():
    return render_template('v-orderfilter-demo.html')

@app.route('/page-title')
def page_title():
    return render_template('v-page-title-demo.html')

@app.route('/selectpage')
def selectpage():
    return render_template('v-selectpage-demo.html')

@app.route('/sparkline-dt')
def sparkline_dt():
    return render_template('v-sparkline-dt-demo.html')
@app.route('/sparkline-pie')
def sparkline_pie():
    return render_template('v-sparkline-pie-demo.html')

@app.route('/table-info')
def table_info():
    return render_template('v-table-info-demo.html')

@app.route('/tafilter')
def tafilter():
    return render_template('v-tafilter-demo.html')

@app.route('/tags')
def tags():
    return render_template('v-tags-demo.html')

@app.route('/updownrow')
def updownrow():
    return render_template('v-updownrow-demo.html')

@app.route('/value-card-subtext')
def value_card_subtext():
    return render_template('v-value-card-subtext-demo.html')

@app.route('/value-card')
def value_card():
    return render_template('v-value-card-demo.html')

@app.route('/widget')
def widget():
    return render_template('v-widget-demo.html')


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    socketio.run(app)
    # app.run()


