import json
import pydash as py_


class LookupService:


    def get_lookup_area_store(self):
        x = [{"store_area":"未分區","store_id":"232","store_name":"嘉義仁愛店#232"},{"store_area":"未分區","store_id":"279","store_name":"板橋莒光店#279"},{"store_area":"未分區","store_id":"141","store_name":"逢甲福星店#141"},{"store_area":"未分區","store_id":"227","store_name":"高雄大社店#227"},{"store_area":"未分區","store_id":"152","store_name":"土城裕民店#152"},{"store_area":"未分區","store_id":"366","store_name":"大里成功店#366"},{"store_area":"未分區","store_id":"131","store_name":"彰化民族店#131"},{"store_area":"未分區","store_id":"205","store_name":"桃園大竹店#205"},{"store_area":"未分區","store_id":"365","store_name":"潭子勝利店#365"},{"store_area":"未分區","store_id":"309","store_name":"路竹中正店#309"},{"store_area":"未分區","store_id":"370","store_name":"高雄建興店#370"},{"store_area":"未分區","store_id":"29","store_name":"大竹店#29"},{"store_area":"未分區","store_id":"317","store_name":"土城延和店#317"},{"store_area":"未分區","store_id":"360","store_name":"基隆義二店#360"},{"store_area":"未分區","store_id":"271","store_name":"左營崇德店#271"},{"store_area":"未分區","store_id":"387","store_name":"新竹南大店#387"},{"store_area":"未分區","store_id":"329","store_name":"新莊輔大店#329"},{"store_area":"未分區","store_id":"246","store_name":"板橋中山店#246"},{"store_area":"未分區","store_id":"217","store_name":"桃園中正店#217"},{"store_area":"未分區","store_id":"209","store_name":"豐原南陽店#209"},{"store_area":"未分區","store_id":"67","store_name":"高雄文橫店#67"},{"store_area":"未分區","store_id":"48","store_name":"鹿港復興店#48"},{"store_area":"未分區","store_id":"352","store_name":"五甲自強店#352"},{"store_area":"未分區","store_id":"301","store_name":"台北木新店#301"},{"store_area":"未分區","store_id":"340","store_name":"屏東樂福店#340"},{"store_area":"未分區","store_id":"267","store_name":"文山興隆店#267"},{"store_area":"未分區","store_id":"203","store_name":"梧棲文化店#203"},{"store_area":"未分區","store_id":"345","store_name":"淡水英專店#345"},{"store_area":"未分區","store_id":"224","store_name":"中和景新店#224"},{"store_area":"未分區","store_id":"191","store_name":"桃園大園店#191"},{"store_area":"未分區","store_id":"142","store_name":"竹東長春店#142"},{"store_area":"未分區","store_id":"5","store_name":"永靖店#5"},{"store_area":"未分區","store_id":"237","store_name":"斗六站前店#237"},{"store_area":"未分區","store_id":"51","store_name":"沙鹿中山店#51"},{"store_area":"未分區","store_id":"229","store_name":"仁德中清店#229"},{"store_area":"未分區","store_id":"196","store_name":"嘉義新生店#196"},{"store_area":"未分區","store_id":"236","store_name":"新竹光復店#236"},{"store_area":"未分區","store_id":"259","store_name":"楠梓德賢店#259"},{"store_area":"未分區","store_id":"21","store_name":"虎尾中正店#21"}]

        return x


    def get_lookup_bhv(self):
        x = [{"bhv1":"未知","bhv2":"未知"},{"bhv1":"儲值","bhv2":"外送"},{"bhv1":"未知","bhv2":"未知"},{"bhv1":"積點","bhv2":"外送"},{"bhv1":"積點","bhv2":"現場"},{"bhv1":"積點","bhv2":"自取"},{"bhv1":"購買","bhv2":"外送"},{"bhv1":"購買","bhv2":"現場"},{"bhv1":"購買","bhv2":"自取"}]
        return x


    def get_lookup_ord_type(self):
        x =[{"ord_paytype":"未知"},{"ord_paytype":"3212"},{"ord_paytype":"手機會員卡結帳"},{"ord_paytype":"晶片卡結帳"},{"ord_paytype":"會員卡加值"},{"ord_paytype":"未知"}]
        return x

    def get_lookup_ord_paytype(self):
        x =[{"ord_paytype":"未知"},{"ord_paytype":"APP外送結帳"},{"ord_paytype":"手機會員卡結帳"},{"ord_paytype":"晶片卡結帳"},{"ord_paytype":"會員卡加值"},{"ord_paytype":"未知"}]
        return x


    def get_lookup_prd_cat(self):
        x = [{"store_area":"未分區","store_id":"191","store_name":"桃園大園店#191"},{"store_area":"未分區","store_id":"142","store_name":"竹東長春店#142"},{"store_area":"未分區","store_id":"5","store_name":"永靖店#5"},{"store_area":"未分區","store_id":"237","store_name":"斗六站前店#237"},{"store_area":"未分區","store_id":"51","store_name":"沙鹿中山店#51"},{"store_area":"未分區","store_id":"229","store_name":"仁德中清店#229"},{"store_area":"未分區","store_id":"196","store_name":"嘉義新生店#196"},{"store_area":"未分區","store_id":"236","store_name":"新竹光復店#236"},{"store_area":"未分區","store_id":"259","store_name":"楠梓德賢店#259"},{"store_area":"未分區","store_id":"21","store_name":"虎尾中正店#21"}]
        return x

    def get_lookup_touch(self):
        x = [{"store_area":"未分區","store_id":"271","store_name":"左營崇德店#271"},{"store_area":"未分區","store_id":"387","store_name":"新竹南大店#387"},{"store_area":"未分區","store_id":"329","store_name":"新莊輔大店#329"},{"store_area":"未分區","store_id":"246","store_name":"板橋中山店#246"},{"store_area":"未分區","store_id":"217","store_name":"桃園中正店#217"},{"store_area":"未分區","store_id":"209","store_name":"豐原南陽店#209"},{"store_area":"未分區","store_id":"67","store_name":"高雄文橫店#67"},{"store_area":"未分區","store_id":"48","store_name":"鹿港復興店#48"},{"store_area":"未分區","store_id":"352","store_name":"五甲自強店#352"},{"store_area":"未分區","store_id":"301","store_name":"台北木新店#301"},{"store_area":"未分區","store_id":"340","store_name":"屏東樂福店#340"},{"store_area":"未分區","store_id":"267","store_name":"文山興隆店#267"},{"store_area":"未分區","store_id":"203","store_name":"梧棲文化店#203"},{"store_area":"未分區","store_id":"345","store_name":"淡水英專店#345"},{"store_area":"未分區","store_id":"224","store_name":"中和景新店#224"},{"store_area":"未分區","store_id":"191","store_name":"桃園大園店#191"},{"store_area":"未分區","store_id":"142","store_name":"竹東長春店#142"},{"store_area":"未分區","store_id":"5","store_name":"永靖店#5"},{"store_area":"未分區","store_id":"237","store_name":"斗六站前店#237"},{"store_area":"未分區","store_id":"51","store_name":"沙鹿中山店#51"},{"store_area":"未分區","store_id":"229","store_name":"仁德中清店#229"},{"store_area":"未分區","store_id":"196","store_name":"嘉義新生店#196"},{"store_area":"未分區","store_id":"236","store_name":"新竹光復店#236"},{"store_area":"未分區","store_id":"259","store_name":"楠梓德賢店#259"},{"store_area":"未分區","store_id":"21","store_name":"虎尾中正店#21"}]
        return x