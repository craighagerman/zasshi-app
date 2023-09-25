import { defineStore } from "pinia";
import { useAxios } from "@vueblocks/vue-use-axios";
import axios from "axios";

export const useSettingsStore = defineStore({
  id: "settingsStore",
  state: () => ({
    ui_mode: "navigationStack",
  }),
  // getters: {
  //   currentMode: (state) => state.ui_mode,
  // },
  actions: {
    async foo_bar() {    
      const response = await axios.get(url);
      this.sections = response.data.items;
    },

    set_stack_model() {
      this.ui_mode = "navigationStack"
    },

    set_accordion_model() {
      this.ui_mode = "accordion"
    },
  },
});
