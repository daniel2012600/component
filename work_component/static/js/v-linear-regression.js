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
        predict :   預測數(想預測的日期)    ex:  公式為 y = 18715.99x + -3023.27  x為預測數(日期判定)
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
        predict_count:{
            type: Number,
            default: 0
        }
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
        format_dt(x, type) {
            switch (type) {
                case 'year':
                    return new Date(x).getFullYear().toString();
                    break;
                case 'm':
                    var month = this.months[new Date(x).getMonth()];
                    return month.toString();
                    break;
                case 'month':
                    dt = new Date(x)
                    return dt.getFullYear() + "/" + (dt.getMonth() + 1);
                    break;
                case 'day':
                case 'week':
                    return new Date(x).toISOString().slice(0, 10);
                    break;
                default:
                    return 'labeltype屬性沒設值出錯了'
            }
        },
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
        get_tooltip(param){
            var label = param.name.split("\n")[param.seriesIndex]
            return [
                '區間 ' + label + ': ' + '<br />',
                '- 最大值: ' + param.data[5],
                '- Q3: ' + param.data[4],
                '- 中位數: ' + param.data[3],
                '- Q1: ' + param.data[2],
                '- 最小值: ' + param.data[1]
            ].join('<br/>');
        },
        render() {

            var thiscomp = this //有些method裏面引用不到this，就用這個
            //防止重覆呼叫，所以先清掉內文
            elobj = document.getElementById(this.$attrs['id']);
            elobj.innerHTML = "";
            elobj.removeAttribute("_echarts_instance_");
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById(this.$attrs['id']));
            
            // if 預測數增加 1 日期便增加 1 ---------> if pre = 1  this.data.dt +1   dt+1 送去x  變成points 自然會出現y =>  [11,y]
            // console.log(this.data[this.data.length-1])
            // 一、尋找日期轉換!!! ok   注意: 日期計算有誤
            
            
            var c_data = _.map(this.data,(v,k) =>{ 
                var c_data = [k+1,v.總銷售額]
                return c_data})
            var myRegression = ecStat.regression('linear', c_data);
            var line_data = myRegression.points.sort(function(a, b) {
                result = a[0] - b[0]
                return  result;
            });
            // 塞 x  return y
            var a = myRegression.parameter.gradient
            var b = myRegression.parameter.intercept
            var new_list = []
            
            var data_count = this.data.length

            
            // 二、預測數有幾個 就要出現幾個x  ,  pre = 3  => x1,x2,x3   再由一個 []包住  => [ [x1,y1],[x2,y2],[x3,y3] ]  ok
            // new_list.push(x)
            // new_list.push(y)
            // console.log(new_list)
            // var linedata = c_data.push(new_list)
            // console.log(c_data)
            // 三、將舊的趨勢線資料更改成加上預測數及y    ok



            // 四、找尋預測數的趨勢線資料可否為虛線
            var origin_date =  _.map(this.data,d=>{ return d.dt})

            for(i=1;i<=this.predict_count;i++){
                var x = data_count + i
                var y = a * x + b
                myRegression.points.push([x,y])
                var my_day = new Date(this.data[this.data.length-1].dt)
                
                var tomorrow_date =    my_day.getFullYear() + "-" + (my_day.getMonth()+1) + "-" + (my_day.getDate()+i)
                origin_date.push(tomorrow_date)
            }
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
                                var a = params[0]
                                var dt = origin_date[params[0].axisValueLabel-1]
                                console.log(dt)
                                var my_format = `${dt}<br/>` +params.map(d => {
                                    var value = this.y_label_format(d.data[1]||0, d.seriesName);
                                    return `${d.marker}${d.seriesName}: ${value}`
                                }).join('</br>');
                                return my_format }
                },
                grid:{
                    bottom: '10',
                    containLabel: true
                },

                xAxis: {
                    type: 'category',
                    splitLine: {
                        lineStyle: {
                            type: 'dashed'
                        }
                    },
                    axisLabel: {
                        rotate:45,
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



