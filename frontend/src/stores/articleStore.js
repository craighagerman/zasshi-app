import { defineStore } from 'pinia'
import { useAxios } from '@vueblocks/vue-use-axios'
import axios from 'axios'


export const useArticleStore = defineStore({
  id: 'articleStore',
  state: () => ({
    articles: [],
    feedUrls: [],
    rssFeed: "",
    rssUrl: "http://127.0.0.1:8000/static_articles"
  }),
  actions: {
    async getData() {
        console.log("fetching...")
        const res = await fetch(this.rssUrl);
        const finalRes = await res.json();
        console.log(finalRes.items)
        this.articles = finalRes.items;
    },


    async fetchAxios() {
        const url = "http://127.0.0.1:8000/fetch_feed?q=" + this.rssFeed;
        const response = await axios.get(url)
        this.articles = response.data.items
    },

    async fetchAxiosUrl(xmlUrl) {
        const url = "http://127.0.0.1:8000/fetch_feed?q=" + xmlUrl;
        const response = await axios.get(url)
        this.articles = response.data.items
    },

    fetchBBC() {
        this.rssUrl = "http://127.0.0.1:8000/bbc_articles"
        this.getData()
        // this.fetch()
    },


    fetch() {
        if (this.rssFeed) {
            this.rssUrl = "http://127.0.0.1:8000/fetch_feed?q=" + this.rssFeed;
        }

        if (this.rssUrl) {
            this.getData()  
        }
    },


    async fetch_feed_list() {
        const url = "http://127.0.0.1:8000/feed_list"
        const response = await axios.get(url)
        console.log(response.data.items)
        this.feedUrls = response.data.items
    },


    clear() {
        this.rssUrl = ""
        this.rssFeed = ""
        this.articles = []
    },
    reset() {
        this.rssUrl = "http://127.0.0.1:8000/static_articles"
        this.rssFeed = ""
        this.articles = []
    }
    }
})
 
