<template>
	<section class="services_section">
	  <div class="container_lg">
	    <div class="servises_blocks">
		   <div>
		     <service-cart>
				<img src="@/assets/img/shipped.png" alt="shipped">
				<p>
					O’zbekiston bo’ylab yetkazib berish
				</p>
		     </service-cart>
		   </div>
		   <div>
		     <service-cart>
				<img src="@/assets/img/debit.png" alt="debit">
				<p>
					Qulay to’lov<br>usullari
				</p>
			 </service-cart>
		   </div>
		   <div>
			 <service-cart>
				<img src="@/assets/img/24hours.png" alt="24hours">
				<p>
					Haftada 7 kun 24 soat aloqadamiz
				</p>
			 </service-cart>
		   </div>
		   <div>
			 <service-cart>
				<img src="@/assets/img/quality.png" alt="quality">
				<p>
					Yuqori sifatli<br>tovarlar
				</p>
			 </service-cart>
		   </div>
		   <div>
			 <service-cart>
				<img src="@/assets/img/salary.png" alt="salary">
				<p>
					3 kun ichida pulni qaytarib olish
				</p>
	   		 </service-cart>
		   </div>
		</div>
	  </div>
	</section>
</template>
<script>
import ServiceCart from "@/components/GlobalUI/ServicesCart.vue"
export default{
	components:{
		ServiceCart
	}
}
</script>
<style>
	.servises_blocks{
		display: flex;
		margin-bottom:40px;
  	}
  	.servises_blocks div{
		padding: 0px 12px;
  	}
  	@media(max-width: 1200px){
	  	.servises_blocks{
	  		flex-wrap: wrap;
	  		justify-content: center;
	  	}
	  	.servises_blocks div{
			width: 33.333333%;
			padding:12px;
	  	}
  	}

  	@media(max-width: 576px){
  		.servises_blocks div{
  			width: 50%;
			padding:6px;
	  	}
  	}
</style>