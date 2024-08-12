<template>
    <div class="space-y-2">
        <h1>Summary</h1>
        <Summary />
        
        <h1>All Bills</h1>
        <BillsDetails />
    </div>
</template>

<script setup>
import Summary from './chunks/electricity/Summary.vue';
import BillsDetails from './chunks/electricity/BillsDetails.vue';

</script>