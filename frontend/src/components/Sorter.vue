<template>
	<section class="sorter_section">
		<div class="container_lg" id="products">
			<slot></slot>
			<div class="filter_btn" @click="filterBar = !filterBar">
				<img src="@/assets/img/filter.svg">
			</div>
			<div class="sorter_blocks">
				<div class="sorted_products">
					<TransitionGroup name="filter">
						<div class="srted_product" v-for="product in filterProduct" :key="product.id">
							<Product :product="product">
								<router-link :to="'/products/detail/' + product.slug + '/' + product.id + '#product'">
									<img :src="Array(product.get_img_url)[0]" :alt="product.name">
								</router-link>
								<p>
									<span>{{ product.priceDolor }}</span> - {{ product.price }} uzs
								</p>
							</Product>
						</div>
					</TransitionGroup>
				</div>
				<div class="sorter_block" ref="sorterBlock">
					<div class="sorter_items">
						<div class="filter_btn_back" @click="filterBar = !filterBar">
							<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-backspace-reverse"
								viewBox="0 0 16 16">
								<path
									d="M9.854 5.146a.5.5 0 0 1 0 .708L7.707 8l2.147 2.146a.5.5 0 0 1-.708.708L7 8.707l-2.146 2.147a.5.5 0 0 1-.708-.708L6.293 8 4.146 5.854a.5.5 0 1 1 .708-.708L7 7.293l2.146-2.147a.5.5 0 0 1 .708 0z" />
								<path
									d="M2 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h7.08a2 2 0 0 0 1.519-.698l4.843-5.651a1 1 0 0 0 0-1.302L10.6 1.7A2 2 0 0 0 9.08 1H2zm7.08 1a1 1 0 0 1 .76.35L14.682 8l-4.844 5.65a1 1 0 0 1-.759.35H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1h7.08z" />
							</svg>
						</div>
						<div class="sorter_title">
							<p>Kategoriyalar</p>
						</div>
						<div class="sorter_accordion">
							<ul>
								<li v-for="category in uniqueId">
									<a class="accordions" @click="filterByCategory(category)">
										<span>
											<img src="@/assets/img/accordion.svg">
										</span>
										<span>{{categoryList[category-1]}}</span>
									</a>
								</li>
							</ul>
						</div>
						<div class="sorter_selections">
							<ul>
								<li>
									<a class="accordion_select">
										<span>Material</span>
										<span>
											<svg xmlns="http://www.w3.org/2000/svg" width="17" height="10"
												viewBox="0 0 17 10" fill="none">
												<path
													d="M15.3084 9L9.53824 2.48C8.85679 1.71 7.74169 1.71 7.06024 2.48L1.29004 9"
													stroke="#292D32" stroke-width="2" stroke-miterlimit="10"
													stroke-linecap="round" stroke-linejoin="round" />
											</svg>
										</span>
										<span class="line_hover"></span>
									</a>
									<div class="selection_items">
										<div class="selection_dropdown">
											<div class="dropdown_text">
												<p v-for="material in materialsId">
													<label class="switch">
														<input type="checkbox" :id="`item${material}`" @change="filterByMaterial(material)">
														<span class="slider round"></span>
													</label>
													<label :for="`item${material}`" style="display: inline-block; 
																			transform: translate(10px, -3px);
																			cursor: pointer;">
														{{materials[material-1]}}
													</label>
												</p>
											</div>
										</div>
									</div>
								</li>
								<li>
									<a class="accordion_select">
										<span>Narxi</span>
										<span>
											<svg xmlns="http://www.w3.org/2000/svg" width="17" height="10"
												viewBox="0 0 17 10" fill="none">
												<path
													d="M15.3084 9L9.53824 2.48C8.85679 1.71 7.74169 1.71 7.06024 2.48L1.29004 9"
													stroke="#292D32" stroke-width="2" stroke-miterlimit="10"
													stroke-linecap="round" stroke-linejoin="round" />
											</svg>
										</span>
										<span class="line_hover"></span>
									</a>
									<div class="selection_items">
										<div class="selection_dropdown">
											<div class="dropdown_text">
												<p>
													{{ toHtml[0] }} - {{ toHtml[1] }}
												</p>
												<p style="padding:8px 10px;">
													<Slider v-model="rangeValue" :tooltips="false" :min="10000"
														:max="200000" :step="1000" />
												</p>
											</div>
										</div>
									</div>
								</li>
								<li>
									<a class="accordion_select">
										<span>Rang</span>
										<span>
											<svg xmlns="http://www.w3.org/2000/svg" width="17" height="10"
												viewBox="0 0 17 10" fill="none">
												<path
													d="M15.3084 9L9.53824 2.48C8.85679 1.71 7.74169 1.71 7.06024 2.48L1.29004 9"
													stroke="#292D32" stroke-width="2" stroke-miterlimit="10"
													stroke-linecap="round" stroke-linejoin="round" />
											</svg>
										</span>
										<span class="line_hover"></span>
									</a>
									<div class="selection_items">
										<div class="selection_dropdown">
											<div class="dropdown_text">
												<p style="display:flex; flex-wrap: wrap;">
													<span class="color_blocks" v-for="color in colors">
														<span :style="`background-color:${color};`" 
																@click="filterByColor(color)"></span>
													</span>
												</p>
											</div>
										</div>
									</div>
								</li>
							</ul>
						</div>
						<div class="sorter_back_all">
							<a @click="backAll">
								Hammasini qaytarish
							</a>
						</div>
					</div>
					<slot name="social"></slot>
				</div>
			</div>
			<div class="show_all" v-if="btn">
				<router-link to="/products/all/">
					Hammasini ko’rish
				</router-link>
			</div>
		</div>
		<div class="curtain" ref="curtain"></div>
	</section>
