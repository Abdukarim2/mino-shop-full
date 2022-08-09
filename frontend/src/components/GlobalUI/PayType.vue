<template>
  <div class="pay_agents">
	<p>To’lov usullari </p>	
	<div class="pay_agents_items">
	  <a>
	  	<img src="@/assets/img/payme.png" alt="payme">
	  </a>
	  <a>
	  	<img src="@/assets/img/apelsin.png" alt="aplesin">
	  </a>
	</div>
  </div>
</template>
<script>
export default{
	name:"PayType"
}
</script>
<style>
.pay_agents{
	background: #FFFFFF;
	box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
	border-radius: 10px;
	padding: 10px 20px 20px 20px;
	margin-top: 20px;
}	
.pay_agents{
	font-family: poppins;
	font-size: 22px;
}
.pay_agents_items{
	display: flex;
	flex-direction: column;
	margin-top: 20px;
}
.pay_agents_items a img{
	width: 50%;
}
@media(max-width: 768px){
	.pay_agents_items{
		flex-direction: row;
	}
	.pay_agents_items a img{
		width: 100%;
	}
}

</style>