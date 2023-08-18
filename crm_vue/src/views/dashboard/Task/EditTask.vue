<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit Task: {{task.name}}</h1>
      </div>
      <div class="column is-8">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Name</label>
            <div class="control">
              <input type="text" class="input" v-model="task.name">

            </div>
          </div>

          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="task.status">
                  <option value="new">New</option>
                  <option value="inprogress">In progress</option>
                  <option value="cancelled">Cancelled</option>
                  <option value="finished">Finished</option>
                  <option value="frozen">Frozen</option>
                </select>
              </div>


            </div>
          </div>


          <div class="field">
            <label>Start date</label>
            <div class="control">
              <input type="date" class="input" v-model="task.start_date">

            </div>
          </div>

          <div class="field">
            <label>End date</label>
            <div class="control">
              <input type="date" class="input" v-model="task.end_date">

            </div>
          </div>


          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea class="textarea" v-model="task.description"></textarea>

            </div>
          </div>


          <div class="field">
            <label>Member</label>
            <div class="control">
              <div class="select">
                <select v-model="task.member">
                  <option value="" selected>Select member</option>
                  <option
                      v-for="member in team.members"
                      v-bind:key="member.id"
                      v-bind:value="member.id"
                  >{{ member.username }}
                  </option>
                </select>
              </div>
            </div>
          </div>

          <div class='field'>
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>


        </form>

      </div>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "EditTask",
  data() {
    return {
      task: {},
      team: {
        members: [],
      },
    };
  },
  mounted() {
    this.getTask(); // Renamed from getTasks() to getTask() to fetch a single task
    this.getDepartment();
  },
  methods: {
    async getTask() {
      this.$store.commit('setIsLoading', true);
      const taskID = this.$route.params.task_id;
      const projectID = this.$route.params.id;

      axios
        .get(`/api/v1/tasks/${taskID}/?project_id=${projectID}`)
        .then((response) => {
          this.task = response.data;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.$store.commit('setIsLoading', false);
        });
    },
    async submitForm() {
      this.$store.commit('setIsLoading', true);
      const projectID = this.$route.params.id;

      axios
        .patch(`/api/v1/tasks/${this.task.id}/?project_id=${projectID}`, this.task) // Pass the task object as the request data
        .then((response) => {
          toast({
            message: 'task updated successfuly',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 4000,
            position: 'top-center',
          });

          this.$router.push({ name: 'Project', params: { id: this.$route.params.id } });
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.$store.commit('setIsLoading', false);
        });
    },
    async getDepartment() {
      this.$store.commit('setIsLoading', true);
      await axios
        .get('/api/v1/teams/get_my_team/')
        .then((response) => {
          this.team= response.data;
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.$store.commit('setIsLoading', false);
        });
    },
  },
};
</script>

<style scoped>

</style>