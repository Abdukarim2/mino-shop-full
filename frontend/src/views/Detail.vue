<template>
  <main>
    <section class="detail_page_section">
	  <div class="container_lg">
	  	<div class="detail_product_blocks" @dblclick="heart = !heart" id="product">
	  	 <span class="heart d_product_heart" @click="heart = !heart">
			<svg v-if="heart" 
			:class="{ heart_action: heart }" xmlns="http://www.w3.org/2000/svg"   fill="currentColor" viewBox="0 0 16 16">
				  <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
			</svg>
			<svg v-else :class="{ heart_action: !heart }" xmlns="http://www.w3.org/2000/svg"   fill="red" viewBox="0 0 16 16">
			  <path 
			  d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" />
			</svg>
		  </span>
	  	  <div class="detail_product_img">
	  	  	<a>
	  	  	  <!-- <picture>
						  <source media="(min-width:768px)" srcset="@/assets/img/t-shirst2.png">
						  <img src="@/assets/img/t-shirt.png" >
				    </picture> -->
				    <img :src="Array(product.get_img_url)[0]" :alt="product.name">
	  	  	</a>
	  	  </div>
	  	  <div class="detail_product_about">
	  	  	<div class="d_product_title">
	  	  	  <p>
	  	  	  	{{product.name}}
	  	  	  </p>
	  	  	</div>
	  	  	<div class="d_product_price">
	  	  	  <p>
	  	  	  	<span>{{product.priceDolor}} $</span> - {{product.price}} uzs
	  	  	  </p>
	  	  	</div>
	  	  	<div class="d_product_condition">
	  	  	  <p v-if="product.material">
	  	  	  	<b>Material :</b> 
				<span v-for="material in product.material">{{' '+materials[material-1]+' '}}</span>
	  	  	  </p>
	  	  	  <p>
	  	  	  	<b> Omborda :</b> mavjud. ({{Math.ceil(Math.random() * (15 - 3) + 3)}} ta qoldi)
	  	  	  </p>
	  	  	</div>
	  	  	<div class="d_product_about">
	  	  	  <p>Tovar haqida :</p>
	  	  	  <p ref="about">
	  	  	  	{{product.about}}
	  	  	  </p>
	  	  	</div>
	  	  	<div class="d_product_btn">
	  	  	  <a>
	  	  	  	<span>
	  	  	  	  <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16">
						    <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
						  </svg>
	  	  	  	</span>
	  	  	  	<span>Savatchaga olish</span>
	  	  	  </a>
	  	  	</div>
	  	  </div>
	  	  <div class="d_product_about about_product_mobile">
	  	    <p>Tovar haqida :</p>
  	  	    <p ref="about_mobile">
  	  	  	 
  	  	    </p>
  	  	  </div>
	  	</div>
	  </div>
	  <!-- start Deliver services -->
	  <Deliver>
	  	<div class="view_title">
			  <p>Tez va bepul yetkazib berish</p>
			</div>
	  </Deliver>
	  <!-- start Products -->
	  <Products :products="products">
		  <div class="view_title">
		    <p>TOP tovarlar</p>
		  </div>
	  </Products>
    </section>		
  </main>
