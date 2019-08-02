<template>
  <div class="example">
    <h1>Este es un ejemplo de componente!</h1>
    <h3>{{ message }}</h3>
  </div>
</template>

<script>
export default {
    name: "example",
    data() {
        return {
            message: "Hello world!!"
        }
    }
}
</script>


<style scoped>
h1 {
    color: red;
}
</style>
