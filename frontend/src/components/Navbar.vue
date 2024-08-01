<template>
    <nav class="bg-white px-20 py-2 shadow-md ">
        <div class="flex justify-between items-center">
            <h1 class="cursor-pointer">
                <router-link to="/" class="text-gray-700 ">Nepal Government Service</router-link>
            </h1>
            <Dropdown :options="options">
                <Avatar class="cursor-pointer"
                        :shape="'square'"
                        :image="image || 'https://i.pravatar.cc/100'"
                        :label="label || 'G'"
                        size="md"
                />
            </Dropdown>
        </div>
    </nav>
</template>

<script setup>
import { Dropdown, FeatherIcon, Avatar } from 'frappe-ui';
import { ref, h } from 'vue';

const options = ref([
    {
        label: 'Support',
        onClick: () => {
            console.log('Support clicked');
        },
        icon: () => h(FeatherIcon, { name: "headphones" }),
    },
    {
        label: 'Feedback',
        onClick: () => {
            console.log('Feedback clicked');
        },
        icon: () => h(FeatherIcon, { name: "meh" }),
    },
    {
        label: 'Logout',
        onClick: () => {
            console.log('Logout clicked');
        },
        icon: () => h(FeatherIcon, { name: "log-out" }),
    },
]);

const props = defineProps({
    label: String,
    image: String
});
</script>