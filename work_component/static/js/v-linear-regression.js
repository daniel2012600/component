/*************************************
- 元件名:
        v-linear-regression.js
- 描述:
        線性迴歸分析圖
- 維度量值:
        dt、總銷售額
- html:
        id:必填，元件id，要有唯一性
- 限制:
        data裏面一定要有dt, dt格式一定'yyyy-mm-dd'
- 屬性:
        data : [{dt:'2020-10-01', 總銷售額:44},....]
- 依賴:
        <script src="/static/style/echarts/4.8.0/ecStat.js"></script>
- 作者:
        daniel
- 展示:
       https://echarts.apache.org/examples/zh/editor.html?c=scatter-linear-regression
- 使用範例:
       <v-echarts-pie id="pie" :data="piedata"></v-echarts-pie>
- 日期:
       2018-08-06 11:16
*************************************/


Vue.component("v-linear-regression", {
    props: {
        data: Array,
        y_label_format: {
            type: Function,
            default: (val, key) => val 
        },
        x_label_format: {
            type: Function,
            default: (val) => val
        },
    },
    watch: {
        data: function (newVal, oldVal) {
            this.render()
        }
    },
    template: `
        <div id="this.$attrs['id']" style="width: 100%; height: 450px;" ></div>
    `,
    data() {
        return {
            _chart: null
        };
    },
    methods: {
        fKNum(strNum) {
            if (strNum.length <= 3) {
                return strNum;
            }
            if (!RegExp('^(\\+|-)?(\\d+)(\\.\\d+)?$').test(strNum)) {
                return strNum;
            }
            var a = RegExp.$1,
                b = RegExp.$2,
                c = RegExp.$3;
            var re = new RegExp();
            re.compile("(\\d)(\\d{3})(,|$)");
            while (re.test(b)) {
                b = b.replace(re, "$1,$2$3");
            }

            return a + "" + b + "" + c;
        },
        render() {

            var thiscomp = this //有些method裏面引用不到this，就用這個
            //防止重覆呼叫，所以先清掉內文
            elobj = document.getElementById(this.$attrs['id']);
            elobj.innerHTML = "";
            elobj.removeAttribute("_echarts_instance_");
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById(this.$attrs['id']));

            var c_data = _.map(this.data,(v,k) =>{ 
                var c_data = [k+1,v.總銷售額]
                return c_data})
            
            var myRegression = ecStat.regression('linear', c_data);
            myRegression.points.sort(function(a, b) {
                result = a[0] - b[0]
                return  result;
            });
            var origin_date =  _.map(this.data,d=>{ return d.dt})
            var weekdays = "星期日,星期一,星期二,星期三,星期四,星期五,星期六".split(",");
            var e_date = _.map(origin_date,d=>{ 
                var week = weekdays[new Date(d).getDay()].split('星期')[1]
                var date_edition = d + ' '+'('+week+')'+ ' '
                        return date_edition  })
            var option = {
                title: {
                    text: '線性迴歸分析',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross'
                    },
                    formatter: params => { 
                                var dt = origin_date[params[0].axisValueLabel-1]
                                var my_format = `${dt}<br/>` +params.map(d => {
                                    var value = this.y_label_format(d.data[1]||0, d.seriesName);
                                    return `${d.marker}${d.seriesName}: ${value}`
                                }).join('</br>');
                                return my_format }
                },

                xAxis: {
                    type: 'category',
                    splitLine: {
                        lineStyle: {
                            type: 'dashed'
                        }
                    },
                    axisLabel: {
                        formatter: params => {
                            var index = this.x_label_format(params)-1
                            return e_date[index]
                        }
                    }
                },
                yAxis: {
                    type: 'value',
                    min: 1.5,
                    splitLine: {
                        lineStyle: {
                            type: 'dashed'
                        }
                    },
                },
                series: [{
                    name: '總銷售額',
                    type: 'scatter',
                    emphasis: {
                        label: {
                            show: true,
                            position: 'left',
                            color: 'blue',
                            fontSize: 16
                        }
                    },
                    data: c_data
                }, {
                    name: '趨勢線',
                    type: 'line',
                    showSymbol: false,
                    data: myRegression.points,
                    markPoint: {
                        itemStyle: {
                            color: 'transparent'
                        },
                        data: [{
                            coord: myRegression.points[myRegression.points.length - 1]
                        }]
                    }
                }]
            };
            


            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            thiscomp._chart = myChart;

            //將chart元件放在window._echartskey就是這個chart的id
            if(window._echarts == undefined){ window._echarts = {} }
            window._echarts[this.$attrs.id] = myChart;
        }
    },
    mounted: function () {
        var that = this;
        that.render();
        window.addEventListener('resize',function (){
            if(that._chart){
                that._chart.resize();
            }
        });
    },
});



