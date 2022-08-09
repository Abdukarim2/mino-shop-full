<template>
	<div class="mino_inputs">
		<slot></slot>
	</div>
</template>
<script>
export default{
	name:"MinoInput"
}	
</script>
<style>
	.mino_inputs{
		width: 100%;
	}
	.mino_inputs input,.mino_inputs textarea,.mino_inputs select{
		display: block;
		width: 100%;
		border: 1.5px solid #C4C4C4;
		font-family: poppins;
		opacity: 0.7;
		height: 50px;
		font-size: 21px;
		padding: 0px 15px;
		border-radius: 5px;
	}	
	.mino_inputs textarea{
		padding:10px 15px;
		outline: none;
		max-width: 100%;
		min-width: 100%;
		min-height: 160px;
		max-height: 160px;
	}
</style>