<template>
 <main>
   <section class="design_page_section">
     <Categories class="design_categories">
	   <div class="view_title">
		 <p>Kategoriyalar</p>
	   </div>
	 </Categories>
	 <div class="container_lg">
	   <div class="design_blocks">
	   	<div class="design_block">
	   	  <div class="design_block_items">
	   	  	<div class="design_image">
	   	  	  <div class="image_change_color" :style="'background-color:'+design.tShrtColor+';'" ref="toImg">
	   	  	  	<div class="writer_text" >
	   	  	  		<div :style="`width: 100%; height: 100%; 
	   	  	  								position: relative;
	   	  	  								display: flex;
												  	justify-content: center;
												  	align-items: center;`"
												  	@mousemove="clientMousemove($event)"
												  	@touchmove="clientMousemove($event)"
												  	@mouseleave="activate = false"
												  	@touchcanel="activate = false"
												  	class="moverBlock">
	   	  	  			<p class="design_text" 
	   	  	  			:style="'font-size:'+design.textSize+'px;'+
	   	  	  			'color:'+design.textColor+';'+
	   	  	  			'font-family:'+design.fontFamily+';' "

	   	  	  			@mousedown="clientMousedown($event)"
	   	  	  			@touchstart="clientMousedown($event)"
	   	  	  			@mouseup="clientMouseup($event)"
	   	  	  			@touchend="clientMouseup($event)"
	   	  	  			ref="textMover">
	   	  	  				{{design.text}}
	   	  	  			</p>
	   	  	  	  </div>	
	   	  	  	</div>
	   	  	  	<a>
		   	  	  	<img src="@/assets/img/t-shirt2.png" class="assets">
		   	  	  </a>
	   	  	  </div>
	   	  	</div>
	   	  	<div class="design_tools">
	   	  	  <div class="color_changer design_tools_blocks">
	   	  	  	<p class="tool_title">Rangi</p>
	   	  	  	<div class="selection_blocks">
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#fff'"></div>
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#000'"></div>
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#CA8970'"></div>
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#FFD600'"></div>
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#DBDBDD'"></div>
	   	  	  		<div class="selection_block" @click="design.tShrtColor = '#7C18FB'"></div>
	   	  	  	</div>
	   	  	  </div>
	   	  	  <div class="size_changer design_tools_blocks">
	   	  	  	<p class="tool_title">Hajmi</p>
	   	  	  	<div class="selection_blocks">
	   	  	  		<div class="selection_block">
	   	  	  			<p>L</p>
	   	  	  		</div>
	   	  	  		<div class="selection_block">
	   	  	  			<p>M</p>
	   	  	  		</div>
	   	  	  		<div class="selection_block">
	   	  	  			<p>X</p>
	   	  	  		</div>
	   	  	  		<div class="selection_block">
	   	  	  			<p>XL</p>
	   	  	  		</div>
	   	  	  		<div class="selection_block">
	   	  	  			<p>XXL</p>
	   	  	  		</div>
	   	  	  	</div>
	   	  	  </div>
	   	  	  <div class="material design_tools_blocks">
	   	  	  	<p class="tool_title">Material</p>
	   	  	  	<select class="tool_selections">
		   	  	  		<option>paxta</option>
		   	  	  		<option>paxta</option>
		   	  	  		<option>paxta</option>
		   	  	  </select>
	   	  	  </div>
						<MinoInput style="margin-top: 15px;">
							<p class="tool_title" style="margin-bottom: 5px;">Matn Rangi</p>
							<input type="color" placeholder="Matn rangi" v-model="design.textColor"
      	       style="height: 30px;">  
						</MinoInput>
						<MinoInput style="margin-top: 25px;">
							<p class="tool_title" style="margin-bottom: 5px;">Matn Fo'nti</p>
							<select v-model="design.fontFamily">
								<option selected value="poppins">Font1</option>
								<option value="poppins-bold">Font2</option>
								<option value="poppins-bolder">Font3</option>
								<option value="sans">Font4</option>
								<option value="sans-serif">Font5</option>
								<option value="verdana">Font6</option>
								<option value="tahoma">Font7</option>
								<option value="cursive">Font8</option>
								<option value="monospace">Font9</option>
								<option value="fantasy">Font10</option>
								<option value="arial">Font11</option>
								<option value="helvetica">Font12</option>
								<option value="trebuchet MS">Font13</option>
								<option value="times new roman">Font14</option>
								<option value="georgia">Font15</option>
								<option value="garamond">Font16</option>
								<option value="courier New">Font17</option>
								<option value="brush script MT">Font18</option>
							</select>
						</MinoInput>
	   	  	</div>
	   	  </div>
	   	</div>
	   	<div class="design_right_bar">
	   	  <div class="writer_block">
	   	  	<p>Shaxsiy matningizni kiriting</p>
	   	  	<MinoInput>
      	     <input type="text" placeholder="Matn..." v-model="design.text">     	    	
      	     <input type="text" placeholder="Matn kattaligi" v-model="design.textSize"
      	      style="margin-top:10px;">     	      	   
					</MinoInput>
					<div class="design_page_buy_btn">
				      <a @click="createDesign">
				      	$ Sotib olish
				      </a>
					</div>
	   		</div>
	   	  <PayType  class="design_page_pay"></PayType>
		  	<SocialMedias class="social_medias_cart_page"></SocialMedias>
	   	</div>
	   </div>
	 </div>
	 <Services class="design_page_services"></Services>
   </section>
 </main>
</template>
<script>
import Categories from "@/components/Categories.vue"
import Services from "@/components/Services.vue"
import PayType from "@/components/GlobalUI/PayType.vue"
import SocialMedias from "@/components/GlobalUI/SocialMedias.vue"
import DomToImg from "@/assets/js/dom-to-img.js"
export default{
	name:"Design",
	data(){
		return {
			design:{
				text:"Matn...",
				textSize:20,
				fontFamily:"cursive",
				textColor:"#000",
				tShrtColor:"#fff",
			},
			activate:false,
			elementTop:0,
			elementLeft:0,
			elementinLeft:0,
			elementinTop:0,
			isMobile:false
		}
	},
	components:{
		Categories,
		Services,
		PayType,
		SocialMedias
	},
	mounted(){
			this.elementTop = document.querySelector(".moverBlock").getBoundingClientRect().top;
			this.elementLeft = document.querySelector(".moverBlock").getBoundingClientRect().left;
			window.addEventListener("scroll", ()=>{
				if(document.querySelector(".moverBlock")){
					this.elementTop = document.querySelector(".moverBlock").getBoundingClientRect().top;
				}
			})
			window.addEventListener("resize", ()=>{
				if(document.querySelector(".moverBlock")){
					this.elementLeft = document.querySelector(".moverBlock").getBoundingClientRect().left;
				}
			})
	},
	watch:{
		activate(val){
			if(val && this.isMobile){
				document.body.style.overflow = "hidden"
			}
			else{
				document.body.style.overflow = "inherit"
			}
		}
	},
	methods:{
		clientMousedown(event){
			if(!event.changedTouches){
				this.isMobile = false
				this.activate = true
				this.elementinTop = event.offsetY
				this.elementinLeft = event.offsetX
			}
			if(event.changedTouches){
				this.isMobile = true
				this.activate = true

				/* hisoblagan bu yerga*/
				this.elementinTop = event.touches[0].offsetY
				this.elementinLeft = event.touches[0].offsetX
			}
		},
		clientMouseup(){
			this.activate = false
		},
		clientMousemove(event){
			let element = this.$refs.textMover;
				if(this.activate && !event.changedTouches){
						this.isMobile = false
						element.style.position = "absolute"
						element.style.top = event.clientY - this.elementTop - this.elementinTop + "px"
						element.style.left = event.clientX - this.elementLeft - this.elementinLeft + "px"
						
				}	
				if(this.activate && event.changedTouches){
					this.isMobile = true
					element.style.position = "absolute"
					element.style.top = event.touches[0].clientY - this.elementTop - 15  + "px"
					element.style.left = event.touches[0].clientX - this.elementLeft  - 30 + "px"
				}
		},
		createDesign(){
			  DomToImg.toPng(this.$refs.toImg)
				.then(function (dataUrl) {
					    fetch(dataUrl)
					    .then(res => res.blob())
					    .then(blob => {
					    	window.location.href = URL.createObjectURL(blob)
					    })
					})
				.catch(function (error) {
					    console.error('oops, something went wrong!', error);
			});
		}
	}
}
</script>
<style>
  .design_categories{
  	padding-left: 0;
  }
  .design_categories .categories_blocks{
  	padding-left: 0;
  }
  .design_categories .categories_blocks .category_block:first-child{
  	padding-left: 0;
  }
  .design_categories .categories_blocks .category_block:nth-child(4),
  .design_categories .categories_blocks .category_block:nth-child(5){
  	visibility: hidden;
  }
  .design_blocks{
  	padding-bottom: 20px;
  }
  .design_blocks{
  	display: flex;
  }

  .design_block{
  	max-width: calc(100% - 400px);
  	padding-right: 30px;
  }
  .design_right_bar{
  	max-width: 400px;
  	position: sticky;
  	top: 0;
  	height: 100%;
  }
  .design_block_items{
	  background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding: 15px 20px;
		display: flex;
  }
  .design_image{
  	position: relative;
  	width: 65.5%;
  }
  .design_image a img{
  	width: 100%;
  }
  .design_tools{
  	width: 34.5%;
  	padding: 0px 2%;
  }
  .design_tools{
  	font-size: 26px;
  	font-family: poppins;
  }
  .tool_selections{
  	border: none;
  	font-size: 24px;
  	font-family: poppins;	
  }
  .selection_blocks{
  	display: flex;
  	flex-wrap: wrap;
  }
  .selection_blocks .selection_block{
  	width: 45px;
  	height: 45px;
  	margin:15px 15px 0px 0px;
  	display: flex;
  	align-items: center;
  	justify-content: center;
  	cursor: pointer;
  }
  .color_changer .selection_blocks .selection_block{
  		border: 1px solid black;
  }
  .design_tools_blocks{
  	margin-bottom: 20px;
  }
  .color_changer .selection_blocks .selection_block:nth-child(1){background-color:#fff;}
  .color_changer .selection_blocks .selection_block:nth-child(2){background-color:#000;}
  .color_changer .selection_blocks .selection_block:nth-child(3){background-color:#CA8970;}
  .color_changer .selection_blocks .selection_block:nth-child(4){background-color:#FFD600;}
  .color_changer .selection_blocks .selection_block:nth-child(5){background-color:#DBDBDD;}
  .color_changer .selection_blocks .selection_block:nth-child(6){background-color:#7C18FB;}
  .size_changer .selection_blocks .selection_block:hover{background-color:#DBDBDD;}
  /**/

  .writer_block{
  	background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding:20px;
  }
  .writer_block p{
  	font-family: poppins;
  	font-size: 25px;
  	text-align: center;
  }
  .writer_block .mino_inputs{
  	margin: 20px 0px 40px 0px;
  }
  .design_page_buy_btn a{
  	display: block;
  	max-width: 250px;
  	background: #FFD600;
  	border-radius: 10px;
  	padding: 10px 0px;
  	font-family: poppins-bold;
  	font-size: 20px;
  	text-align: center;
  	margin: auto;
  }

  .design_page_services {
  	padding: 40px 0px 20px 0px;
  }
  .design_page_services .servises_blocks div:first-child{
  	padding-left: 0;
  }
  .design_page_services .servises_blocks div:last-child{
  	padding-right: 0;
  }

  /* design styles */
  .image_change_color{
  	position: relative;
  	transition-property:background-color;
  	transition-duration: 0.5s;
  	transition-timing-function: ease;
  }

  .writer_text{
  	position: absolute;
  	width: 97%;
  	left: 2%;
  	top: 1%;
  	height: 98%;
  	overflow: hidden;
  	box-sizing: border-box;
  }
  .design_text{
 		 font-family: poppins-bold;
 		 -webkit-touch-callout: none;
     -webkit-user-select: none;
     -moz-user-select: none;
     -ms-user-select: none;
     user-select: none;
     cursor: move;
     padding: 3px 10px;

  }

  @media(max-width: 1400px){
  	.design_block_items{
  		flex-direction: column;
  	}
  	.design_tools{
  		margin-top: 40px;
  	}
  	.design_image,.design_tools{
  		width: 100%;
  		padding: 0;
  	}
  	.design_image{
  		padding:20px 60px 0px 60px;
  	}
  	.design_block{
	  	max-width: calc(100% - 450px);
	  }
	  .design_right_bar{
	  	max-width: 450px;
	  }
  }
   @media(max-width: 1200px){
  	.design_image{
  		padding:20px 0px 0px 0px;
  	}
  	.design_block{
	  	max-width: calc(100% - 400px);
	  }
	  .design_right_bar{
	  	max-width: 400px;
	  }
  }
   @media(max-width: 992px){
  	.design_block{
	  	max-width: calc(100% - 350px);
	  	padding-right: 20px;
	  }
	  .design_right_bar{
	  	max-width: 350px;
	  }
	  .writer_block p{
	  	font-size: 23px;
	  }
  }
  @media(max-width: 768px){
  	.design_blocks{
  		flex-direction: column-reverse;
  		margin-top: -160px;
  	}
  	.design_block{
	  	max-width: 650px;
	  	padding-right: 0;
	  	margin-left:auto;
	  	margin-right: auto;
	  }
	  .design_right_bar{
	  	max-width: 650px;
	  	position: inherit;
	  	margin-bottom: 20px;
	  	margin-left:auto;
	  	margin-right: auto;
	  }
	  .design_page_pay{
	  	display: none;
	  }
  }
  @media(max-width: 576px){
  	 .writer_block p{
	  	font-size: 22px;
	  }
  	.design_tools{
	  	font-size: 24px;
	  }
	  .tool_selections{
	  	font-size: 22px;
	  }
	  .selection_blocks .selection_block{
	  	width: 40px;
	  	height: 40px;
	  }
  }


</style>