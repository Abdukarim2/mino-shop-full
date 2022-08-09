<template>
<Transition name="slide-fade">
  <div class="cart_item" v-if="show">
  	<div class="cart_item_delete" @click="shakeDo = !shakeDo,
  	$emit('deleteCartItem'), show = !show">
  	  <a >
  	  	<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 33 35" fill="none">
				<path d="M14.25 14.75C14.25 13.9216 13.5784 13.25 12.75 13.25C11.9216 13.25 11.25 13.9216 11.25 14.75H14.25ZM11.25 26C11.25 26.8284 11.9216 27.5 12.75 27.5C13.5784 27.5 14.25 26.8284 14.25 26H11.25ZM21.75 14.75C21.75 13.9216 21.0784 13.25 20.25 13.25C19.4216 13.25 18.75 13.9216 18.75 14.75H21.75ZM18.75 26C18.75 26.8284 19.4216 27.5 20.25 27.5C21.0784 27.5 21.75 26.8284 21.75 26H18.75ZM29.25 7.25C29.25 6.42157 28.5784 5.75 27.75 5.75C26.9216 5.75 26.25 6.42157 26.25 7.25H29.25ZM6.75 7.25C6.75 6.42157 6.07843 5.75 5.25 5.75C4.42157 5.75 3.75 6.42157 3.75 7.25H6.75ZM1.5 5.75C0.671573 5.75 0 6.42157 0 7.25C0 8.07843 0.671573 8.75 1.5 8.75V5.75ZM31.5 8.75C32.3284 8.75 33 8.07843 33 7.25C33 6.42157 32.3284 5.75 31.5 5.75V8.75ZM20.625 7.25C20.625 8.07843 21.2966 8.75 22.125 8.75C22.9534 8.75 23.625 8.07843 23.625 7.25H20.625ZM9.375 7.25C9.375 8.07843 10.0466 8.75 10.875 8.75C11.7034 8.75 12.375 8.07843 12.375 7.25H9.375ZM11.25 14.75V26H14.25V14.75H11.25ZM18.75 14.75V26H21.75V14.75H18.75ZM26.25 7.25V29.75H29.25V7.25H26.25ZM24 32H9V35H24V32ZM6.75 29.75V7.25H3.75V29.75H6.75ZM9 32C7.75736 32 6.75 30.9926 6.75 29.75H3.75C3.75 32.6495 6.10051 35 9 35V32ZM26.25 29.75C26.25 30.9926 25.2426 32 24 32V35C26.8995 35 29.25 32.6495 29.25 29.75H26.25ZM1.5 8.75H31.5V5.75H1.5V8.75ZM23.625 7.25V5.375H20.625V7.25H23.625ZM18.375 0.125H14.625V3.125H18.375V0.125ZM9.375 5.375V7.25H12.375V5.375H9.375ZM14.625 0.125C11.7255 0.125 9.375 2.47551 9.375 5.375H12.375C12.375 4.13236 13.3824 3.125 14.625 3.125V0.125ZM23.625 5.375C23.625 2.47551 21.2745 0.125 18.375 0.125V3.125C19.6176 3.125 20.625 4.13236 20.625 5.375H23.625Z" fill="#404143"/>
				</svg>
  	  </a>
  	</div>
	<div class="cart_item_img">
	  <div class="cart_item_title">
	  	<p>Erni gapi gapmi ?!</p>
	  </div>
	  <div class="cart_item_img_slide">
	  	<div class="cart_item_image">
	  		<swiper :slides-per-view="1" :space-between="20" @swiper="swiperObj = $event">
			    <swiper-slide>
			    	<a>
			  	  <!--  <picture>
						    <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
						    <img src="@/assets/img/t-shirt.png" >
						  </picture> -->
						  <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
			  	  </a>
			    </swiper-slide>
			    <swiper-slide>
			    	<a>
			  	   <!-- <picture>
						    <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
						    <img src="@/assets/img/t-shirt.png" >
						  </picture> -->
						  <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
			  	  </a>
			    </swiper-slide>
			    <swiper-slide>
			    	<a>
			  	  <!--  <picture>
						    <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
						    <img src="@/assets/img/t-shirt.png" >
						  </picture> -->
						  <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
			  	  </a>
			    </swiper-slide>
			  </swiper>
	  	</div>
	  	<div class="cart_item_slide">
	  	  <div class="cart_item_slide_control" @click="slideToIndex = 0">
	  	   <a>
	  	    <!-- <picture>
				     <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
				     <img src="@/assets/img/t-shirt.png" >
				   </picture> -->
				   <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
	  	   </a>
	  	  </div>
	  	  <div class="cart_item_slide_control" @click="slideToIndex = 1">
	  	  	<a>
	  	  	  <!-- <picture>
				     <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
				     <img src="@/assets/img/t-shirt.png" >
				    </picture> -->
				    <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
	  	    </a>
	  	  </div>
	  	  <div class="cart_item_slide_control" @click="slideToIndex = 2">
	  	  	<a>
	  	  	 <!--  <picture>
				     <source media="(min-width:1200px)" srcset="@/assets/img/t-shirst2.png">
				     <img src="@/assets/img/t-shirt.png" >
				    </picture> -->
				    <img src="@/assets/img/t-shirt2.png" alt="t-shirt">
	  	    </a>
	  	  </div>
	  	</div>
	  </div>
	</div>
	<div class="cart_item_about">
	  <div class="cart_item_price">
	  	<p><span>$7.5</span> - 81.000 uzs</p>
	  </div>
	  <div class="cart_item_about_text">
	  	<p>
	  	  80% paxta va 20% poliesterdan tayyorlangan  sifatli futbolka. M ,L, XL, XXL hajmlarida mavjud.
          80% paxta va 20% poliesterdan tayyorlangan  sifatli futbolka. M ,L, XL, XXL hajmlarida mavjud.
      	</p>
	  </div>
	  <div class="cart_item_condition">
	  	<p><b>Omborda :</b> bor. (12- ta qoldi)</p>
	  	<p><b>Material :</b> paxta 80%, poliester 20%, </p>
	  </div>
	  <div class="edits_cart_item">
	  	<div class="edit_color">
	  	  <div class="edit_selections">
	  	  	<span></span> -
	  	  	<select>
	  	  	  <option>oq</option>
	  	  	  <option>oq</option>
	  	  	  <option>oq</option>
	  	  	</select>
	  	  </div>
	  	</div>
	  	<div class="edit_size">
	  	  <div class="edit_selections">
	  	  	<select>
	  	  	  <option>XL</option>
	  	  	  <option>XL</option>
	  	  	  <option>XL</option>
	  	  	</select>
	  	  </div>
	  	</div>
	  	<div class="edit_quantity">
	  	  <div class="edit_selections">
	  	  	<select>
	  	  	  <option>1</option>
	  	  	  <option>2</option>
	  	  	  <option>3</option>
	  	  	  <option>5</option>
	  	  	  <option>8</option>
	  	  	</select>
	  	  </div>
	  	</div>
	  </div>
	  <div class="buy_btn">
	  	<a>
	  	  <span>
	  	  	<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 40 40" fill="none">
					<path d="M20 23.3333H21.6667C23.5 23.3333 25 21.8333 25 20V3.33334H10C7.5 3.33334 5.31668 4.71665 4.18335 6.74998" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M3.33325 28.3333C3.33325 31.1 5.56659 33.3333 8.33325 33.3333H9.99992C9.99992 31.5 11.4999 30 13.3333 30C15.1666 30 16.6666 31.5 16.6666 33.3333H23.3333C23.3333 31.5 24.8333 30 26.6666 30C28.4999 30 29.9999 31.5 29.9999 33.3333H31.6666C34.4333 33.3333 36.6666 31.1 36.6666 28.3333V23.3333H31.6666C30.7499 23.3333 29.9999 22.5833 29.9999 21.6667V16.6667C29.9999 15.75 30.7499 15 31.6666 15H33.8166L30.9666 10.0167C30.3666 8.98335 29.2666 8.33334 28.0666 8.33334H24.9999V20C24.9999 21.8333 23.4999 23.3333 21.6666 23.3333H19.9999" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M13.3333 36.6667C15.1743 36.6667 16.6667 35.1743 16.6667 33.3333C16.6667 31.4924 15.1743 30 13.3333 30C11.4924 30 10 31.4924 10 33.3333C10 35.1743 11.4924 36.6667 13.3333 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M26.6666 36.6667C28.5075 36.6667 29.9999 35.1743 29.9999 33.3333C29.9999 31.4924 28.5075 30 26.6666 30C24.8256 30 23.3333 31.4924 23.3333 33.3333C23.3333 35.1743 24.8256 36.6667 26.6666 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M36.6667 20V23.3333H31.6667C30.75 23.3333 30 22.5833 30 21.6667V16.6667C30 15.75 30.75 15 31.6667 15H33.8166L36.6667 20Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M3.33325 13.3333H13.3333" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M3.33325 18.3333H9.99992" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					<path d="M3.33325 23.3333H6.66659" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
					</svg>
	  	  </span>
	  	  <span>Sotib olish</span>
	  	</a>
	  </div>
	</div>
 </div>
