<template>
	<a class="cart_category">
		<slot></slot>
	</a>
</template>
<script>
export default{
	name:"CategoryCart"
}
</script>
<style>
	.cart_category{
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background-color: #fff;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding:10% 5%;
		text-align: center;
		transition-property: box-shadow;
		transition-duration: 0.2s;
		transition-timing-function: ease-in;
	}
	.cart_category:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
	}
	.cart_category img{
		width:35%;
	}
	.cart_category p{
		font-family: poppins;
		font-size: 14px;
		margin-top:15px;
	}
</style>