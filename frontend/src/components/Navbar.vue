<template>
	<nav>
		<section class="navbar_section">
			<div class="container_lg">
				<div class="navbar_fields">
					<div class="navbar_logo">
						<router-link to="/">
							<img src="@/assets/img/logo.png" alt="logo">
						</router-link>
					</div>
					<div class="navbar_list">
						<ul>
							<li @click="clickLi">
								<a>Futbolkalar</a>
							</li>
							<li @click="clickLi">
								<a>Hudilar</a>
							</li>
							<li @click="clickLi">
								<a>Krujkalar</a>
							</li>
							<li @click="clickLi">
								<a>Shaxsiy dizayn</a>
							</li>
							<li @click="clickLi">
								<a>Aloqa</a>
							</li>
							<li @click="clickLi" v-if="$store.getters.getLikedProducts.length">
								<router-link to="/products/liked" style="transform:translateY(10px);">
									<svg xmlns="http://www.w3.org/2000/svg" width="27"  fill="#000" viewBox="0 0 16 16">
										<path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
									</svg>
								</router-link>
							</li>
						</ul>
					</div>
					<div class="navbar_cart">
						<router-link to="/cart" class="navbar_cart_btn">
							<span>
								<svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-cart2" viewBox="0 0 16 16">
								    <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
								</svg>
							</span>
							<span class="cart_counter">
								{{getCartLength}}
							</span>
							<span>Savatcha</span>
						</router-link>
						<a class="navbar_control" @click="navbarControl">
							<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
							  <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5zm0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5z"/>
							</svg>
						</a>
					</div>
				</div>
			</div>
		</section>
	</nav>
</template>
<script>
import media from "@/assets/js/media.js"
import { mapGetters } from "vuex";

export default{
	name:"Navbar",
	data(){
		return {
			navbar: false
		}
	},
	methods:{
		clickLi(){
			let navbarList = document.querySelector(".navbar_list");
			this.navbar = !this.navbar
			navbarList.style = "" 
		},	
		navbarControl(){
			this.navbar = !this.navbar
			let navbar = this.navbar
			let navbarList = document.querySelector(".navbar_list");
			let navbar_ul = navbarList.querySelector("ul");
			media("max-width: 1200px", function(x){
				if (x){ 
			        if (!navbar) {
			        	navbarList.style.height = 0;        
			        }
			        if(navbar){
			          navbarList.style.height = navbar_ul.clientHeight + "px";    
			       	}
			    }
			    else{
			    	navbar = false
			    	navbarList.style = ""
			    } 
			})
		}
	},
	computed:{
		...mapGetters(['getCartLength'])
	}
}
</script>
<style>
	.navbar_section{
		background-color: #f8eeee;
	}
	.navbar_fields{
		display: flex;
		align-items: center;
		padding:10px 0px;
		font-family:poppins-bold;
		font-size:20px;
	}
	.navbar_logo,.navbar_list,.navbar_cart{
		width: auto;
	}
	.navbar_list{
		flex-grow: 1;
		text-align: center;
	}
	.navbar_list ul li{
		display: inline-block;
	}
	.navbar_logo a img{
		width: 140px;
	}
	.navbar_list ul li a{
		display: inline-block;
		padding:10px 25px;
	}
	.navbar_cart_btn{
		display: flex;
		background-color:#FFD600;
		padding:7px 35px 4px 35px;
		border-radius: 10px;
	}
	.navbar_cart_btn span svg{
		width:25px;
		transform:translateY(1px);
	}
	.cart_counter{
		font-size:14px;
		min-width: 18px;
		height: 18px;
		font-family: poppins;
		background-color:#DBDBDD;
		border-radius:50%;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 0px 5px;
		transform: translateX(-5px) translateY(-2px);
	}
	.navbar_control{
		display: none;
		padding:5px 10px;
	}
	.navbar_control svg{
		width:40px;
	}

	@media(max-width: 1300px){
	.navbar_list ul li a{
			padding:8px 20px;
		}
	}
	@media(max-width: 1200px){
		.navbar_fields{
			flex-wrap: wrap;
			justify-content: space-between;
		}
		.navbar_logo,.navbar_cart{
			width: auto;
		}
		.navbar_logo{
			order: 1;
		}
		.navbar_cart{
			order: 2;
			display: flex;
			align-items: center;
		}
		.navbar_list{
			min-width: 100%;
			text-align: left;
			order: 3;
			-moz-transition: height .5s;
            -ms-transition: height .5s;
            -o-transition: height .5s;
            -webkit-transition: height .5s;
            transition: height .5s;
            height: 0;
            overflow: hidden;
		}
		.navbar_control{
			display: inherit;
		}
		.navbar_list ul li{
			display: block;
		}
		.navbar_list ul li a {
			padding:10px 0px;
			width: 100%;
			border-radius: 10px;
			transition-property: background-color, padding;
			transition-duration: 0.5s;
			transition-timing-function: ease;
		}
		.navbar_list ul li a:hover{
			background-color:#F8E1E1;
			padding-left: 10px;
		}
	}
	@media(max-width: 576px){
		.navbar_section{
			overflow: hidden;
		}
		.navbar_cart_btn{
			position: fixed;
			right:-152px;
			top:49%;
			padding:12px 20px 10px 20px;
			transition-property: right;
			transition-duration: 0.8s;
			transition-timing-function: ease;
			border-top-right-radius: 0;
			border-bottom-right-radius: 0;
			z-index: 1;
		}
		.cart_counter{
			margin-right:40px;
			transition-property: margin-right;
			transition-duration: 0.8s;
			transition-timing-function: ease;
		}
		.navbar_cart_btn:hover{
			right: 0;
		}
		.navbar_cart_btn:hover .cart_counter{
			margin-right: 0;
		}
		.navbar_logo a img{
			width: 120px;
		}
		.navbar_cart_btn span svg{
			width:30px;
		}
		.cart_counter{
			min-width: 20px;
			height: 20px;
			font-size: 15px;
		}
		.navbar_cart_btn span:nth-child(3){
			transform: translateY(4px);
		}
	}
	@media(max-width: 320px){
		.navbar_logo a img{
			width: 100px;
		}
		.navbar_cart_btn span svg{
			width:25px;
		}
		.navbar_cart_btn span:nth-child(3){
			transform: translateY(0px);
		}
	}
</style>