</Transition>
</template>
<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
export default{
	name:"CartItem",
	data(){
		return {
			shakeDo:false,
			swiperObj:null,
			slideToIndex:0,
			show:true
		}
	},
	components:{
		Swiper,
		SwiperSlide
	},
	watch:{
		slideToIndex(val){
			this.swiperObj.slideTo(val)
		}
	},
}
</script>
<style>
	.cart_item{
		background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding: 20px 30px;
		display: flex;
		align-items: center;
		position: relative;
		margin-bottom: 20px;
	}
	.cart_item:last-child{
		margin-bottom: 0px;
	}
	.cart_item_delete{
		position: absolute;
		width: auto;
		height: auto;
		right: 10px;
		top: 10px;
		padding:5px 10px;
		cursor: pointer;
	}
	.cart_item_delete a svg{
		width: 35px;
	}
	.cart_item_img{
		width: 50%;
	}
	.cart_item_about{
		width: 50%;
	}
	/* start vue transition */
	.slide-fade-enter-active {
	  transition: all 0.3s ease-out;
	}

	.slide-fade-leave-active {
	  transition: all 0.8s ;
	}

	.slide-fade-enter-from,
	.slide-fade-leave-to {
	  transform: translateX(50px);
	  opacity: 0;
	}
	/* end vue transition */
	/**/
	.cart_item_title{
		font-family: poppins-bold;
		font-size: 30px;
		margin-bottom: 20px;
	}
	.cart_item_img_slide{
		display: flex;
	}
	.cart_item_image a img{
		width: 100%;
	}
	.cart_item_image{
		width: 70%;
	}
	.cart_item_slide{
		width: 30%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding-bottom: 50px;
	}
	.cart_item_slide_control{
		width: 45px;
		height: 55px;
		border: 1px solid #857E7E;
		margin-bottom: 10px;
	}
	.cart_item_slide_control a img{
		width: 100%;
	}
    /**/
	.cart_item_price{
		font-family: poppins-bolder;
		font-size: 35px;
		margin-bottom: 10px;
	}
	.cart_item_price p span{
		color: #FE8947;
	}
	.cart_item_about_text{
		font-size: 18px;
		font-family: poppins;
		margin-bottom: 20px;
	}
	.cart_item_condition{
		font-size:18px;
		font-family: poppins;
		margin-bottom:30px;
	}
	.edits_cart_item{
		display: flex;
		align-items: center;
	}
	.edit_selections select{
		border: none;
		font-family: poppins;
		font-size: 18px;
		width: auto;
	}
	.edit_selections span{
		display: inline-block;
		width: 30px;
		height: 30px;
		border: 1px solid #000;
		margin-bottom: -10px;
	}
	.buy_btn a {
		display: block;
		text-align: center;
		padding: 9px 0px;
		border-radius: 10px;
		background-color: #FFD600;
		margin-top: 60px;
		font-family: poppins-bolder;
		font-size: 25px;
	}

	.buy_btn a span svg{
		width: 30px;
		transform: translateY(5px);
		margin-right: 10px;
	}
	@media(max-width: 1400px){
		.cart_item_img_slide{
			flex-direction: column;
		}
		.cart_item_image{
			width: 100%;
		}
		.cart_item_slide{
			flex-direction: row;
			width: 100%;
			align-items: inherit;
			padding-bottom: 0;
			padding-top: 20px;
		}
		.cart_item_slide_control{
			margin-bottom: 0;
			min-width: 45px;
			min-height: 55px;
			margin-right: 10px;
		}
		.cart_item_img{
			width: 45%;
			padding-right: 20px;
		}
		.cart_item_about{
			width: 55%;
			padding-left: 20px;
		}
	}
	@media(max-width: 1200px){
		.cart_item{
			flex-direction: column;
		}
		.cart_item_img{
			padding: 0;
			width:100%;
		}
		.cart_item_about{
			width:100%;
			padding: 0;
		}
		.cart_item_slide{
			padding-bottom: 20px;
			padding-top: 20px;
		}
		.cart_item_title{
			padding-bottom: 10px;
		}
		.cart_item_slide_control{
			min-width: 60px;
			min-height: 73px;
		}
		.buy_btn a{
			margin-top: 40px;
		}
	}
	@media(max-width:992px){
		.cart_item{
			padding:20px;
		}
		.cart_item_title{
			font-size:25px;
		}
		.cart_item_price{
			font-size: 30px;
		}
		.cart_item_about_text,.cart_item_condition,.edit_selections{
			font-size: 15px;
		}
		.buy_btn a{
			font-size:22px;
		}
	}
	@media(max-width: 768px){
		.cart_item{
			max-width: 600px;
			margin: 20px auto 20px auto;
		}
	}
	@media(max-width: 576px){
		.cart_item_delete{
			padding: 7px 10px;
			right: 0px;
			top: 0px;
		}
		.cart_item_delete a svg{
				width: 30px;
		}
	}
</style>