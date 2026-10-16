<template>
  <section class="course-module">
    <p class="module-kicker">常见报错速查</p>
    <table>
      <thead>
        <tr>
          <th>看到什么</th>
          <th>原因</th>
          <th>先做什么</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" :key="index">
          <td>{{ row.symptom }}</td>
          <td>{{ row.cause }}</td>
          <td>{{ row.fix }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup>
defineProps({
  rows: { type: Array, default: () => [] }
})
</script>

<style scoped>
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { border-bottom: 1px solid var(--vp-c-divider); padding: 8px 10px; text-align: left; vertical-align: top; }
th { font-size: 13px; }
</style>
