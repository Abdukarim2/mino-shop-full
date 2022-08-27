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
						<transition-group name="slide-fade" tag="div">
							<CartItem v-if="getAllProducts.length" v-for="(product, index) in getAllProducts" 
								@deleteCartItem="removeCartItem(index)" 
								:key="product.id" :product="product" :index="index"/>
							<h1 v-else style="text-align:center;
										font-family:poppins-bolder; padding: 50px 0px;">
								Sizning savatchangiz bo'sh
							</h1>
						</transition-group>
					</div>
					<div class="cart_page_right_bar">
						<OrderTotal>
							<ul>
								<li>Tovarlar soni : {{getAllProducts.length}} ta </li>
								<li>Umumiy summa : ${{Math.ceil(getTotalPrice[0] * Math.pow(10, 2)) / Math.pow(10, 2)}} - {{getTotalPrice[1]}} uzs</li>
								<li>Yetkazib berish : Bepul</li>
								<li>Chegirma bilan : {{getTotalPrice[1]}} uzs</li>
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
import { mapGetters, mapMutations } from "vuex"

export default {
	name: "Cart",
	data(){
		return {
			sumUZS:0,
			sumUSD:0
		}
	},
	components: {
		Deliver,
		OrderTotal,
		CartItem,
		SocialMedias,
		PayType
	},
	methods: {
		...mapMutations(['REMOVE_ITEM']),
		removeCartItem(index) {
			this.REMOVE_ITEM(index)
		}
	},
	computed: {
		...mapGetters(['getAllProducts']),
		...mapGetters(['getTotalPrice'])
	}
}
</script>
<style>
.cart_right_bar {
	display: flex;
	position: relative;
}

.cart_items {
	width: calc(100% - 380px);
	padding-right: 50px;
}

.cart_page_right_bar {
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

/* start vue transition */
.slide-fade-enter-active {
	transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
	transition: all 0.5s;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
	transform: translateX(50px);
	opacity: 0;
}

/* end vue transition */

@media(max-width: 1400px) {
	.cart_items {
		padding-right: 20px;
	}
}

@media(max-width: 992px) {
	.cart_items {
		width: calc(100% - 330px);
	}

	.cart_page_right_bar {
		max-width: 330px;
	}
}

@media(max-width: 768px) {
	.cart_right_bar {
		flex-direction: column-reverse;
	}

	.cart_items {
		width: 100%;
		padding-right: 0px;
	}

	.cart_page_right_bar {
		max-width: 600px;
		height: auto;
		position: inherit;
		margin: auto;
	}

	.social_medias_cart_page {
		display: none;
	}
}
</style>