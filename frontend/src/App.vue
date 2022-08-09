<template>
	<!-- start navbar -->
	<Navbar/>

	<!-- start main -->
	<router-view></router-view>

	<!-- start footer -->
	<Footer/>
</template>

<script>
import Header from "@/components/Header.vue"
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"

export default {
  components: {
    Header,
    Navbar,
    Footer
  }
}
</script>

<style>
	@import "@/assets/css/custom.css";
	
</style>