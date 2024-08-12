<template>
    <ListView
        class="h-[150px]"
        :columns="columns"
        :rows="rows"
        :options="options"

        row-key="id"
/>
</template>

<script setup>
import { ListView } from 'frappe-ui';

const columns = [
  {
    label: 'NEA Bill ID',
    key: 'billID',
   
  },
  {
    label: 'Status',
    key: 'status',
   
  },
  {
    label: 'Usage',
    key: 'usage',
   
  },
  {
    label: 'Rate',
    key: 'rate',
   
  },
  {
    label: 'Amount',
    key: 'amount',
  
  },
  {
    label: 'Action',
    key: 'action',
   
  },
  
];


const options = {
    selectable: false,
      showTooltip: true,
      resizeColumn: true,
      emptyState: {
        title: 'No records found',
        
       
      }
}


</script>