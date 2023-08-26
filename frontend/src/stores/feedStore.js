import { defineStore } from "pinia";
import { useAxios } from "@vueblocks/vue-use-axios";
import axios from "axios";

export const useFeedStore = defineStore({
  id: "feedStore",
  state: () => ({
    categories: [],
    feed_list: [],
    article: "<div><h1>*** Hello, World! ***</h1></div>",
  }),

  actions: {
    async fetch_categories() {
      const url = "http://127.0.0.1:8000/categories";
      const response = await axios.get(url);
      // console.log(response.data.items);
      this.categories = response.data.items;
    },

    async fetch_feed_list() {
      const url = "http://127.0.0.1:8000/feed_list";
      const response = await axios.get(url);
      // console.log(response.data.items);
      this.feed_list = response.data.items;
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

    clear() {
      this.categories = [];
      this.feed_list = [];
      this.article = "";
    },
  },
});
