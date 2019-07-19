Vue.component("task-list", {
    props: {
        tasks: {
            type: Array,
            required: true
        },
    },
    data: function () {
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
                this.error = "Ingrese una nueva tarea!";
            }
        }
    },
    template: `
        <div class="mt-2">
            <div class="container">
                <h3>{{ error }}</h3>
                <form @submit.prevent="submitTask" class="mb-3">
                    <div class="form-group">
                        <label for="newTask">Añada una nueva tarea</label>
                        <input class="form-control" id="newTask" type="text"
                                v-model="new_task">
                        </input>
                    </div>
                    <button class="btn btn-sm btn-primary" type="submit">
                        Añadir
                    </button>
                </form>
                <hr>
                <single-task v-for="(task, index) in tasks" :task="task" 
                        :key="index">
                </single-task>
            </div>
        </div>
    `
})

Vue.component("single-task", {
    props: {
        task: {
            type: String,
            required: true
        }
    },
    template: `
        <div class="mb-2">
            <div class="container">
                <div class="alert alert-success alert-dismissible fade 
                        show w-50" role="alert">
                    <strong>{{ task }}</strong> 
                    <button type="button" class="btn close" data-dismiss="alert" 
                            aria-label="Close"> 
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
    methods: {
        addNewTask(new_task) {
            this.tasks.push(new_task);
        }
    },
})