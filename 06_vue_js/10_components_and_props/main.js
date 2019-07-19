Vue.component("comment", {
    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    template: `
        <div>
            <div class="card-body">
                <p>{{ comment.username }}</p>
                <p>{{ comment.content }}</p>
            </div>
        </div>
    `
})

var app = new Vue({
    el: "#app",
    data: {
        comments: [
            {
                username: "pusinsky",
                content: "la vida es bella"
            },
            {
                username: "weimar",
                content: "que gonorrea ome"
            },
            {
                username: "Yajaira",
                content: "q' hubo pirovo"
            },
            {
                username: "Laura",
                content: "ay usted tan guache"
            },
        ]
    },
})