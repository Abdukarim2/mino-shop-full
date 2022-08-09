<template>
  <section class="try_section">
	  <div class="container_lg">
	  	<div class="try_fields">
	  	  <div class="try_blocks">
	  	  	<div class="try_field">
	  	  	  <div class="try_text_field">
	  	  		<p>
	  	  			Shaxsiz matningizni istalgan rangdagi  sifatli futbolkaga tushirib beramiz!
	  	  		</p>
	  	  		<p class="try_price_field">
	  	  			Boshlanish narxi 63.000 uzs
	  	  		</p>
	  	  		<div class="try_btn_field">
	  	  			<a>
	  	  				Sinab ko’rish
	  	  			</a>
	  	  		</div>
	  	  	  </div>
	  	  	  <div class="try_image_field">
	  	  	  	<a>
	  	  	  		<img src="@/assets/img/t-shirt.png" alt="t-shirt">
	  	  	  	</a>
	  	  	  </div>
	  	  	</div>
	  	  </div>
	  	  <div class="try_blocks">
	  	  	<div class="try_field">
	  	  	  <div class="try_text_field">
	  	  		<p>
	  	  			Shaxsiz dizayningizni turli xildagi  sifatli krujkalarga chop etamiz!
	  	  		</p>
	  	  		<p class="try_price_field">
	  	  			Boshlanish narxi 63.000 uzs
	  	  		</p>
	  	  		<div class="try_btn_field">
	  	  			<a>
	  	  				Sinab ko’rish
	  	  			</a>
	  	  		</div>
	  	  	  </div>
	  	  	  <div class="try_image_field">
	  	  	  	<a>
	  	  	  		<img src="@/assets/img/cup.png" alt="t-shirt">
	  	  	  	</a>
	  	  	  </div>
	  	  	</div>
	  	  </div>
	  	</div>
	  </div>
  </section>
</template>
<script>
	
</script>
<style>
	.try_fields{
		display: flex;
		margin:70px 0px 40px 0px;
	}
	.try_field{
		background: linear-gradient(105.72deg, rgba(255, 255, 255, 0) 10.7%,#DBDBDD 100.47%);
		filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.1));
		border-radius: 10px;
	}

	.try_blocks:nth-child(1){
		padding-right: 20px;
	}
	.try_blocks:nth-child(2){
		padding-left: 20px;
	}
	.try_field{
		display: flex;
		padding:20px;
	}
	.try_text_field{
		width: 55%;
		padding:2% 0%;
	}
	.try_image_field{
		width: 45%;
	}
	.try_image_field a img{
		width: 100%;
	}
	.try_text_field p {
		font-size:22px;
		font-family: poppins-bold;
	}
	.try_text_field .try_price_field {
		font-size:18px;
		margin:10% 0%;
		font-family: poppins;
	}
	.try_btn_field a{
		width:250px;
		max-width:250px;
		display: inline-block;
		background: #FFD600;
		text-align: center;
		padding:12px 0px;
		border-radius:10px;
		font-family: poppins-bold;
		font-size:20px;
	}
	@media(max-width: 1400px){
		.try_text_field p{
			font-size:18px;
		}
		.try_text_field .try_price_field{
			font-size:15px;
		}
		.try_btn_field a{
			padding: 10px 0px;
			width:210px;
			max-width:210px;
			font-size: 16px;
		}
	}
	@media(max-width: 1200px){
		.try_field{
			background: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%,#DBDBDD 30.47%);
		}
		.try_field{
			flex-direction: column-reverse;
		}
		.try_text_field,.try_image_field{
		  width: 100%;
		}
		.try_blocks:nth-child(1){
			padding-right: 10px;
		}
		.try_blocks:nth-child(2){
			padding-left: 10px;
		}
		.try_text_field{
			margin:5% 0%;
		}
	}
	@media(max-width: 768px){
		.try_fields{
			flex-wrap: wrap;
			justify-content: center;
		}
		.try_blocks{
			width: 450px;
			max-width: 450px;
			padding-right: 0 !important;
		}
		.try_btn_field{
			text-align: center;
		}

	}
</style>