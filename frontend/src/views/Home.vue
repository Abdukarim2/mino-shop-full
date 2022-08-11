<template>
	<main>
		<!-- start Banner--->
		<Banner />
		<!-- start Services -->
		<Services />

		<!-- start Try content-->
		<Try />

		<!-- start Categories-->
		<Categories>
			<div class="view_title">
				<p>Kategoriyalar</p>
			</div>
		</Categories>

		<!-- start Products -->
		<Products :products="products.slice(0, 4)">
			<div class="view_title">
				<p>TOP tovarlar</p>
			</div>
		</Products>

		<!--- start Sorter ---->
		<Sorter :btn="true" :products="products">
			<!--:products="products"-->
			<div class="view_title">
				<p><span>Barcha</span> tovarlar</p>
			</div>
		</Sorter>

		<!-- start Top products -->
		<TopProducts :products="products.slice(4, 8)">
			<div class="view_title">
				<p>
					Eng ko’p sotilgan tovarlar
				</p>
			</div>
		</TopProducts>

		<!-- start Products -->
		<Products :products="productJacket">
			<div class="view_title">
				<p>Hudilar</p>
			</div>
		</Products>

		<!-- start Products -->
		<Products :products="productMug">
			<div class="view_title">
				<p>Krujkalar</p>
			</div>
		</Products>

		<!-- start Contact Form --->
		<ContactForm>
			<div class="view_title">
				<p>Aloqa</p>
			</div>
		</ContactForm>
	</main>
</template>
<script>
import Banner from "@/components/Banner.vue"
import Services from "@/components/Services.vue"
import Try from "@/components/Try.vue"
import Categories from "@/components/Categories.vue"
import Products from "@/components/Products.vue"
import Sorter from "@/components/Sorter.vue"
import TopProducts from "@/components/TopProducts.vue"
import ContactForm from "@/components/ContactForm.vue"
import axios from "axios"
export default {
	name: "Home",
	data() {
		return {
			products: [],
			productJacket: [],
			productMug: []
		}
	},
	components: {
		Banner,
		Services,
		Try,
		Categories,
		Products,
		Sorter,
		TopProducts,
		ContactForm
	},
	async beforeMount() {
		await axios.get("api/products/get/?limit=9&random=True")
			.then(response => {
				this.products = response.data
			})
		await axios.get("api/products/bycategory/hudilar/?limit=4&random=True")
			.then(response => {
				this.productJacket = response.data
			})
		await axios.get("api/products/bycategory/krujkalar/?limit=4&random=True")
			.then(response => {
				this.productMug = response.data
			})
	}
}
</script>
<style>
.view_title {
	font-family: poppins-bolder;
	font-size: 35px;
	margin: 30px 0px 20px 0px;
	color: #000;
}

.view_title span {
	color: #CA8970;
}

@media(max-width: 576px) {
	.view_title {
		font-size: 30px;
		text-align: center;
	}
}
</style>