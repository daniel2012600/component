/*由多個元素組成，由左而右為:
  txt1 - val - txt2 - up - perc

Note:
    

Props:
    

Event:
    

Example:


*/
Vue.component("v-value-card-subtext", {
  delimiters: ["[[", "]]"],
  props: {
    id: {
      type: String,
      default: "id"
    },
    txt1: {
      type: String,
      default: "同比"
    },
    val: {
      type: String,
      default: "1999"
    },
    txt2: {
      type: String,
      default: "相比"
    },
    updntype: {
      type: String,
      default: "updn"
    },
    up: {
      type: Boolean,
      default: null
    },
    perc: {
      type: Number,
      default: "20"
    },
  },
  watch: {},
  template: `
    <div class="comparebox">
    <div class="comparebox__field">[[txt1]] [[val]] [[txt2]]</div>
      <span class="comparebox__increase" :class="{'text-danger': up, 'text-success': !up}">
        [[updn_char()]][[perc]]%
      </span>
    </div>
        `,
  data() {
    return {
     
    };
  },
  methods: {
    updn_char(){
      if(this.updntype == 'updn'){
          return this.up == true ? '▲' : this.up == false ? '▼' : ''
      }else{ // +-
        return this.up == true ? '+' : this.up == false ? '-' : ''
      }
    }
  },
  mounted: function() {}
});
