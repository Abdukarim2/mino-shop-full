<template>
	<section class="products_section">
		<div class="container_lg">
			<slot></slot>
			<div class="products_blocks">
				<transition-group name="liked" >
					<div class="product_block" v-for="product in products" :key="product.id">
						<Product :product="product" :liked="liked" >
							<router-link :to="'/products/detail/' + product.slug + '/' + product.id + '#product'">
								<img :src="product.get_img_url[0]" :alt="product.name">
							</router-link>
							<p>
								<span>{{ product.priceDolor }} $</span> - {{ product.price }} uzs
							</p>
						</Product>
					</div>
				</transition-group>
			</div>
		</div>
	</section>
</template>
<script>
import Product from "@/components/GlobalUI/Product.vue"
import axios from "axios"
export default {
	name: "Products",
	components: {
		Product,
	},
	props: {
		products: {
			type: Array,
		},
		liked: Boolean
	}
}
</script>
<style>
.products_section {
	margin-top: 40px;
	margin-bottom: 30px;
}

.products_blocks {
	display: flex;
	flex-wrap: wrap;
}

.product_block {
	padding: 10px;
	max-width: 25%;
}

.liked-enter-active,
.liked-leave-active{
	transition: all 0.8s;
}

.liked-enter-from{
	transform: translateY(0px);
	opacity: 1;
}
.liked-leave-to{
	transform: translateY(-10%);
	opacity: 0;
}

@media(max-width: 1200px) {
	.products_blocks {
		flex-wrap: wrap;
	}

	.product_block {
		max-width: 50%;
		padding: 10px;
	}
}

@media(max-width: 576px) {
	.products_blocks {
		justify-content: center;
	}

	.product_block {
		max-width: 500px;
		padding: 10px;
	}
}
</style>
