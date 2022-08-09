<template>
  <div class="social_medas_block">
  	<div class="social_title">
  	  <p>Biz ijtimoiy tarmoqlarda</p>
  	</div>
  	<ul>
  	  <li>
  	  	<a>
  	  	  <span>
  	  	  	<img src="@/assets/img/Facebook.png" alt="Facebook">
  	  	  </span>
  	  	  <span>Facebok</span>
  	  	</a>
  	  </li>
  	  <li>
  	  	<a>
  	  	  <span>
  	  	  	<img src="@/assets/img/instagram.png" alt="Instagram">
  	  	  </span>
  	  	  <span>Instagram</span>
  	  	</a>
  	  </li>
  	  <li>
  	  	<a>
  	  	  <span>
  	  	  	<img src="@/assets/img/telegram.png" alt="Telegram">
  	  	  </span>
  	  	  <span>Telegram</span>
  	  	</a>
  	  </li>
  	</ul>
  </div>
</template>
<script>
export default{
	name:"SocialMedias"
}
</script>
<style>
	.social_medas_block{
		margin-top: 20px;
		background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding: 10px 20px;
	}
	.social_title{
		font-family: poppins-bolder;
		font-size: 25px;
	}
	.social_medas_block ul li a span img{
		width: 30px;
	}
	.social_medas_block ul li a{
		display: flex;
		align-items: center;
		padding:5px 0px;
		font-family: poppins;
		font-size: 21px;
	}
	.social_medas_block ul li a span:nth-child(1){
		transform: translateY(5px);
		margin-right: 7px;
	}
	@media(max-width: 576px){
		.social_title{
			font-size: 23px;
		}
	}
</style>