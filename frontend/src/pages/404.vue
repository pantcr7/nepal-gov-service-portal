<template>
    <div class="overflow-hidden h-screen">
      <Navbar :label="userInfo.label" :image="userInfo.image" />
      <div class="container h-full">
        <div class="flex justify-center items-center h-full">
          <div class="text-center">
            <h1 class="text-xl font-bold text-gray-800">404</h1>
            <p class="text-gray-500">Page not found</p>
            <p class="text-gray-500 text-sm">Nepal Government Service </p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  html, body {
    height: 100%;
    margin: 0;
    overflow: hidden;
  }
  </style>
  
  <script setup>
  import { onMounted, ref, h } from 'vue';
  import Navbar from '../components/Navbar.vue';
  import { user_info } from '../data/user';
 

 
  
  const userInfo = ref({
    name: 'Guest',
    image: 'https://i.pravatar.cc/100',
    label: 'G'
  });
  
  const state = ref({
    index: 0
  });
  
  const fetchUserInfo = async () => {
    try {
      const data = await user_info();
     
      if (data.message && data.message.user_info) {
        userInfo.value.name = data.message.user_info.name;
        userInfo.value.image = data.message.user_info.user_image;
        userInfo.value.label = data.message.user_info.name[0];
      }
    } catch (error) {
      console.error('Error fetching user info:', error);
    }
  };
  
  onMounted(() => {
    fetchUserInfo();
  });

  </script>