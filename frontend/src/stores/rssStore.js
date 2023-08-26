import { defineStore } from "pinia";
import { useAxios } from "@vueblocks/vue-use-axios";
import axios from "axios";

export const useRssStore = defineStore({
  id: "rssStore",
  state: () => ({
    feedUrls: [],
  }),
  actions: {
    async fetch_feed_list() {
      const url = "http://127.0.0.1:8000/feed_list";
      const response = await axios.get(url);
      console.log(response.data.feeds);
      this.feedUrls = response.data.feeds;
    },

    clear() {
      this.feedUrls = [];
    },
  },
});
