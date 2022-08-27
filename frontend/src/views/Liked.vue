<template>
    <main>
        <Products :products="getLikedProducts" :liked="true">
            <div class="view_title">
                <p>Yoqqan <span>tovarlar</span></p>
            </div>
            <div class="view_title" v-if="!getLikedProducts.length"
                style="height:50vh; display: flex; justify-content: center; align-items: center;">
                <p>Yoqqan tovarlar mavjud emas</p>
            </div>
        </Products>
    </main>
</template>
<script>
import Products from "@/components/Products.vue"
import { mapGetters } from "vuex";
export default {
    components: {
		Products
	},
    computed:{
        ...mapGetters(['getLikedProducts'])
    }
}
</script>
<style>
    
</style>