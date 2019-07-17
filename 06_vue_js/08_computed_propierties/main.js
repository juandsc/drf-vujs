var app = new Vue({
    el: "#app",
    data: {
        firstName: "Jose",
        lastName: "Repelin"
    },
    computed: {
        getRandomComputed() {
            return Math.random();
        },
        fullName() {
            return `${ this.firstName } ${ this.lastName }`;
        },
        reverseFullName() {
            first = this.firstName.split("").reverse().join("");
            last = this.lastName.split("").reverse().join("");
            return `${ first } ${ last }`;
        }
    },
    methods: {
        getRandomNumber() {
            return Math.random();
        }
    },
})