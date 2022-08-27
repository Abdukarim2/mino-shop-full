<template>
  <section class="categories_section">
		<div class="container_lg">
			<slot></slot>
		  <div class="categories_blocks">
		  	<div class="category_block" v-for="category in categories">
		  	  <router-link :to="'/products/'+category.slug+'/'" class="cart_category">
		  	  	<img :src="category.get_img_url" :alt="category.name">
		  	  	<p>
		  	  		{{category.name}}
		  	  	</p>
		  	  </router-link>
		  	</div>
		  </div>
		</div>	
  </section>
</template>
<script>
import CategoryCart from "@/components/GlobalUI/CategoryCart.vue"
import axios from "axios"
export default{
	name:"Categories",
	data(){
		return {
			categories:[]
		}
	},
	components:{
		CategoryCart
	},
	mounted(){
		  axios
				.get("api/categories/get/")
				.then(response=>{
					this.categories = response.data
				})
	}
}
</script>
<style>
	.categories_blocks{
		padding:0% 10%;
		display: flex;
		margin-bottom:40px;
		margin-top:30px;
	}
	.category_block{
		padding:0px 20px;
	}
	@media(max-width: 1200px){
		.categories_blocks{
			padding:0% 5%;
		}	
	}
	@media(max-width: 992px){
		.category_block{
			padding:0px 10px;
		}
	}
	@media(max-width: 768px){
		.categories_blocks{
			flex-wrap: wrap;
			justify-content: center;
		}
		.category_block{
			width: 33.333333%;
			padding: 10px;
		}
	}
	@media(max-width: 576px){
		.categories_blocks{
			padding: 0%;
		}
		.category_block{
			width: 50%;
			padding:5px;
		}
	}
</style>