</template>
<script>
import Product from "@/components/GlobalUI/Product.vue"
import Slider from '@vueform/slider'
export default {
	name: "Sorter",
	components: {
		Product,
		Slider,
	},
	data() {
		return {
			rangeValue: [35000, 175000],
			toHtml: ['25.000', '75.000'],
			filterBar: false,
			filterProduct: [],
			categoriesId:[],
			uniqueId:[],
			categoryList:['Sovg\'alar', 'Beyzbolkalar', 'Krujkalar', 'Hudilar', 'Futbolkalar'],
			materialsId:[],
			materials:['Paxta', 'Sintetika', 'Boshqa'],
			colors:[]
		}
	},
	props: {
		btn: {
			type: Boolean,
			default: true
		},
		products: {
			type: Array,
		}
	},
	watch: {
		products(val) {
			this.filterProduct = val
			for(let i of val){
				this.categoriesId.push(i.category)
				for (let z of i.material){
					if(!this.materialsId.includes(z)){
						this.materialsId.push(z)
					}
				}
				for(let c of i.get_colors){
					if(!this.colors.includes(c)){
						this.colors.push(c)
					}
				}
			}
			this.uniqueId = new Set(this.categoriesId)
		},
		rangeValue(val) {
			let toString1 = String(val[0]).replace('000', '')
			let toString2 = String(val[1]).replace('000', '')
			this.toHtml[0] = toString1 + ".000"
			this.toHtml[1] = toString2 + ".000"
			this.filterProduct = this.products.filter(e => e.price >= val[0] && e.price <= val[1] )
			if(!this.btn){
				this.$router.push({hash:"#products"})
			}
		},
		filterBar(bool) {
			let curtain = this.$refs.curtain;
			let sorterBlock = this.$refs.sorterBlock;
			if (bool) {
				curtain.classList.add("clsfor_curtain")
				sorterBlock.classList.add("clsfor_filterbar")
			}
			else {
				setTimeout(function () {
					curtain.className = "curtain"
				}, 400)
				sorterBlock.className = "sorter_block"
			}
		},
	},
	beforeMount() {
		this.filterProduct = this.products
		for(let i of this.products){
			this.categoriesId.push(i.category)
			for (let z of i.material){
				if(!this.materialsId.includes(z)){
					this.materialsId.push(z)
				}
			}
			for(let c of i.get_colors){
				if(!this.colors.includes(c)){
					this.colors.push(c)
				}
			}
		}
		this.uniqueId = new Set(this.categoriesId)
	},
	mounted() {
		let accordionsSelect = document.querySelectorAll(".accordion_select")
		accordionsSelect.forEach(function (el) {
			el.addEventListener("click", function () {
				let accordionsSelectBlock = el.nextElementSibling;
				let accordionsSelectItems = accordionsSelectBlock.querySelector(".selection_dropdown");
				if (accordionsSelectBlock.style.height) {
					accordionsSelectBlock.style.height = null;
					el.querySelectorAll("span")[1].querySelector("svg").style = "transform:rotate(180deg);"
				}
				else {
					accordionsSelectBlock.style.height = accordionsSelectItems.clientHeight + "px"
					el.querySelectorAll("span")[1].querySelector("svg").style = "transform:rotate(0deg);"
				}
			})
		})
	},
	methods: {
		filterByCategory(id) {
			this.filterProduct = this.products.filter(e => e.category == id)
			if(!this.btn){
				this.$router.push({hash:"#products"})
			}
		},
		filterByMaterial(val){
			if(event.target.checked){
				this.filterProduct = this.products.filter( e => e.material.includes(val))
			}
			else{
				this.filterProduct = this.products
			}
			if(!this.btn){
				this.$router.push({hash:"#products"})
			}
		},
		filterByColor(color){
			this.filterProduct = this.products.filter( e => e.get_colors.includes(color))
			if(!this.btn){
				this.$router.push({hash:"#products"})
			}
		},
		backAll(){
			this.filterProduct = this.products
		}
	}
}
</script>

