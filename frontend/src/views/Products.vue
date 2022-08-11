<template>
	<main>
		<!--- start Products ---->
		<Sorter :btn="false" :products="products" v-if="getBy == 'all'">
			<div class="view_title">
				<p><span>Barcha</span> tovarlar</p>
			</div>
			<template v-slot:social>
				<SocialMedias />
			</template>
		</Sorter>
		<ProductsWell :products="products" v-else>
			<div class="view_title">
				<p>Barch <span>{{ getBy }}</span></p>
			</div>
		</ProductsWell>
		<div class="container_lg" v-if="getBy == 'all'">
			<div class="loader_container">
				<div class="loader">
					<div ref="observer" class="lds-ellipsis">
						<div></div>
						<div></div>
						<div></div>
						<div></div>
					</div>
				</div>
			</div>
		</div>
	</main>
</template>
<script>
import Sorter from "@/components/Sorter.vue"
import SocialMedias from "@/components/GlobalUI/SocialMedias.vue"
import ProductsWell from "@/components/Products.vue"
import axios from "axios"
export default {
	name: "Products",
	data() {
		return {
			products: [],
			limit: 6,
			getBy: null,
		}
	},
	components: {
		Sorter,
		SocialMedias,
		ProductsWell
	},
	created() {
		this.getBy = this.$route.params.by
	},
	beforeMount() {
		if (this.getBy) {

			if (this.getBy == "all") {
				this.getProducts()
			}
			else {
				this.getProductsByCategory(this.getBy)
			}

		}
	},
	mounted() {
		if (this.getBy) {
			if (this.getBy == "all") {
				new IntersectionObserver((entries, observer) => {
					if (entries[0].isIntersecting) {
						this.limit += 2
						this.getProducts()
					}
				}, { rootMargin: '0px', threshold: 1.0 }).observe(this.$refs.observer)
			}
		}
	},
	methods: {
		async getProducts() {
			await axios.get(`api/products/get/?limit=${this.limit}`)
				.then(response => {
					this.products = response.data
				})
		},
		async getProductsByCategory(slug) {
			await axios.get(`api/products/bycategory/${slug}/`)
				.then(response => {
					this.products = response.data
				})
		}
	}
}
</script>
<style>
.loader_container {
	width: calc(100% - 380px);
}

.loader {
	background-color: #FFD600;
	display: flex;
	width: 300px;
	height: 60px;
	justify-content: center;
	align-items: center;
	border-radius: 10px;
	margin: 0px auto 40px auto;
}

.lds-ellipsis {
	display: inline-block;
	position: relative;
	width: 75px;
	height: 15px;
}

.lds-ellipsis div {
	position: absolute;
	top: 0px;
	width: 13px;
	height: 13px;
	border-radius: 50%;
	background: #fff;
	animation-timing-function: cubic-bezier(0, 1, 1, 0);
}

.lds-ellipsis div:nth-child(1) {
	left: 8px;
	animation: lds-ellipsis1 0.6s infinite;
}

.lds-ellipsis div:nth-child(2) {
	left: 8px;
	animation: lds-ellipsis2 0.6s infinite;
}

.lds-ellipsis div:nth-child(3) {
	left: 32px;
	animation: lds-ellipsis2 0.6s infinite;
}

.lds-ellipsis div:nth-child(4) {
	left: 56px;
	animation: lds-ellipsis3 0.6s infinite;
}

@keyframes lds-ellipsis1 {
	0% {
		transform: scale(0);
	}

	100% {
		transform: scale(1);
	}
}

@keyframes lds-ellipsis3 {
	0% {
		transform: scale(1);
	}

	100% {
		transform: scale(0);
	}
}

@keyframes lds-ellipsis2 {
	0% {
		transform: translate(0, 0);
	}

	100% {
		transform: translate(24px, 0);
	}
}

@media(max-width: 992px) {
	.loader_container {
		width: 100%;
	}
}

@media(max-width: 576px) {
	.loader_container {
		padding: 0px 10px 0px 10px;
	}

	.loader {
		width: auto;
		max-width: 300px;
		height: 55px;
	}
}
</style>