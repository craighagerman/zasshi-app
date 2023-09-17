import { defineStore } from "pinia";
import { useAxios } from "@vueblocks/vue-use-axios";
import axios from "axios";

import ChannelView from "@/components/v2/ChannelView.vue";
import SectionView from "@/components/v2/SectionView.vue";


export const useComponentStore = defineStore({
  id: "componentStore",
  
  state: () => ({
    component: Object,
    last_component: Object,
    active_section: String,
  }),

  actions: {
    async fetch_categories() {
      const url = "http://127.0.0.1:8000/categories";
      const response = await axios.get(url);
      // console.log(response.data.items);
      this.sections = response.data.items;
    },


  },
});
