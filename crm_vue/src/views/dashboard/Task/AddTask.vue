<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add a Task</h1>
      </div>

      <div class="column is-6">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Task name</label>
            <div class="control">
              <input type="text" class="input" v-model="name">

            </div>
          </div>

          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
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
            <label>start_date</label>
            <div class="control">
              <input type="date" class="input" v-model="start_date">

            </div>
          </div>

          <div class="field">
            <label>end_date</label>
            <div class="control">
              <input type="date" class="input" v-model="end_date">

            </div>
          </div>


          <div class="field">
            <label>Description</label>
            <div class="control">
              <textarea class="textarea" v-model="description"></textarea>

            </div>
          </div>

          <div class="field">
            <label>member</label>
            <div class="control">
              <div class="select">
                <select v-model="member">
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
import {toast} from "bulma-toast";
import project from "@/views/dashboard/Project/Project";

export default {
  name: "AddTask",
  data() {
    return {
      name: '',
      status: 'new',
      start_date: '',
      end_date: '',
      description: '',
      member: '',
      team: {
        members: []
      }
    }
  },
  mounted() {
    this.getTeam()
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      console.log('submit form')

      const task = {
        project_id: this.$route.params.id,
        name: this.name,
        status: this.status,
        start_date: this.start_date,
        end_date: this.end_date,
        description: this.description,
        member: this.member
      }
      await axios
          .post('/api/v1/tasks/', task)
          .then(response => {
            toast({
              message: 'Task added successfully',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            console.log(response)
            this.$router.push({name: 'Project', params: {id: this.$route.params.id}})
          })

          .catch(error => {
            console.log(error.response.data)
          })

      this.$store.commit('setIsLoading', false)
    },
    async getTeam() {
  this.$store.commit('setIsLoading', true);
  await axios
      .get('/api/v1/teams/get_my_team/')
      .then(response => {
        this.team = response.data; // Update to this.team = response.data
      })
      .catch(error => {
        console.log(error);
      });
  this.$store.commit('setIsLoading', false);
}

  }
}
</script>

<style scoped>

</style>