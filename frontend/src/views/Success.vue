<template>
  <main>
    <section class="section_success_page">
 	  <div class="container_lg">
 	  	<div class="success_items">
 	  	  <div class="success_page_car">
 	  	    <a>
 	  	      <img src="@/assets/img/shipped.png" alt="">
 	  	    </a>
 	      </div>
 	      <div class="success_page_text">
 	        <p>
 	      	  ID : <span>#bdf223</span> lik buyurtma muvaffaqiyatli yetkazib berish jarayoniga   qo’shildi. Tez orada tovar qo’lingizda bo’ladi ! 
 	        </p>
 	      </div>
 	      <div class="success_page_back">
 	        <a>
 	      	  Ortga 
 	        </a>
 	      </div>
 	  	</div>
 	  </div>
 	</section>	
  </main>
</template>
<script>
export default{
	name:"Success"
}
</script>
<style>
  .success_items{
  	height: 600px;
  	display: flex;
  	flex-direction: column;
  	justify-content: center;
  	text-align: center;
  	padding-bottom: 40px;
  }
  .success_page_car a img{
  	width: 180px;
  }
  .success_page_text{
  	font-family: poppins-bold;
  	font-size: 27px;
  	padding:40px 10%;
  }
  .success_page_text span{
  	color: #FE8947;
  }
  .success_page_back a{
  	display: block;
  	padding: 9px 0px;
  	font-family: poppins-bolder;
  	font-size: 25px;
  	text-align: center;
  	border-radius: 10px;
  	background: #FFD600;
  	max-width: 250px;
  	margin: auto;
  }
   @media(max-width: 768px){
   	 .success_page_car a img{
   	 	width: 150px;
   	 }
 	 .success_page_text{
 	 	font-size: 23px;
 	 	padding:20px 0px;
 	 }
 	 .success_page_back a{
 	 	font-size: 22px;
 	 }
  }
  @media(max-width: 1200px){
  	.success_items{
  		height: 550px;
  	}
  }
  @media(min-width: 1650px){
  	.success_items{
  		height: 650px;
  	}
  }
  @media(min-width: 1900px){
  	.success_items{
  		height: 700px;
  	}
  }
</style>