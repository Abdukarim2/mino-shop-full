<template>
  <main>
  	<section class="order_page_section">
  	  <div class="container_lg">
  	  	<div class="view_title">
	  	  <p>Buyurtma berish</p>
	  	</div>
  	  	<div class="order_blocks" v-if="getAllProducts.length > 0">
  	  	  <div class="order_form">
  	  	  	<div class="order_form_block">
  	  	  	  <div class="order_title">
			  	<p>Buyurtma berish formasi</p>
			  </div>
  	  	  	  <form @submit.prevent="sendOrder">
			    <div class="inputs_blocks">
			      <div class="inpu_block">
			        <MinoInput>
					  <input type="text" placeholder="Ism" v-model="order.name" required>
					</MinoInput>
			       </div>	
			       <div class="inpu_block">
			       <MinoInput>
				     <input type="text" placeholder="Familiya" v-model="order.surname" required>
				   </MinoInput>
			      </div>
			    </div>
			    <div class="inputs_blocks">
			      <div class="inpu_block">
			        <MinoInput>
					  <input type="text" placeholder="Pochta" v-model="order.email" required>
					</MinoInput>
			      </div>	
			    </div>
			    <div class="inputs_blocks">
			      <div class="inpu_block">
			        <MinoInput>
					  <input type="text" placeholder="Manzil" v-model="order.location" required>
					</MinoInput>
			      </div>	
			    </div>
			    <div class="inputs_blocks">
			      <div class="inpu_block">
			        <MinoInput>
					  <input type="number" placeholder="Telefon" v-model="order.phone_number" required>
					</MinoInput>
			       </div>	
			       <div class="inpu_block">
			       <MinoInput>
				     <input type="number" placeholder="Pochta indeksi" v-model="order.index" >
				   </MinoInput>
			      </div>
			    </div>
			    <div class="inputs_blocks">
			      <div class="inpu_block">
			        <MinoInput>	
					  <select required  @change="order.pay_type = $event.target.value">
						<option value="" selected disabled hidden>To'lov turi</option>
						<option value="Payme">Payme</option>
						<option value="Apelsin">Apelsin</option>
					  </select>
					</MinoInput>
			       </div>	
			       <div class="inpu_block">
			       <MinoInput>
				     <input type="text" placeholder="Kupon (agar bo’lsa)" v-model="order.coupon">
				   </MinoInput>
			      </div>
			    </div>
			    <div class="order_form_submit">
			       <button type="submit">
			       	 <span>
			       	 	<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 40 40" fill="none">
						<path d="M20 23.3333H21.6667C23.5 23.3333 25 21.8333 25 20V3.33334H10C7.5 3.33334 5.31668 4.71665 4.18335 6.74998" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M3.33325 28.3333C3.33325 31.1 5.56659 33.3333 8.33325 33.3333H9.99992C9.99992 31.5 11.4999 30 13.3333 30C15.1666 30 16.6666 31.5 16.6666 33.3333H23.3333C23.3333 31.5 24.8333 30 26.6666 30C28.4999 30 29.9999 31.5 29.9999 33.3333H31.6666C34.4333 33.3333 36.6666 31.1 36.6666 28.3333V23.3333H31.6666C30.7499 23.3333 29.9999 22.5833 29.9999 21.6667V16.6667C29.9999 15.75 30.7499 15 31.6666 15H33.8166L30.9666 10.0167C30.3666 8.98335 29.2666 8.33334 28.0666 8.33334H24.9999V20C24.9999 21.8333 23.4999 23.3333 21.6666 23.3333H19.9999" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M13.3333 36.6667C15.1743 36.6667 16.6667 35.1743 16.6667 33.3333C16.6667 31.4924 15.1743 30 13.3333 30C11.4924 30 10 31.4924 10 33.3333C10 35.1743 11.4924 36.6667 13.3333 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M26.6666 36.6667C28.5075 36.6667 29.9999 35.1743 29.9999 33.3333C29.9999 31.4924 28.5075 30 26.6666 30C24.8256 30 23.3333 31.4924 23.3333 33.3333C23.3333 35.1743 24.8256 36.6667 26.6666 36.6667Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M36.6667 20V23.3333H31.6667C30.75 23.3333 30 22.5833 30 21.6667V16.6667C30 15.75 30.75 15 31.6667 15H33.8166L36.6667 20Z" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M3.33325 13.3333H13.3333" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M3.33325 18.3333H9.99992" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M3.33325 23.3333H6.66659" stroke="#404143" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
						</svg>
			       	 </span>
			       	 <span>Habarni yuborish</span>
			       </button>
			    </div>
		      </form>
  	  	  	</div>
  	  	  </div>
  	  	  <div class="order_right_bar">
  	  		<OrderTotal>
  	  		  <ul>
			  	<li>Tovarlar soni : {{getAllProducts.length}} ta </li>
			  	<li>Umumiy summa : ${{getTotalPrice[0]}} - {{getTotalPrice[1]}} uzs</li>
			  	<li>Yetkazib berish : Bepul</li>
			  	<li>Chegirma bilan : {{getTotalPrice[1]}} uzs</li>
			  </ul>
  	  		</OrderTotal>
  	  		<PayType/>
  	  	  </div>
  	  	</div>
		<div style="width:100%; height:60vh; display:flex; align-items: center; text-align: center;"  v-else>
			<div class="view_title">
				<p>Savatchangiz bo'sh</p>
			</div>
		</div>
  	  </div>
  	  <!-- start Services -->
	  <Services/>
  	</section>
  </main>
