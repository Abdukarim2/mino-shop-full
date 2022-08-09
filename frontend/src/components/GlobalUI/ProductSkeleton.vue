<template>
	<div class="product-skeleton">
		<div class="product_img_skeleton"></div>
		<div class="product_text_skeleton"></div>
	</div>
</template>
<script>
export default{
	name:"ProductSkeleton"
}
</script>
<style scoped>
.product-skeleton {
	width: 100%;
	position: relative;
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
.product_img_skeleton{
	width: 100%;
	height: 300px;
	animation: skeleton-loading 1s linear infinite alternate;
	border-radius:10px;
}

.product_text_skeleton{
	width: 80%;
	height: 40px;
	margin-top: 30px;
	animation: skeleton-loading 1s linear infinite alternate;
	margin-left: auto;
	margin-right: auto;
	border-radius:10px;
}

.product-skeleton:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
}
@keyframes skeleton-loading {
  0% {
    background-color: hsl(200, 20%, 70%);
  }

  100% {
    background-color: hsl(200, 20%, 95%);
  }
}
@media(max-width: 1400px){
	.product_img_skeleton{
		height: 250px;
	}
}
@media(max-width: 1200px){
	.product_img_skeleton{
		height: 350px;
	}
}
@media(max-width: 768px){
	.product_img_skeleton{
		width: 95%;
		margin: auto;
	}
}
@media(max-width: 400px){
	.product_img_skeleton{
		width: 100%;
		
	}
}
</style>