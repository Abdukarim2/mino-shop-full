<template>
	<div class="product" @dblclick="addLiked">
	  <span class="heart" @click="addLiked" >
		<svg v-if="!heart" 
		:class="{ heart_action: !heart }" xmlns="http://www.w3.org/2000/svg" width="30"  fill="currentColor" viewBox="0 0 16 16">
			  <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
		</svg>
		<svg v-else :class="{ heart_action: heart }" xmlns="http://www.w3.org/2000/svg" width="30"  fill="red" viewBox="0 0 16 16">
		  <path 
		  d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z" />
		</svg>
	  </span>
	  <slot></slot>
	</div>
</template>
<script>
import { mapMutations } from 'vuex';
export default{
	name:"Product",
	data(){
		return {
			heart:false
		}
	},
	props:{
		product:Object,
		liked:Boolean
	},
	beforeMount() {
		this.heart = this.liked
	},
	methods:{
		...mapMutations(['ADD_LIKED','REMOVE_LIKED', 'NOTIFICATION']),
		addLiked(){
			if(!this.heart){
				this.ADD_LIKED(this.product)
				this.NOTIFICATION("Muvofaqiyatlik qo'shildi!")
			}
			if(this.heart){
				this.REMOVE_LIKED(this.product)
			}
			if(!this.liked){
				this.heart = !this.heart
			}
		}
	}
}
</script>
<style>
	.product{
		width: 100%;
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background-color: #fff;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		padding:10% 0%;
		text-align: center;
		transition-property: box-shadow;
		transition-duration: 0.2s;
		transition-timing-function: ease-in;
	}
	.product:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
	}
	.heart{
		padding:15px 15px 10px 15px;
		position: absolute;
		right: 0px;
		top:0px;
		cursor: pointer;
	}
	.heart_action {
	  animation: heart_action 0.8s ease;
	}
	@keyframes heart_action {
	  0% {
	    transform: scale(0);
	  }
	  50% {
	    transform: scale(1.3);
	  }
	  100% {
	    transform: scale(1);
	  }
	}
	.product a img{
		width:100%;
	}
	.product p{
		margin-top:30px;
		color:#000;
		font-size: 26px;
		font-family: poppins-bolder;
	}
	.product p span{
		color: #FE8947;
	}
	@media(max-width: 1200px){
		.product p{
			font-size:22px;
		}	
	}
</style>