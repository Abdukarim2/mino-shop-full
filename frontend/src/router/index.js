import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Products from '@/views/Products.vue'
import Detail from '@/views/Detail.vue'
import Cart from '@/views/Cart.vue'
import Design from '@/views/Design.vue'
import Order from '@/views/Order.vue'
import Success from '@/views/Success.vue'
import Liked from "@/views/Liked.vue"


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path:'/products/:by/',
    name:'products',
    component:Products
  },
  {
    path: '/products/detail/:slug/:id/',
    name: 'detail',
    component: Detail
  },
  {
    path: '/cart/',
    name: 'cart',
    component: Cart
  },
  {
    path: '/design/:item',
    name: 'design',
    component: Design
  },
  {
    path: '/order/',
    name: 'order',
    component: Order
  },
  {
    path: '/success/',
    name: 'success',
    component: Success
  },
  {
    path:"/products/liked/",
    name:"liked",
    component:Liked
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition){
    if (to.hash) {
      return {
        el: to.hash,
      }
    }
  }
})

export default router
