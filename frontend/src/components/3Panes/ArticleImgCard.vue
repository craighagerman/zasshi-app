
<template id="ArticleImgCard">
  <a class="block-link" :href="link" target="_blank">
    <div class="card">
      <div class="container">
        <h3>{{ title }}</h3>
        <p class="cardMeta">{{ source }} | {{ published }}</p>
        <p class="description">{{ description }}</p>
        <!-- <test v-on:click.native="testFunction"></test> -->
      </div>
    </div>
  </a>
</template>



<script>
export default {
  name: 'ArticleImgCard',
  props: {
    title: String,
    published: String,
    source: String,
    description: String,
    link: String,
    img: String
  },
  methods: {
    testFunction: function (event) {
      console.log('test clicked')
    }
  }
}
</script>


<!-- 
<style scoped>
.block-link {
  display: block;
  margin-left: 0px;
  /* margin-left: auto; */
  /* margin-right: auto; */
  color: black;
}

.card {
  /* Add shadows to create the "card" effect */
  margin: 25px 25px 25px 25px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 600px;
  text-align: left;
}

.description {
  font-size: small;
}

.cardMeta {
  /* font-weight: lighter; */
  color: cadetblue;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}

/* Add rounded corners to the top left and the top right corner of the image */
img {
  border-radius: 5px 5px 0 0;
  height: 200px;
  width: 50px;
}
</style> -->