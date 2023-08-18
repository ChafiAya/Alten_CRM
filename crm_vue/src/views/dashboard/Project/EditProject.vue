<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit: {{project.project_name}}</h1>
      </div>
    <div class="column is-12">

      <form @submit.prevent = "submitForm">
        <div class="field">
          <label>Project Name</label>
          <div class="control">
            <input type="text" class="input" v-model="project.project_name">

          </div>
        </div>

        <div class="field">
          <label>Status</label>
          <div class="control">
            <div class="select">
              <select v-model="project.project_status">
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
              <select v-model="project.priority">
                <option value="medium">Medium</option>
                <option value="high">High</option>
                <option value="low">Low</option>
              </select>
            </div>
          </div>
        </div>

        <div class="field">
          <label>Start Date</label>
          <div class="control">
            <input type="date" class="input" v-model="project.start_date">

          </div>
        </div>

        <div class="field">
          <label>End Date</label>
          <div class="control">
            <input type="date" class="input" v-model="project.end_date">

          </div>
        </div>

    <div class="field">
    <label>Assigned to</label>
    <div class="control">
        <div class="select">
            <select v-model="project.assigned_to">
                <option value="" selected>Select member</option>
                <option
                    v-for="member in team.members"
                    v-bind:key="member.id"
                    v-bind:value="member.id"
                >
                    {{ member.username }}
                </option>
            </select>
        </div>
    </div>
</div>

<!-- Client Select -->
<div class="field">
  <label>Client</label>
  <div class="control">
    <div class="select">
      <select v-model="selectedClientId" :value.sync="selectedClientId" v-if="clients && clients.length > 0">
        <option value="" selected>Select client</option>
        <option v-for="client in clients" :key="client.id" :value="client.id">
          {{ client.name }}
        </option>
      </select>
    </div>
  </div>
</div>


        <div class="field">
          <label>Description</label>
          <div class="control">
            <input type="text" class="input" v-model="project.project_description">

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
  name: "EditProject",
  data() {
  return {
    project: {},
    clients:[],
    team: {
      members: []
    },
    selectedClientId: null,
   
  };
},


mounted() {
  this.getTeam(); // First, fetch the team members
  this.getClients(); // Then fetch the clients
  this.getProjects(); // Finally, fetch the project data and set values
},
methods: {
  async getProjects() {
    this.$store.commit('setIsLoading', true);

    const projectID = this.$route.params.id;
    try {
      const response = await axios.get(`/api/v1/projects/${projectID}/`);
      this.project = response.data;

      // Wait until the team members are fetched before setting the supervisor value
      if (this.team.members.length > 0) {
        this.project.assigned_to = this.team.members[0].id;
      }

      // Set Client value
      this.selectedClientId = this.project.client ? this.project.client.id : '';
    } catch (error) {
      console.log(error);
    }

    this.$store.commit('setIsLoading', false);
  },
    async submitForm() {
    this.$store.commit('setIsLoading', true)
    const projectID = this.$route.params.id

    // Extract the client_id from the project object
    const clientID = this.selectedClientId;

    // Create a new object containing only the necessary data
    const requestData = {
      project_name: this.project.project_name,
      project_status: this.project.project_status,
      priority: this.project.priority,
      start_date: this.project.start_date,
      end_date: this.project.end_date,
      assigned_to: this.project.assigned_to,
      project_description: this.project.project_description,
      client: clientID,
    };

    axios
      .patch(`/api/v1/projects/${projectID}/`, requestData)
      .then((response) => {
        toast({
          message: 'successful update',
          type: 'is-success',
          dismissible: true,
          pauseOnHover: true,
          duration: 4000,
          position: 'top-center',
        });

        this.$router.push(`/dashboard/projects/${projectID}/`);
      })
      .catch((error) => {
        console.log(error);
      });

    this.$store.commit('setIsLoading', false);
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