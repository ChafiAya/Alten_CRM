<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ project.project_name }}</h1>
      
        <div class="buttons">
          <router-link v-if="project.id" :to="{ name: 'EditProject', params: { id: project.id }}"
                       class="button is-light">
                       Edit Project
          </router-link>
          <button @click="deleteProject" class="button is-danger">Delete Project</button>
        </div>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Project</h2>

          <template v-if="project.assigned_to">
            <p><strong>Full Name:</strong> {{ project.assigned_to.first_name }} {{ project.assigned_to.last_name }}</p>
          </template>
          <p><strong>Status:</strong> {{ project.project_status }}</p>
          <p><strong>Priority:</strong> {{ project.priority }}</p>
          <p><strong>Start Date:</strong> {{ project.start_date }}</p>
          <p><strong>End Date:</strong> {{ project.end_date }}</p>
          <template v-if="project.client">
            <p><strong>Client:</strong> {{ project.client.name }}</p>
          </template>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Description</h2>
          <p>{{ project.project_description }}</p>

        </div>
      </div>

      <hr>
      <div class="column is-12">
        <h2 class="subtitle">Tasks</h2>

        <router-link v-if="project.id" :to="{ name: 'AddTask', params:{id: project.id}}" class="button is-success mb-6">
          AddTask
        </router-link>

        <div
            class="box"
            v-for="task in tasks"
            v-bind:key="task.id">
          <h3 class="is-size-4">{{ task.name }}</h3>

          <strong>description : </strong><p>{{ task.description }}</p>
         <strong>employee: </strong> <p>{{task.member.first_name}} {{task.member.last_name}} {{task.member.username}}</p>
          <strong>status: </strong> <p>{{task.status}}</p>
          <strong>start_date: </strong> <p>{{task.start_date }}</p>
          <strong>end_date: </strong> <p>{{task.end_date}}</p>
            <router-link v-if="project.id" :to="{ name: 'EditTask', params:{id: project.id, task_id: task.id}}"
                         class="button is-light mt-6">EditTask
            </router-link>
            &nbsp;
            <router-link v-if="project.id" :to="{ name: 'Task', params:{id: project.id, task_id: task.id}}"
                         class="button is-info mt-6">Task
            </router-link>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  name: "Project",
  data() {
    return {
      project: {},
      client: {},
      tasks: []
    }

  },
  mounted() {
    this.getProject();
  },
  methods: {
    async deleteProject() {
      this.$store.commit('setIsLoading', true);
      const projectID = this.$route.params.id;
      await axios
        .post(`/api/v1/projects/delete_project/${projectID}/`)
        .then(response => {
          toast({
            message: 'Project deleted',
            type: 'is-success',
            dismissible: true,
            pauseOnHover: true,
            duration: 4000,
            position: 'top-center',
          });
          console.log(response.data);
          this.$router.push('/dashboard/projects');
        })
        .catch(error => {
          console.log(error);
        });
      this.$store.commit('setIsLoading', false);
    },


    
    async getProject() {
      this.$store.commit("setIsLoading", true);

      const projectID = this.$route.params.id;
      await axios
        .get(`/api/v1/projects/${projectID}`)
        .then((response) => {
          this.project = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      // Check if the logged-in user is the creator of the team associated with the project
      const isTeamCreator = this.project.team && this.$store.state.user.id === this.project.team.created_by.id;

      // Check if the logged-in user is assigned to the project
      const isAssignedToProject = this.$store.state.user.id === this.project.assigned_to.id;

      // Fetch all tasks for the project if the user is the team creator or is assigned to the project
      if (isTeamCreator || isAssignedToProject) {
        await axios
          .get(`/api/v1/tasks/?project_id=${projectID}`)
          .then((response) => {
            this.tasks = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
             // Fetch tasks where the logged-in user is assigned
      await axios
        .get(`/api/v1/tasks/?project_id=${projectID}`)
        .then((response) => {
          // Filter tasks where the logged-in user is the member
          this.tasks = response.data.filter(
            (task) => task.member.id === this.$store.state.user.id
          );
        })
          .catch((error) => {
            console.log(error);
          });
      }

      this.$store.commit("setIsLoading", false);
    }

  }
  
}
</script>

<style scoped>

</style>