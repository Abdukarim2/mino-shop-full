<template>
	<TransitionGroup name="banner">
		<article v-if="bannerTr">
			<section class="banner_section">
				<div class="container_lg">
					<div class="banner_fields">
						<div class="banner_field" >
							<div class="banner_rotate_text">
								<p>Ajoyib</p>
							</div>
							<div class="banner_rotate_text">
								<p>yozuvlik</p>
							</div>
							<div class="banner_rotate_text">
								<p>futbolkalar.</p>
							</div>
						</div>
						<div class="banner_field">
							<a>
								<img src="@/assets/img/jacket.png" alt="jacket">
							</a>
						</div>
					</div>
				</div>
			</section>
		</article>
	</TransitionGroup>
</template>
<script>
export default{
	name:"Banner",
	data(){
		return {
			bannerTr:false
		}
	},
	mounted(){
		this.bannerTr = true
	}
}
</script>
<style>
  /* start banner */
  .banner_fields{
  	padding: 2% 5%;
  	display: flex;
  	align-items: center;
  	font-family: poppins-bold;
  	margin-bottom: 40px;
  }
  .banner_rotate_text p{
  	display: inline-block;
  	width: auto;
  	font-size:70px;
  	background-color: #fff;
  	padding: 0px 70px 5px 70px;
  	-webkit-box-shadow: 1px 5px 6px 0px rgba(34, 60, 80, 0.08);
		-moz-box-shadow: 1px 5px 6px 0px rgba(34, 60, 80, 0.08);
		box-shadow: 1px 5px 6px 0px rgba(34, 60, 80, 0.08);
  }
  .banner_rotate_text:nth-child(1) p{
  	color: #FFD600;
  	transform: rotate(-6.04deg);
  }
  .banner_rotate_text:nth-child(2) p{
  	color: #CA8970;
  	transform:  translateX(15%) rotate(-0.87deg);
  	margin-top:4%;
  }
  .banner_rotate_text:nth-child(3) p{
  	background-color: transparent;
  	box-shadow: none;
  	padding: 0;
  	transform:  translateX(10%) rotate(-8.33deg);
  	margin-top:4%;
  }
  .banner_field a img{
  	width: 70%;
  	float: right;
  }
  /* start vue transition group */
  .banner-enter-from{
  	opacity: 0;
  }
  .banner-enter-to {
  	opacity: 1;
  }
  .banner-enter-active{
    transition: opacity 1.5s ease;
  }
  .banner-leave-from{
  	opacity: 1;
  }
  .banner-leave-to {
  	opacity: 0;
  }
  .banner-leave-active{
    transition: opacity 1s ease;
  }
  /* end vue transition group */
  /* end banner */
  @media(max-width: 1300px){
  	 .banner_rotate_text p{
  	 	font-size: 60px;
  	 }
  }
  @media(max-width: 1200px){
  	 .banner_rotate_text p{
  	 	font-size: 50px;
  	 }
  }
  @media(max-width: 992px){
  	 .banner_fields{
  	 	flex-direction: column;
  	 }
  	 .banner_rotate_text:nth-child(2){
  	 	text-align: right;
  	 }
  	 .banner_rotate_text:nth-child(2) p {
  	 	transform:  translateX(0%) rotate(-0.87deg);
  	 }
  	 .banner_field a img{
  	 	display: block;
  	 	margin: auto;
  	 	width: 50%;
  	 	float: inherit;
  	 }
  }
  @media(max-width: 768px){
  	 .banner_field a img{
  	 	width: 60%;
  	 }
  	 .banner_fields{
  	 	padding:8% 5%;
  	 }
  }
  @media(max-width: 576px){
  	 .banner_fields{
  	 	padding:6% 0%;
  	 }
  	 .banner_rotate_text p{
  	 	padding: 0px 50px 5px 50px;
  	 	font-size: 40px;
  	 }
  	 .banner_rotate_text:nth-child(2) p {
  	 	margin:8% 0% 3% 0%;
  	 }
  	 .banner_field a img{
  	 	margin-top:3%;
  	 	width: 70%;
  	 }
  }
</style>