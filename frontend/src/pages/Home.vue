<template>
  <div>
    <Navbar :label="userInfo.label" :image="userInfo.image" />
    <div class="px-20 py-2">
      <div>
        <h2 class="font-bold text-3xl mt-5 text-gray-600 mb-4">
          Hi, {{ userInfo?.name ?? 'Guest' }}!
        </h2>
        <p class="text-gray-600 font-semibold">
          Welcome to Nepal Government Service Portal
        </p>
      </div>
      <div class="mt-20">
            <Tabs
            v-model="state.index"
            :tabs="contents"
            >
            <template #default="{ tab }">
              <div class="p-5">
                {{ tab.content }}
              </div>
            </template>
        </Tabs>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { onMounted, ref,h } from 'vue';
import Navbar from '../components/Navbar.vue';
import { user_info } from '../data/user';
import { Tabs,FeatherIcon } from 'frappe-ui';

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

const contents = ref([
  {
    label: 'Electricity',
    content: 'Dashboard content goes here',
    icon: h(FeatherIcon, { class: 'w-4 h-4', name: 'activity' }),
  },
  {
    label: 'Water',
    content: 'Profile content goes here',
    icon: h(FeatherIcon, { class: 'w-4 h-4', name: 'droplet' }),
  },
  {
    label: 'Gas',
    content: 'Settings content goes here',
    icon: h(FeatherIcon, { class: 'w-4 h-4', name: 'wind' }),
  },
]);
</script>