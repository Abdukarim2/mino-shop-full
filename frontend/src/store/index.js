import { setTimeout } from 'core-js'
import { createStore } from 'vuex'

export default createStore({
  state: {
    products: [],
    notification: false,
    liked:[],
    notificationContent:""
  },
  getters: {
    getCartLength(state) {
      return state.products.length
    },
    getAllProducts(state) {
      return state.products
    },
    getTotalPrice(state){
      let sumUZS = 0;
      let sumUSD = 0;
      for(let product of state.products){
        sumUSD += (product.priceDolor * product.quantity);
        sumUZS += (product.price * product.quantity);
      }
      let decimial = String(sumUZS).replace("000", "") 
      return [sumUSD, decimial+".000"]
    },
    getLikedProducts(state){
      return state.liked
    }
  },
  mutations: {
    INITIAL(state) {
      let products = localStorage.getItem("cartProducts")
      let liked = localStorage.getItem("liked")
      if (products && liked) {
        state.products = JSON.parse(products)
        state.liked = JSON.parse(liked)
      }
      else {
        localStorage.setItem("cartProducts", JSON.stringify(state.products))
        localStorage.setItem("liked", JSON.stringify(state.liked))
      }
    },
    ADD_TO_CART(state, obj) {
      obj.color = ""
      obj.size = ""
      obj.quantity = 1
      state.products.push(obj)
      localStorage.setItem("cartProducts", JSON.stringify(state.products))
    },
    NOTIFICATION(state, content) {
      state.notificationContent = content
      state.notification = !state.notification
      setTimeout(() => {
        state.notification = !state.notification
      }, 2000)
    },
    REMOVE_ITEM(state, index) {
      // state.products = state.products.filter(e=> e.id !== id)
      state.products.splice(index,1)
      localStorage.setItem("cartProducts", JSON.stringify(state.products))
    },
    EDIT_CART_ITEM(state, items){
      if(items.quantity){
        state.products[items.index].quantity = items.quantity
      }
      if(items.color){
        state.products[items.index].color = items.color
      }
      if(items.size){
        state.products[items.index].size = items.size
      }
      localStorage.setItem("cartProducts", JSON.stringify(state.products))
    },
    ADD_LIKED(state, obj){
      state.liked.push(obj)
      localStorage.setItem("liked", JSON.stringify(state.liked))
    },
    REMOVE_LIKED(state, obj){
      let index = state.liked.indexOf(obj)
      state.liked.splice(index,1)
      localStorage.setItem("liked", JSON.stringify(state.liked))
    }
  },
  actions: {
  },
  modules: {
  }
})
