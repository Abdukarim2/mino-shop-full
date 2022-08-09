<template>
  <section class="section_contact_form">
  	<div class="container_lg">
  	  <slot></slot>
	  <div class="contact_form_blocks">
	    <div class="contact_form_block">
	      <form>
	      	<div class="inputs_blocks">
	      	  <div class="inpu_block">
	      	   	<MinoInput>
			      	  <input type="text" placeholder="Ism">
			      	</MinoInput>
	      	  </div>	
	      	  <div class="inpu_block">
	      	   	<MinoInput>
			      	  <input type="text" placeholder="Pochta">
			      	</MinoInput>
	      	  </div>
	      	</div>
	      	<div class="inputs_blocks">	
	      	  <div class="inpu_block">
	      	   	<MinoInput>
			      	  <input type="text" placeholder="Mavzu">
			      	</MinoInput>
	      	  </div>
	      	</div>
	      	<div class="inputs_blocks">	
	      	  <div class="inpu_block">
	      	   	<MinoInput>
			      	  <textarea placeholder="Habar"></textarea>
			      	</MinoInput>
	      	  </div>
	      	</div>
	      	<div class="contact_form_submit">
	      		<input type="submit" value="Habarni yuborish">
	      	</div>
	      </form>
	     </div>
	    <div class="contact_block">
	      <div class="contact_items">
	      	<ul>
	      		<li>
	      			<a>
	      				<span>
	      					<svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 33 29" fill="none">
									<path d="M6.71904 26.0981L6.27399 24.6657H6.27399L6.71904 26.0981ZM3.86302 26.9096L4.11918 28.3876H4.11918L3.86302 26.9096ZM6.3141 2.6732L6.67883 4.12818L6.3141 2.6732ZM11.6154 2.09968L11.9589 0.639548C11.9483 0.637063 11.9377 0.634693 11.9271 0.632438L11.6154 2.09968ZM3.3983 3.75784L2.80109 2.38185L2.80109 2.38185L3.3983 3.75784ZM25.9498 26.0981L25.5048 24.6657H25.5048L25.9498 26.0981ZM21.2308 26.9098L20.8873 28.3699C20.8978 28.3724 20.9084 28.3748 20.919 28.377L21.2308 26.9098ZM29.0361 25.1214L28.6071 23.6841L28.6071 23.6841L29.0361 25.1214ZM25.5449 2.6732L25.1802 1.21822L25.5449 2.6732ZM28.979 2.03509L28.8532 0.540372L28.979 2.03509ZM21.5301 4.23484L22.1205 5.61376L21.5301 4.23484ZM20.9142 4.2874L20.5707 5.74753L20.9142 4.2874ZM11.3969 24.6956L11.7291 26.1584L11.3969 24.6956ZM11.8333 24.6989L11.4897 26.159L11.8333 24.6989ZM6.27399 24.6657C5.17192 25.0081 4.39551 25.295 3.60685 25.4316L4.11918 28.3876C5.16243 28.2068 6.26351 27.8104 7.16408 27.5306L6.27399 24.6657ZM11.0646 23.2329C9.52452 23.5827 7.79487 24.1931 6.27399 24.6657L7.16408 27.5306C8.85704 27.0046 10.3405 26.4738 11.7291 26.1584L11.0646 23.2329ZM6.67883 4.12818C7.38791 3.95043 8.27214 3.74169 9.14889 3.61435C10.0574 3.4824 10.8089 3.46181 11.3036 3.56693L11.9271 0.632438C10.8996 0.414103 9.71963 0.499984 8.7177 0.645504C7.684 0.795638 6.67872 1.03539 5.94936 1.21822L6.67883 4.12818ZM3.9955 5.13383C5.0181 4.69 5.91763 4.319 6.67883 4.12818L5.94936 1.21822C4.91355 1.47788 3.79689 1.94965 2.80109 2.38185L3.9955 5.13383ZM0.5 5.84778V25.0891H3.5V5.84778H0.5ZM2.80109 2.38185C1.42553 2.97887 0.5 4.32593 0.5 5.84778H3.5C3.5 5.56561 3.67472 5.27305 3.9955 5.13383L2.80109 2.38185ZM3.60685 25.4316C3.58431 25.4356 3.59224 25.4305 3.61301 25.4378C3.62969 25.4436 3.62728 25.4479 3.61056 25.4305C3.56843 25.3865 3.5 25.2661 3.5 25.0891H0.5C0.5 25.9752 0.824154 26.8584 1.44407 27.5056C2.08978 28.1798 3.04619 28.5735 4.11918 28.3876L3.60685 25.4316ZM25.5048 24.6657C24.5803 24.9529 23.8983 25.1987 23.1944 25.3595C22.53 25.5112 22.0102 25.5419 21.5426 25.4426L20.919 28.377C21.9736 28.6011 22.9697 28.4881 23.8624 28.2842C24.7157 28.0893 25.6321 27.7676 26.3949 27.5306L25.5048 24.6657ZM28.6071 23.6841C27.6127 23.9809 26.4766 24.3637 25.5048 24.6657L26.3949 27.5306C27.5067 27.1852 28.4539 26.8606 29.4652 26.5587L28.6071 23.6841ZM25.9096 4.12818C26.8297 3.89755 28.0237 3.6208 29.1048 3.5298L28.8532 0.540372C27.5086 0.653544 26.1088 0.985419 25.1802 1.21822L25.9096 4.12818ZM22.1205 5.61376C23.5724 4.99213 24.8352 4.39752 25.9096 4.12818L25.1802 1.21822C23.8024 1.56359 22.205 2.31417 20.9397 2.85592L22.1205 5.61376ZM29.3462 3.92033V22.8269H32.3462V3.92033H29.3462ZM29.1048 3.5298C29.1506 3.52595 29.1716 3.53329 29.1796 3.53644C29.1898 3.54048 29.2079 3.54995 29.2311 3.57453C29.2818 3.62827 29.3462 3.74669 29.3462 3.92033H32.3462C32.3462 2.19451 31.02 0.358001 28.8532 0.540372L29.1048 3.5298ZM29.4652 26.5587C31.0619 26.0821 32.3462 24.6381 32.3462 22.8269H29.3462C29.3462 23.1418 29.1035 23.5359 28.6071 23.6841L29.4652 26.5587ZM11.2718 3.55982L20.5707 5.74753L21.2577 2.82726L11.9589 0.639548L11.2718 3.55982ZM21.5743 25.4497L12.1768 23.2387L11.4897 26.159L20.8873 28.3699L21.5743 25.4497ZM20.9397 2.85592C21.0446 2.81099 21.1564 2.80342 21.2577 2.82726L20.5707 5.74753C21.0835 5.86819 21.627 5.82507 22.1205 5.61376L20.9397 2.85592ZM11.7291 26.1584C11.64 26.1786 11.5578 26.175 11.4897 26.159L12.1768 23.2387C11.8218 23.1552 11.4413 23.1474 11.0646 23.2329L11.7291 26.1584Z" fill="#404143"/>
									<path d="M21.5996 27L12.522 24.8473C12.3505 24.8066 12.1752 24.7847 12 24.7835V2.28514C12 2.18898 12.0061 2.09377 12.018 2L20.8572 4.09614C21.1068 4.15535 21.3631 4.17348 21.6154 4.15054V26.7312C21.6154 26.8216 21.61 26.9114 21.5996 27Z" stroke="#404143" stroke-width="3" stroke-linejoin="round"/>
									</svg>
	      					Haqqulobod shahri, Namangan viloyati
	      				</span>
	      			</a>
	      		</li>
	      		<li>
	      			<a>
	      				<span>
	      					<svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16">
									  <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
									</svg>
	      					+99 893 123 45 67 
	      				</span>
	      			</a>
	      		</li>
	      		<li>
	      			<a>
	      				<span>
	      					<svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
									  <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"/>
									  <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"/>
									</svg>
	      					Ish vaqti : Dush-Jum 08:00-17:00
	      				</span>
	      			</a>
	      		</li>
	      		<li>
	      			<a>
	      				<span>
	      					<svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
									  <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/>
									</svg>
	      					minoshopuz@yandex.com
	      				</span>
	      			</a>
	      		</li>
	      		<li>
	      			<a>
	      				<span>
	      					<img src="@/assets/img/Facebook.png" alt="Facebook">
	      					Facebok
	      				</span>
	      			</a>
	      			<a>
	      				<span>
	      					<img src="@/assets/img/instagram.png" alt="Instagram">
	      					Instagram
	      				</span>
	      			</a>
	      			<a>
	      				<span>
	      					<img src="@/assets/img/telegram.png" alt="Telegram">
	      					Telegram
	      				</span>
	      			</a>
	      		</li>
	      	</ul>
	      </div>
	    </div>
	  </div>
	</div>
  </section>
