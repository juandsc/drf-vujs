Vue.component("task-list", {
    props: {
        tasks: {
            type: Array,
            required: true
        },
        remaining: {
            type: Number,
            required: true
        },
    },
    data () {
        return {
            new_task: null,
            error: null
        }
    },
    methods: {
        submitTask() {
            if (this.new_task) {
                this.$emit("submit-task", this.new_task);
                this.new_task = null;
                this.error = null;
            } else {
                this.error = "El campo no puede estar vacio!";
            }
        },
        removeTask(task) {
            this.$emit("remove-task", task);
        },
    },
    template: `
        <div class="container mt-2">
            <p><strong>Remaining Tasks: {{ remaining }}</strong></p>
            <input type="text"
                    class="form-control"
                    placeholder="Qué necesitas hacer?"
                    v-model="new_task"
                    @keyup.enter="submitTask">
            <br>
            <div class="single-task" 
                    v-for="(task, index) in tasks" 
                    :task="task" 
                    :key="index">
                <div class="alert alert-success">
                    {{ task }}
                    <button type="button" class="close no-outline" @click="removeTask(task)">
                        <span>&times;</span>
                    </button>
                </div>
            </div>
            <p v-if="error">{{ error }}</p>
            <p v-if="remaining === 0">Añade una nueva tarea a tu lista de cosas por hacer!</p>
        </div>
    `
})

Vue.component("single-tas", {
    props: {
        task: {
            type: String,
            required: true
        }
    },
    methods: {
        submitRemoveTask() {
            this.$emit("submit-remove-task", this.key);
        }
    },
    template: `
        <div class="mb-2">
            <div class="container">
                <div class="alert alert-success alert-dismissible fade 
                        show w-50" role="alert">
                    <strong>{{ task }}</strong> 
                    <button type="button" class="btn close" data-dismiss="alert" 
                            aria-label="Close" :click="submitRemoveTask"> 
                        <span aria-hidden="true">×</span> 
                    </button> 
                </div> 
            </div>
        </div>
    `
})

var app = new Vue({
    el: "#app",
    data: {
        tasks: [],
    },
    computed: {
        taskCount() {
            return this.tasks.length;
        }
    },
    methods: {
        addNewTask(new_task) {
            this.tasks.push(new_task);
        },
        removeTask(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1);
        },
    },
})

// `
//     <div class="container mt-2">
//         <p>Tareas sobrantes: {{ remaining }}</p>
//         <h3>{{ error }}</h3>
//         <form @submit.prevent="submitTask" class="mb-3">
//             <div class="form-group">
//                 <label for="newTask">Añada una nueva tarea</label>
//                 <input class="form-control" id="newTask" type="text"
//                         v-model="new_task">
//                 </input>
//             </div>
//             <button class="btn btn-sm btn-primary" type="submit">
//                 Añadir
//             </button>
//         </form>
//         <hr>
//         <single-task v-for="(task, index) in tasks" :task="task" 
//                 :key="index" @submit-remove-task="removeTask">
//         </single-task>
//     </div>
// `