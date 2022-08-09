<template>
	<a class="cart_service">
		<slot></slot>
	</a>
</template>
<script>
export default{
	name:"ServiceCart"
}
</script>
<style>
	.cart_service{
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background-color: #fff;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding:10%;
		text-align: center;
		transition-property: box-shadow;
		transition-duration: 0.2s;
		transition-timing-function: ease-in;
	}
	.cart_service img{
		width:55%;
	}
	.cart_service p{
		margin-top:20px;
		font-size:18px;
		font-family: poppins-bold;
	}
	.cart_service:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
	}
	@media(max-width: 768px){
	  	.cart_service p{
			font-size:15px;
		}
  	}
	@media(max-width: 576px){
		.cart_service img{
			width: 50%;
		}
		.cart_service p{
			font-size:13px;
		}
  	}
</style>