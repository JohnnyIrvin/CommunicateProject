<script setup lang="ts">
import Chat from './components/Chat.vue'
</script>

<template lang="pug">
img(alt="Vue logo" src="./assets/logo.png")
Chat(msg="Hello Vue 3 + TypeScript + Vite")
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