<style>
@import "@vueform/slider/themes/default.css";
</style>

<style>
.filter-enter-active,
.filter-leave-active {
  transition: all 0.5s ease;
}

.filter-leave-to {
  order: 1;
  opacity: 0;
  transform: scale(0.5);
}

.sorter_section {
	margin-bottom: 40px;
}

.sorter_blocks {
	display: flex;
}

.sorted_products {
	width: calc(100% - 380px);
	display: flex;
	flex-wrap: wrap;
}

.sorter_block {
	top: 0;
	position: sticky;
	height: 100%;
	width: 380px;
	padding: 10px;
}

.srted_product {
	padding: 10px;
	max-width: 33.33333%;
}

.sorter_items {
	background-color: #fff;
	border-radius: 10px;
	box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
	padding: 10px 17px;
}

.sorter_title {
	font-family: poppins-bolder;
	font-size: 26px;
}

.sorter_accordion {
	margin: 15px 0px;
	font-family: poppins-bold;
	font-size: 22px;
}

.sorter_accordion ul li {
	border-radius: 10px;
	transition-property: background-color, padding-left;
	transition-duration: 0.2s;
	transition-timing-function: ease-in;
}

.sorter_accordion ul li:hover {
	padding-left: 10px;
	background-color: #f8eeee;
}

.sorter_accordion ul li a {
	display: block;
	padding: 4px 0px;
}

.sorter_accordion ul li a span:first-child {
	margin-right: 10px;
}

.sorter_selections {
	font-family: poppins;
	font-size: 25px;
}

.sorter_selections ul li a {
	display: flex;
	justify-content: space-between;
	align-items: center;
	position: relative;
	padding: 3px 0px;
}

.sorter_selections ul li a span:nth-child(2) svg {
	transition-property: transform;
	transition-duration: 0.5s;
	transition-timing-function: ease;
	transform: rotate(180deg);
}

.line_hover {
	position: absolute;
	bottom: 0px;
	width: 0%;
	border-bottom: 2px solid red;
	transition-property: width;
	transition-duration: 0.8s;
	transition-timing-function: ease;
}

.sorter_selections ul li a:hover .line_hover {
	width: 100%;
}

.sorter_back_all {
	margin: 20px 0px 10px 0px;
}

.sorter_back_all a {
	display: block;
	width: 90%;
	margin: auto;
	padding: 10px 0px;
	border-radius: 10px;
	background-color: #FFD600;
	font-family: poppins-bold;
	text-align: center;
	font-size: 19px;
}


.selection_items {
	font-size: 20px;
	-moz-transition: height .5s;
	-ms-transition: height .5s;
	-o-transition: height .5s;
	-webkit-transition: height .5s;
	transition: height .5s;
	height: 0;
	overflow: hidden;
}

