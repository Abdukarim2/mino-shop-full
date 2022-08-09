<template>
  <div class="order_total_block">
  	<p>Buyurtmaga</p>
  	<slot></slot>
  	<div class="to_order_btn">
  	  <a>
  	  	<span>
	  	    <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 40 40" fill="none">
			<path d="M20 23.3333H21.6667C23.5 23.3333 25 21.8333 25 20V3.33334H10C7.5 3.33334 5.31668 4.71665 4.18335 6.74998" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M3.33325 28.3333C3.33325 31.1 5.56659 33.3333 8.33325 33.3333H9.99992C9.99992 31.5 11.4999 30 13.3333 30C15.1666 30 16.6666 31.5 16.6666 33.3333H23.3333C23.3333 31.5 24.8333 30 26.6666 30C28.4999 30 29.9999 31.5 29.9999 33.3333H31.6666C34.4333 33.3333 36.6666 31.1 36.6666 28.3333V23.3333H31.6666C30.7499 23.3333 29.9999 22.5833 29.9999 21.6667V16.6667C29.9999 15.75 30.7499 15 31.6666 15H33.8166L30.9666 10.0167C30.3666 8.98335 29.2666 8.33334 28.0666 8.33334H24.9999V20C24.9999 21.8333 23.4999 23.3333 21.6666 23.3333H19.9999" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M13.3333 36.6667C15.1743 36.6667 16.6667 35.1743 16.6667 33.3333C16.6667 31.4924 15.1743 30 13.3333 30C11.4924 30 10 31.4924 10 33.3333C10 35.1743 11.4924 36.6667 13.3333 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M26.6666 36.6667C28.5075 36.6667 29.9999 35.1743 29.9999 33.3333C29.9999 31.4924 28.5075 30 26.6666 30C24.8256 30 23.3333 31.4924 23.3333 33.3333C23.3333 35.1743 24.8256 36.6667 26.6666 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M36.6667 20V23.3333H31.6667C30.75 23.3333 30 22.5833 30 21.6667V16.6667C30 15.75 30.75 15 31.6667 15H33.8166L36.6667 20Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M3.33325 13.3333H13.3333" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M3.33325 18.3333H9.99992" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			<path d="M3.33325 23.3333H6.66659" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
			</svg>
  	  	</span>
  	  	<span>Buyurtma</span>
  	  </a>
  	</div>
  </div>
</template>
<script>
export default{
	name:"OrderTotal"
}	
</script>
<style>
	.order_total_block{
		background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding: 10px 20px 20px 20px;
	}
	.order_total_block p{
		font-family: poppins-bolder;
		font-size: 28px;
	}
	.to_order_btn{
		margin-top: 20px;
	}
	.to_order_btn a{
		display:block;
		max-width: 80%;
		margin: auto;
		text-align: center;
		padding:8px 0px;
		background-color: #FFD600;
		border-radius: 10px;
		font-family: poppins-bolder;
		font-size: 25px;
	}
	.to_order_btn a span svg{
		width: 30px;
		transform: translateY(6px);
		margin-right: 10px;
	}
	.order_total_block ul li{
		font-family: poppins-bold;
		padding:5px 0px;
		font-size: 18px;
	}
	@media(max-width: 992px){
		.order_total_block ul li{
			font-size: 16px;
		}
		.to_order_btn a{
			font-size: 23px;
		}
	}
	@media(max-width: 576px){
		.to_order_btn a{
			max-width: 400px;
		}
	}
</style>