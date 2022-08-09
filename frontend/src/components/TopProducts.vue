<template>
  <section class="top_products_section">
  	<div class="container_lg">
  	  <slot></slot>
  	  <div class="top_products_blocks">
  	  	<div class="top_products_block" v-for="product in products">	
  	  	  <TopProduct :product="product"></TopProduct>
  	  	</div>	
  	  </div>
  	</div>
  </section>
</template>
<script>
import TopProduct from "@/components/GlobalUI/TopProduct.vue"
export default{
	name:"TopProducts",
	components:{
		TopProduct
	},
	props:{
		products:{
			type:Array,
		}
	}
}
</script>
<style>
	.top_products_section{
		margin:20px 0px 40px 0px;
	}
	.top_products_blocks{
		display: flex;
		flex-wrap: wrap;
	}
	.top_products_block{
		padding: 0px 12px;
	}
	.top_products_block{
		padding-top: 10px;
		padding-bottom: 10px;
		max-width: 50%;
	}
	@media(max-width: 768px){
		.top_products_block:nth-child(1n+1){
			padding-right:10px;
		}
		.top_products_block{
			padding-top: 10px;
			padding-bottom: 10px;
		}
		.top_products_block:nth-child(1n+2){
			padding-left:10px;
		}
	}
	@media(max-width: 576px){
		.top_products_block{
			padding: 10px !important;
		}
		.top_products_blocks{
			flex-direction: column;
		}
		.top_products_block{
			max-width: 100%;
		}
	}
</style>