.selection_dropdown {
	padding: 10px 0px 5px 0px;
}

.dropdown_text {
	opacity: 0.7;
}

.dropdown_text p {
	padding: 5px 0px;
}

.switch {
	position: relative;
	display: inline-block;
	width: 45px;
	height: 25px;
}

.switch input {
	opacity: 0;
	width: 0;
	height: 0;
}

.slider {
	position: absolute;
	cursor: pointer;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: #ccc;
	-webkit-transition: .4s;
	transition: .4s;
}

.slider:before {
	position: absolute;
	content: "";
	height: 20px;
	width: 20px;
	left: 2px;
	top: 2.5px;
	background-color: white;
	-webkit-transition: .4s;
	transition: .4s;
}

.slider.round {
	border-radius: 34px;
}

.slider.round:before {
	border-radius: 50%;
}

.dropdown_text input[type="checkbox"]:checked+.slider {
	background-color: #2196F3;
}

.dropdown_text input[type="checkbox"]:focus+.slider {
	box-shadow: 0 0 1px #2196F3;
}

.dropdown_text input[type="checkbox"]:checked+.slider:before {
	-webkit-transform: translateX(20px);
	-ms-transform: translateX(20px);
	transform: translateX(20px);
}

.color_blocks {
	padding: 1px 5px;
}

.color_blocks span {
	border: 1px solid black;
	display: inline-block;
	width: 35px;
	height: 35px;
	background-color: red;
	cursor: pointer;
	box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.15);
}

.filter_btn {
	display: none;
	float: right;
	width: 50px;
	height: 50px;
	margin-bottom: 20px;
	padding: 7px 5px 5px 5px;
	cursor: pointer;
}

.filter_btn svg {
	width: 100%;
}

.clsfor_curtain {
	display: block !important;
}

.clsfor_filterbar {
	right: 0px !important;
}

.filter_btn_back svg {
	width: 25px;
}

.filter_btn_back {
	display: none;
	position: absolute;
	right: 15px;
	top: 10px;
	width: 40px;
	height: 40px;
	align-items: center;
	justify-content: center;
	cursor: pointer;
}

.show_all {
	text-align: center;
}

.show_all a {
	display: inline-block;
	text-align: center;
	padding: 10px 0px;
	width: 350px;
	font-family: poppins-bolder;
	border-radius: 10px;
	background-color: #FFD600;
	margin: 30px auto 0px auto;
	font-size: 20px;
}

/* media */
@media(max-width: 1400px) {
	.srted_product {
		max-width: 50%;
	}
}

@media(max-width: 992px) {
	.sorter_blocks {
		flex-direction: column-reverse;
	}

	.srted_product {
		max-width: 50%;
	}

	.sorted_products {
		width: 100%;
		flex-wrap: wrap;
	}

	.sorter_block {
		position: fixed;
		z-index: 2;
		right: -400px;
		top: 0;
		width: 400px;
		height: 100%;
		overflow-y: scroll;
		z-index: 2;
		transition: right 0.5s ease;
	}

	.sorter_block::-webkit-scrollbar {
		display: none;
	}

	.sorter_items {
		min-height: 100%;
		position: relative;
	}

	.curtain {
		z-index: 1;
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		display: none;
		background-color: rgba(0, 0, 0, 0.3);
		-webkit-backdrop-filter: blur(10px);
		backdrop-filter: blur(10px);
	}

	.filter_btn {
		display: inline-block;
	}

	.filter_btn_back {
		display: flex;
	}
}

@media(max-width: 576px) {
	.sorted_products {
		justify-content: center;
	}

	.srted_product {
		max-width: 500px;
	}

	.sorter_block {
		width: 370px;
	}

	.show_all a {
		width: 300px;
		max-width: 300px;
		font-size: 19px;
	}
}

@media(max-width: 400px) {
	.filter_btn {
		width: 45px;
		height: 45px;
	}

	.sorter_block {
		width: 100%;
	}

	.show_all a {
		width: 100%;
		max-width: 100%;
	}
}
</style>