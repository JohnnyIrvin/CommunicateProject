<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const connection = new WebSocket("ws://64.225.16.66/ws/commander")
const msg = ref('Hello World')
const messages = ref([] as string[])

connection.onmessage = function(event) {
  messages.value.push(event.data)
}

function sendMessage() {
  connection.send(msg.value)
  msg.value = ""
}
</script>

<template lang="pug">
.div
  .div(v-for="msg in messages")
    p {{ msg }}
.div
  textarea(v-model="msg")
.div
  button(type="button" @click="sendMessage") Send
</template>

<style scoped>
a {
  color: #42b983;
}

label {
  margin: 0 0.5em;
  font-weight: bold;
}

code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}
</style>