</template>
<script>
import Products from "@/components/Products.vue"
import Deliver from "@/components/GlobalUI/Deliver.vue"
import axios from "axios"
export default{
	name:"Detail",
	data(){
		return {
			heart:true,
			product:{},
			products:[],
			materials:['Paxta', 'Sintetika', 'Boshqa'],
		}
	},
	components:{
		Products,
		Deliver
	},
	watch: {
		$route(val){
			if(val.params.slug && val.params.id){
				this.getDetail()
			}
		}
	},
	async beforeMount(){
		this.getDetail()
		await axios.get("api/products/get/?limit=4&random=True")
				   .then(response =>{
				   		this.products = response.data
				   })
	},
	methods: {
		async getDetail(){
			let id = this.$route.params.id;
			let slug = this.$route.params.slug;
			await axios.get(`api/products/detail/${slug}/${id}/`)
								.then(response=>{
										this.product = response.data
								})

			this.$refs.about.innerHTML = this.product.about
			this.$refs.about_mobile.innerHTML = this.product.about
		}
	},
}
</script>
<style>
  .detail_page_section{
  	padding: 30px 0px 50px 0px;
  }
  .detail_product_blocks{
  	display: flex;
  	padding: 25px;
  	background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		position: relative;
		flex-wrap: wrap;
  }
  .d_product_heart{
  	right: 12px;
  	top: 10px;
  }
  .d_product_heart svg{
  	width: 60px;
  }
  .detail_product_img{
  	width: 45%;
  	padding-right: 70px;
  }
  .detail_product_img a img{
  	width: 100%;
  }
  .detail_product_about{
  	width: 55%;
  	display: flex;
  	flex-direction: column;
  	justify-content: space-evenly;
  }
  .d_product_title{
  	font-family: poppins-bold;
  	font-size: 40px;
  	margin-bottom: 10px;
  }
  .d_product_price{
  	font-family: poppins-bolder;
  	font-size: 45px;
  }
  .d_product_price span{
  	color: #FE8947;
  }
  .d_product_condition{
  	font-family: poppins;
  	font-size: 25px;
  	margin-bottom: 20px;
  }
  .d_product_about{
  	font-family: poppins;
  	font-size: 22px;
  	margin-bottom: 20px;
  }
  .d_product_about p:first-child{
  	font-size: 25px;
  	margin-bottom: 10px;
  }
  .d_product_btn a{
  	display: inline-block;
  	padding:12px 0px;
  	text-align: center;
  	background:  #FFD600;
  	border-radius: 10px;
  	width: 350px;
  	font-family: poppins-bold;
  	font-size: 25px;
  	margin-top: 15px;
  }
  .d_product_btn a span svg{
  	width: 25px;
  	margin-right: 10px;
  }
  .about_product_mobile{
  	display: none;
  }
  @media(max-width: 1400px){
  	 .d_product_title{ 	
	  	font-size: 37px;
	  	margin-bottom: 0;
	 } 
	.d_product_price{
	  	font-size: 42px;
	 }
	 
	 .d_product_condition{
	 	font-size:22px;
	 }
	 .d_product_about{
	  	font-size: 20px;
	 }
	 .d_product_btn a{
	 	padding: 12px 0px;
	 	width: 330px;
	 	font-size:23px;
	  }
	 .d_product_about p:first-child{
	  	font-size: 23px;
	  }
  }
   @media(max-width: 1200px){
   	 .detail_product_img{
   	 	padding-right: 20px;
   	 }
  	 .d_product_title{ 	
	  	font-size: 35px;
	 } 
	.d_product_price{
	  	font-size: 40px;
	 } 
	 .d_product_condition{
	 	font-size:20px;
	 }
	 .d_product_about{
	  	font-size: 19px;
	 }
	 .d_product_btn a{
	 	width: 310px;
	 	font-size:21px;
	  }
	 .d_product_about p:first-child{
	  	font-size: 22px;
	  }
  }
  @media(max-width: 992px){
  	 .detail_product_blocks{
  	 	align-items: center;
  	 }
	 .detail_product_img{
	  	width: 45%;
	 }
	 .detail_product_about{
	  	width: 55%;
	 }
	 .d_product_about{
	   display: none;
	 }
	 .about_product_mobile{
	  	display: block;
	  	margin-top: 20px;
	  }
	 .d_product_price{
	  	margin: 15px 0px;
	 }
	 .d_product_heart svg{
	  	width: 50px;
	  }
  }
  @media(max-width:768px){
  	 .detail_product_blocks{
  		max-width: 600px;
  		margin: auto;
	  	flex-direction: column;
	 }
	 .detail_product_img{
	  	width: 100%;
	  	padding-right: 0px;
	 }
	 .detail_product_about{
	 	padding-top: 30px;
	  	width: 100%;
	 }
	 .d_product_about{
	   display: block;
	 }
	 .about_product_mobile{
	  	display: none;
	  }
	 .d_product_heart svg{
	  	width: 40px;
	  }
  }
  @media(max-width:500px){
  	 .d_product_title{ 	
	  	font-size: 30px;
	 } 
	 .d_product_price{
	  	font-size: 35px;
	 } 
	 .d_product_condition{
	 	font-size:18px;
	 }
	 .d_product_about{
	  	font-size: 18px;
	 }
	 .d_product_btn a{
	 	width: 100%;
	 	font-size:20px;
	  }
	 .d_product_about p:first-child{
	  	font-size: 21px;
	  }
  }
  @media(max-width:400px){
  	 .d_product_title{ 	
	  	font-size: 27px;
	 } 
	 .d_product_price{
	  	font-size: 30px;
	 } 
	 .d_product_condition,.d_product_about{
	 	font-size:16px;
	 }
	 .d_product_btn a{
	 	width: 100%;
	 	font-size:19px;
	  }
	 .d_product_about p:first-child{
	  	font-size: 20px;
	  }
	 .d_product_heart{
	  	right: 0;
	  	top: 0;
	  }
  }
</style>