</template>
<script>
export default{
	name:"ContactForm"
}
</script>
<style>
	.section_contact_form{
		margin-top: 30px;
		margin-bottom: 40px;
	}
	.contact_form_blocks{
		display: flex;
		flex-wrap: wrap;
	}
	.contact_form_block{
		width: 60%;
		padding-right:40px;
	}
	.contact_block{
		width: 40%;
	}
	.inputs_blocks{
		display: flex;
	}
	.inpu_block{
		padding:0px 15px 15px 0px;
	}
	.contact_block{
		padding-bottom: 87px;
	}
	.contact_items{
		height: 100%;	
		background: #FFFFFF;
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
		transition-property: box-shadow;
		transition-duration: 0.2s;
		transition-timing-function: ease-in;
		padding:10px 20px;
	}
	.contact_items:hover{
		-webkit-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		-moz-box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
		box-shadow: 0px 48px 100px -21px rgba(34, 60, 80, 0.2);
	}
	.contact_items ul {
		height: 100%;
		display: flex;
		flex-direction: column;
		font-size:22px;
		font-family: poppins;
	}
	.contact_items ul li{
		height: 100%;
	}
	.contact_items ul li a{
		display: block;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: space-between;
	}
	.contact_items ul li:last-child{
		display: flex;
		justify-content: space-between;
	}
	.contact_items ul li:last-child a{
		flex-grow: 1;
	}	
	.contact_items ul li a span svg,.contact_items ul li a span img{
		width: 25px;
		margin-right:10px;
		transform: translateY(5px);
	}
	.contact_items ul li a span img{
		margin-right: 5px;
	}
	.contact_form_submit{
		padding:20px 0px 0px 0px;
	}
	.contact_form_submit input {
		display: inline-block;
		font-family: poppins-bold;
		font-size:20px;
		background-color:#FFD600;
		padding:10px 0px;
		border-radius: 10px;
		width: 270px;
		border: none;
	}
	@media(max-width: 1400px){
		.contact_items ul{
			font-size: 18px;
		}
	}
	@media(max-width: 1200px){
		.inputs_blocks{
			flex-direction: column;
		}
		.contact_form_block{
			width: 50%;
			padding-right:20px;
		}
		.contact_block{
			width: 50%;
		}
	}
	@media(max-width: 992px){
		.contact_form_blocks{
			flex-direction: column;
		}
		.contact_form_block{
			width: 100%;
			padding-right:0px;
		}
		.contact_block{
			width: 100%;
			height: auto;
			padding: 10px;
		}
		.inpu_block{
			padding:5px 10px;
		}
		.contact_items ul li a{
			height: auto;
			padding:10px 0px;
		}
		.contact_form_submit{
			padding: 20px 10px;
		}
	}
	@media(max-width: 576px){
		.contact_items ul li:last-child{
			flex-direction: column;
		}
		.contact_items ul{
			font-size: 16px;
		}
	}
	@media(max-width: 400px){
		.contact_items ul{
			font-size: 14px;
		}
		.contact_items ul li a{
			padding:7px 0px;
		}
		.contact_form_submit input {
			font-size:18px;
			width: 250px;
		}
	}
</style>