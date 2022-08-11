<template>
  <div class="product_top_pr_block">
  	<div class="product_top_pr_title">
  	  <p>{{product.name}}</p>
  	</div>
  	<div class="product_top_pr_items">
  	  <div class="product_top_pr_img">
    	<router-link :to="'/detail/'+product.slug+'/'+product.id+'#product'">
    	<!--   <picture>
				 <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
				 <img src="@/assets/img/t-shirt.png" >
			  </picture> -->
			  <img :src="Array(product.get_img_url)[0]" :alt="product.name">
    	</router-link>
      </div>
      <div class="product_top_pr_about">
    	<div class="top_pr_price">
    	  <p>
    	    <span>{{product.price}} uzs</span>
    	  </p>
    	</div>
    	<div class="top_pr_about">
    	  <p ref="productAbout"></p>
    	</div>
    	<div class="ptop_pr_condition">
    	  <p><b>Omborda</b>: mavjud. (11 ta qoldi)</p>
    	</div>
    	<div class="top_pr_btn">
    	  <a>
    	  	<svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16">
								    <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
					</svg>
    	  	Savatga
    	  </a>
    	</div>
      </div>	
  	</div>	
  </div>
</template>
<script>
export default{
	name:"TopProduct",
	props:{
		product:{
			type:Object,
		}
	},
	mounted(){
		this.$refs.productAbout.innerHTML = this.product.about.slice(0,120) + "..."
	}
}
</script>
<style>
	.product_top_pr_block{
		max-width:100%;
		padding:25px 25px;
		background-color: #fff;
		transition-property: box-shadow;
		transition-duration: 0.2s;
		transition-timing-function: ease-in;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		
	}
	.product_top_pr_items{
		display: flex;
		align-items: center;
	}
	.product_top_pr_block:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
	}
	.product_top_pr_title{
		font-size: 32px;
		font-family: poppins-bold;
		margin-bottom: 40px;
	}
	.product_top_pr_img,.product_top_pr_about{
		width: 50%;
	}
	.product_top_pr_img{
		padding-right: 20px;
	}
	.product_top_pr_about{
		padding-left: 20px;
	}
	.product_top_pr_img a img{
		width: 100%;
	}
	.top_pr_price{
		font-size: 33px;
		font-family: poppins-bolder;
		margin-bottom: 30px;
	}
	.top_pr_price span{
		color:  #FE8947;
	}
	.top_pr_about,.ptop_pr_condition{
		font-size: 17px;
		font-family: poppins;
	}
	.top_pr_about{
		margin-bottom: 15px;
	}
	.ptop_pr_condition{
		margin-bottom:35px;
	}
	.top_pr_btn a svg{
		width:25px;
	}
	.top_pr_btn a {
		display: inline-block;
		font-family: poppins-bolder;
		width: 90%;
		padding:15px;
		background-color: #FFD600;
		text-align: center;
		border-radius: 10px;
		font-size: 25px;
	}
	@media(max-width: 1400px){
		.top_pr_price{
			font-size: 28px;
		}
		.top_pr_about,.ptop_pr_condition{
			font-size: 15px;
		}
		.top_pr_btn a{
			font-size: 20px;
			padding:10px;
		}
		.product_top_pr_title{
			font-size: 30;
		}
	}
	@media(max-width: 1200px){
		.product_top_pr_items{
			flex-direction: column;
		}
		.product_top_pr_img,.product_top_pr_about{
			width: 100%;
		}
		.top_pr_about,.ptop_pr_condition{
			font-size: 17px;
		}
		.top_pr_price{
			margin: 20px 0px;
		}
		.top_pr_btn{
			text-align: center;
		}
		.product_top_pr_title{
			text-align: center;
		}
		.product_top_pr_img,.product_top_pr_about{
			padding: 0;
		}
	}
	@media(max-width: 992px){
		.product_top_pr_block{
			padding: 15px;
		}
	}
	@media(max-width:768px){
		.top_pr_price{
			font-size: 25px;
			margin-bottom: 10px;
		}
		.product_top_pr_title{
			font-size: 23px;
		}
		.top_pr_btn a{
			font-size: 18px;
			padding:8px;
		}
		.top_pr_about,.ptop_pr_condition{
			font-size: 15px;
		}
		.ptop_pr_condition{
			margin-bottom: 20px;
		}
		.product_top_pr_block{
			max-width: 500px;
			margin: auto;
		}
	}
</style>