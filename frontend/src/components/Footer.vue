<template>
	<footer>
		<section class="footer_section">
			<div class="container_lg">
				<div class="footer_fields">
					<div class="footer_field">
						<div class="footer_logo">
							<router-link to="/">
								<img src="@/assets/img/logo_light.png" alt="logo">
							</router-link>
						</div>
						<div class="footer_about">
							<p>
								Mino bu ajoyib yozuvlik futbulkalar, hudilar, krujkalar va sovg’alar internet do’koni.
							</p>
						</div>
						<div class="footer_number">
							<a>
								+998 93 123 45 67
							</a>
						</div>
					</div>
					<div class="footer_field">
						<ul>
							<li>
								<a>Sahifalar</a>
							</li>
							<li>
								<a>Bosh sahifa</a>
							</li>
							<li>
								<a>Shaxsiy dizayn</a>
							</li>
							<li>
								<a>Do’konlar</a>
							</li>
							<li>
								<a>Aloqa</a>
							</li>
						</ul>
					</div>
					<div class="footer_field">
						<ul>
							<li>
								<a>Hizmatlar</a>
							</li>
							<li>
								<a>Bepul yetkazish</a>
							</li>
							<li>
								<a>Pulni qaytarish</a>
							</li>
							<li>
								<a>Onlayn aloqa</a>
							</li>
							<li>
								<a>To’lov turi</a>
							</li>
						</ul>
					</div>
					<div class="footer_field">
						<ul>
							<li>
								<a>Hamkorlik</a>
							</li>
							<li>
								<a>Hamkorlar uchun</a>
							</li>
							<li>
								<a>Katta buyurtma</a>
							</li>
							<li>
								<a>Savolim bor edi ?</a>
							</li>
							<li>
								<a>Qoidalar</a>
							</li>
						</ul>
					</div>
					<div class="footer_field">
						<ul>
							<li>
								<a>Qo’shimcha</a>
							</li>
							<li>
								<a>Yetkazib berish usuli</a>
							</li>
							<li>
								<a>O’zingiz olib ketmoqchimisiz ?</a>
							</li>
							<li>
								<a>Savatcha</a>
							</li>
							<li>
								<a>Buyurtmalar</a>
							</li>
						</ul>
					</div>
				</div>
				<div class="footer_number footer_number_under">
					<p>
						<a>+998 93 123 45 67</a>
					</p>
				</div>
			</div>
		</section>
	</footer>
</template>
<script>
export default{
	name:"Footer"
}
</script>
<style>
	.footer_section{
		background-color: #404143;
		padding:40px 0px 60px 0px;
		font-family: poppins;
	}
	.footer_fields{
		display: flex;
		color: #fff;
	}
	.footer_field:nth-child(1){
		min-width:24%;
	}
	.footer_field:nth-child(2){
		min-width:15%;
	}
	.footer_field:nth-child(3){
		min-width:17%;
	}
	.footer_field:nth-child(4){
		min-width:19%;
	}
	.footer_field:nth-child(5){
		min-width:25%;
	}
	.footer_logo a img{
		width:140px;
	}
	.footer_about{
		margin:20px 0px;
		padding-right:15%;
		font-size: 18px;
	}
	.footer_number{
		color: #FFD600;
		font-size:28px;
	}
	.footer_field ul li:first-child a{
		font-size:28px;
		opacity: 1;
	}
	.footer_field ul li a{
		display: inline-block;
		font-size:22px;
		padding:4px 0px;
		opacity: 0.7;
		transition-property: opacity;
		transition-duration: 0.5s;
		transition-timing-function: ease-in-out;
	}
	.footer_field ul li a:hover{
		opacity: 1;
	}
	.footer_number_under{
		display: none;
	}
	@media(max-width: 1400px){
		.footer_about{
			padding-right: 0;
		}
		.footer_fields{
			flex-wrap: wrap;
		}
		.footer_field:nth-child(1){
			min-width:100%;
		}
		.footer_field:nth-child(2){
			max-width:22%;
		}
		.footer_field:nth-child(3){
			max-width:24%;
		}
		.footer_field:nth-child(4){
			max-width:24%;
		}
		.footer_field:nth-child(5){
			max-width:30%;
		}
		.footer_number{
			display: none;
		}
		.footer_number_under{
			display: block ;
			margin:20px 0px 0px 0px;
		}
	}
	@media(max-width: 1200px){
		.footer_field:nth-child(2){
			max-width:20%;
		}
		.footer_field:nth-child(3){
			max-width:22%;
		}
		.footer_field:nth-child(4){
			max-width:24%;
		}
		.footer_field:nth-child(5){
			max-width:34%;
		}
	}
	@media(max-width: 992px){
		.footer_field:nth-child(2){
			min-width:50%;
			margin-bottom: 20px;
		}
		.footer_field:nth-child(3){
			min-width:50%;
			margin-bottom: 20px;
		}
		.footer_field:nth-child(4){
			min-width:50%;
		}
		.footer_field:nth-child(5){
			min-width:50%;
		}
	}
	@media(max-width: 992px){
		.footer_about{
			margin:20px 0px 5px 0px;
		}
		.footer_field{
			min-width: 100% !important;
			margin-bottom:15px;
		}
	}
</style>