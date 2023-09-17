import { defineStore } from "pinia";
import { useAxios } from "@vueblocks/vue-use-axios";
import axios from "axios";

export const useFeedStore = defineStore({
  id: "feedStore",
  state: () => ({
    sections: [],
    section_name: "",
    channel_id: "",
    channel_name: "",
    channels: [],
    feed_list: [],
    feed_pane_title: "",
    article: "<div><h1>*** Hello, World! ***</h1></div>",
  }),

  actions: {
    async fetch_categories() {
      const url = "http://127.0.0.1:8000/categories";
      const response = await axios.get(url);
      this.sections = response.data.items;
    },

    async fetch_feed_list() {
      const url = "http://127.0.0.1:8000/feed_list";
      const response = await axios.get(url);
      this.feed_list = response.data.items;
    },

    async fetch_channels(query) {
      this.channels = []
      const url = "http://127.0.0.1:8000/channel_list?channel_id=" + query;
      const response = await axios.get(url);
      this.channel_id = response.data.name;
      this.channel_name = response.data.name;
      this.channels = response.data.items;
    },

    async fetch_feed(xmlUrl) {
        const url = "http://127.0.0.1:8000/fetch_feed?q=" + xmlUrl;
        console.log("POST: " + url)
        const response = await axios.get(url)
        this.feed_list = response.data.items
    },

    // async fetch_article() {
    //   const url = "http://127.0.0.1:8000/article";
    //   const response = await axios.get(url);
    //   console.log(response.data);
    //   this.article = response.data;
    // },

    async fetch_article(url) {
      // const url = "http://127.0.0.1:8000/article";
      const fullurl = "http://127.0.0.1:8000/get_article?url=" + url;
      const response = await axios.get(fullurl);
      console.log("fetching article...");
      // console.log(response.data);
      this.article = response.data;
    },

    set_category_name(name) {
      this.section_name = name;
    },

    clear_feed_list() {
      this.feed_list = [];
    },

    clear() {
      this.sections = [];
      this.feed_list = [];
      this.article = "";
    },
  },
});
