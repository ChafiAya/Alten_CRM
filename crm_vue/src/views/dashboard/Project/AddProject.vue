<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Project</h1>
      </div>

      <div class="column is-6">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label>Title</label>
            <div class="control">
              <input type="text" class="input" v-model="project_name">

            </div>
          </div>

          <div class="field">
            <label>Status</label>
            <div class="control">
              <div class="select">
                <select v-model="project_status">
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
            <label>Priority</label>
            <div class="control">
              <div class="select">
                <select v-model="priority">
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                  <option value="low">Low</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <label>Start date</label>
            <div class="control">
              <input type="date" class="input" v-model="start_date">

            </div>
          </div>

          <div class="field">
            <label>End date</label>
            <div class="control">
              <input type="date" class="input" v-model="end_date">

            </div>
          </div>

          <div class="field">
            <label>assigned to</label>
            <div class="control">
              <div class="select">
                <select v-model="assigned_to">
                  <option value="" selected>Select member</option>
                  <option
                  v-for="member in team.members"
                  v-bind:key="member.id"
                  v-bind:value="member.id"
                >{{ member.username }}</option>

                </select>
              </div>
            </div>
          </div>


          <div class="field">
  <label>Client</label>
  <div class="control">
    <div class="select">
      <select v-if="clients && clients.length > 0" v-model="client">
        <option value="" selected>Select client</option>
        <option
          v-for="client in clients"
          v-bind:key="client.id"
          v-bind:value="client.id"
        >{{ client.name }}</option>
      </select>
      <span v-else>No clients available</span>
    </div>
  </div>
</div>


<div class="field">
  <label>Description</label>
  <div class="control">
    <textarea class="textarea" v-model="project_description"></textarea>
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

export default {
  name: "AddProject",
  data() {
    return {
      project_name: '',
      project_status: 'new',
      priority: 'medium',
      start_date: '',
      end_date: '',
      client: '',
      project_description: '',
      assigned_to: '',


      clients: [],
      team: {
                    members: []
                }
    }
  },
  mounted() {
    this.getTeam()
    this.getClients()
  },
  methods: {
    async submitForm() {
      this.$store.commit('setIsLoading', true)
      console.log('submit form')
      const project = {
        project_name: this.project_name,
        project_status: this.project_status,
        priority: this.priority,
        start_date: this.start_date,
        end_date: this.end_date,
        client: this.client,
        assigned_to: this.assigned_to,
        project_description: this.project_description
      }
      await axios
          .post('/api/v1/projects/', project)
          .then(response => {
            toast({
              message: 'add success',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 4000,
              position: 'top-center',
            })

            console.log(response)
            this.$router.push('/dashboard/projects')
          })

          .catch(error => {
            console.log(error.response.data)
          })

      this.$store.commit('setIsLoading', false)
    },

    async getTeam() {
                this.$store.commit('setIsLoading', true)

                await axios
                    .get('/api/v1/teams/get_my_team/')
                    .then(response => {
                        this.team = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                this.$store.commit('setIsLoading', false)
     },

     async getClients() {
  this.$store.commit('setIsLoading', true);
  try {
    const response = await axios.get('/api/v1/clients/');
    console.log('API Response:', response.data); // Check the response data
    this.clients = response.data.results; // Make sure you're assigning the correct property from the API response
  } catch (error) {
    console.error('Error fetching clients:', error);
  }
  this.$store.commit('setIsLoading', false);
}
  }
}
</script>

<style scoped>

</style>