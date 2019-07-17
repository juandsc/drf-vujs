var app = new Vue({
    el: "#app",
    data: {
        color: 'green',
        text: "",
        checked: true,
        city: "",
        comment: null,
        comments: [],
        errors: null,
    },
    methods: {
        onSubmit() {
            if (this.comment) {
                let new_comment = this.comment;
                this.comments.push(new_comment);
                this.comment = null;
                this.errors = null;
            } else {
                this.errors = "El comentario no puede estar vacio";
            }
            
        }
    }
})