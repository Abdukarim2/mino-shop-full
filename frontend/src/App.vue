<template>
	<!-- start navbar -->
	<Navbar />
	<!-- start main -->
	<router-view></router-view>

	<!-- Notification -->
	<Notification :class="{ notification_show: notification }"></Notification>

	<!-- start footer -->
	<Footer />
</template>
<script>

import Header from "@/components/Header.vue"
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import Notification from "@/components/GlobalUI/Notification.vue"
import { mapState, mapMutations } from "vuex"
export default {
	components: {
		Header,
		Navbar,
		Footer,
		Notification
	},
	computed: {
		...mapState(['notification'])
	},
	beforeMount() {
		this.INITIAL()
	},
	methods: {
		...mapMutations(['INITIAL'])
	}
}
</script>

<style>
@import "@/assets/css/custom.css";
</style>