</template>
<script>
import OrderTotal from "@/components/GlobalUI/OrderTotal.vue"
import PayType from "@/components/GlobalUI/PayType.vue"
import Services from "@/components/Services.vue"
import axios from "axios"
import { mapGetters, mapMutations } from "vuex"
export default{
	name:"Order",
	data() {
		return {
			order: {
				name:null,
				surname:null,
				email:null,
				location:null,
				phone_number:null,
				index:null,
				pay_type:null,
				coupon:'',
				products:[]
			}
		}
	},
	components:{
		OrderTotal,
		PayType,
		Services
	},
	beforeMount() {
		for (let item of this.getAllProducts){
			this.order.products.push(
				JSON.stringify({id:item.id,color:item.color, size:item.size, quantiy:item.quantiy})
			)
		}
	},
	computed: {
		...mapGetters(['getAllProducts']),
		...mapGetters(['getTotalPrice'])
	},
	methods:{
		async sendOrder(){
			await axios.post("management/order/", JSON.stringify(this.order),
				{
					headers: {
					'Content-Type': 'application/json'
					}
				}

			)
			.then(reponse=>{
				console.log(reponse.data)
			})
		}
	}
}
</script>
<style>
  .order_blocks{
  	display: flex;
  	padding-bottom: 50px;
  }
  .order_form{
  	width: calc(100% - 380px);
  	padding-right: 50px;
  }
  .order_right_bar{
  	width: 380px;
  	position: sticky;
  	top: 0;
  	height: 100%;
  }
  .order_form_block{
  	background: #FFFFFF;
	box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
	border-radius: 10px;
	padding: 30px 50px;
  }
  .order_title{
  	font-family: poppins-bolder;
  	font-size: 35px;
  	padding-bottom:15px;
  }
  .order_form_submit button{
  	padding:10px;
  	border-radius: 10px;
  	background: #FFD600;
  	text-align: center;
	width: 350px;
  	font-family: poppins-bolder;
  	font-size: 24px;
  	margin-top: 10px;
	border: none;
  }
  .order_form_submit button span svg{
  	width: 30px;
  	transform: translateY(5px);
  	margin-right: 10px	;
  }
  @media(max-width: 1200px){
  	.order_form_block{
  		padding: 20px 30px;
  	}
  	.order_form{
  		padding-right: 20px;
  	}
  }
  @media(max-width: 992px){
  	  .order_title{
	  	font-size: 28px;
	  	padding-left: 10px;
	  }
	  .order_form{
	  	width: calc(100% - 330px);
	  	padding-right: 20px;
	  }
	  .order_right_bar{
	  	width: 330px;
	  	position: sticky;
	  }
	  .order_form_submit{
	  		padding: 10px 10px;
	  }
	  .order_form_block{
	  	padding: 10px;
	  }
  }
  @media(max-width: 768px){
  	.order_blocks{
	   flex-direction: column-reverse;
	}
	.order_form{
	  	width: 100%;
	  	padding-right: 0;
	  	margin-top: 20px;
	}
	.order_right_bar{
	  	width: 100%;
	  	position: inherit;
	 }
	.order_form_submit button{
  		font-size: 22px;
  	}
  	.order_title{
  		font-size: 25px;
	}
  }
  @media(max-width: 576px){
	.order_form_submit button{
		width: 100%;
	}
  }
</style> 