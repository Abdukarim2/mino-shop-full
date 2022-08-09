<template>
  <main>
  	<!-- start Cart Items -->
  	<section class="section_cart_items">
  	  <div class="container_lg">
  	  	<div class="view_title">
			  	<p>Savatcha</p>
		    </div>
	    <div class="cart_right_bar">
	      <div class="cart_items">
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
					<CartItem @deleteCartItem="removeCartItem" />
	      </div>
	      <div class="cart_page_right_bar">
					<OrderTotal>
					  <ul>
					  	<li>Tovarlar soni : 2 ta </li>
					  	<li>Umumiy summa : $15 - 162.000 uzs</li>
					  	<li>Yetkazib berish : Bepul</li>
					  	<li>Chegirma bilan : 155.000 uzs</li>
					  </ul>
					</OrderTotal>
					<PayType></PayType>
					<SocialMedias class="social_medias_cart_page"></SocialMedias>
	      </div>
	    </div>
  	  </div>
  	</section>
 		<!-- start Deliver services -->
    <Deliver style="padding-bottom: 50px;">
  	  <div class="view_title">
			  <p>Tez va bepul yetkazib berish</p>
		  </div>
    </Deliver>	
  </main>
</template>
<script>
import Deliver from "@/components/GlobalUI/Deliver.vue"
import OrderTotal from "@/components/GlobalUI/OrderTotal.vue"
import CartItem from "@/components/GlobalUI/CartItem.vue"
import PayType from "@/components/GlobalUI/PayType.vue"
import SocialMedias from "@/components/GlobalUI/SocialMedias.vue"
export default{
	name:"Cart",
	components:{
		Deliver,
		OrderTotal,
		CartItem,
		SocialMedias,
		PayType
	},
	methods:{
		removeCartItem(){
			/**/
		}
	}
}
</script>
<style>
  .cart_right_bar{
  	display: flex;	
  	position: relative;
  }
  .cart_items{
  	width: calc(100% - 380px);
  	padding-right: 50px;
  }
  .cart_page_right_bar{
  	max-width: 380px;
  	position: sticky;
  	top: 0;
  	height: 100%;
  }
  .cart-enter-active,
	.cart-leave-active {
	  transition: all 0.5s ease;
	}
	.cart-enter-from,
	.cart-leave-to {
	  opacity: 0;
	  transform: translateX(30px);
	}
  @media(max-width: 1400px){
  	.cart_items{
	  	padding-right: 20px;
	  }
  }
  @media(max-width: 992px){
  	.cart_items{
	  	width: calc(100% - 330px);
	  }
	  .cart_page_right_bar{
	  	max-width: 330px;
	  }
  }
  @media(max-width: 768px){
  	.cart_right_bar{
  		flex-direction: column-reverse;
  	}
  	.cart_items{
	  	width: 100%;
	  	padding-right: 0px;
	  }
	  .cart_page_right_bar{
	  	max-width: 600px;
	  	height: auto;
	  	position: inherit;
	  	margin: auto;
	  }
	  .social_medias_cart_page{
	  	display: none;
	  }
  }
</style>