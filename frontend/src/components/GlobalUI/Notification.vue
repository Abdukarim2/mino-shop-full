<template>
    <div class="notification">
        <p>{{$store.state.notificationContent}}</p>
    </div>
</template>
<script>
export default {
    name:"Notification"
}
</script>
<style>
    .notification{
        background-color:#FFD600;
        position: fixed;
        bottom: 10px;
        right: 10px;
        width: 400px;
        max-width: calc(100% - 20px);
        height: auto;
        min-height: 100px;
        padding: 25px 30px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family:poppins;
        color:#fff;
        font-size: 25px;
        text-align: center;
        transform: translateY(80%);
        transition-property: transform opacity;
        transition-duration: 0.5s;
        transition-timing-function: ease;
        opacity: 0;
    }
    .notification_show{
        transform: translateY(0%);
        opacity: 1;
    }
</style>