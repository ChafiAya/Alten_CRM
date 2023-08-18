<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <div class="column is-6">
          <h2 class="subtitle">MyTasks</h2>

          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>name</th>
                <th>description</th>
                <th>end_date</th>
                <th>status</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="task in tasks" :key="task.id">
                <td>{{ task.name }}</td>
                <td>{{ task.description }}</td>
                <th>{{ task.end_date }}</th>
                <th>{{ task.status }}</th>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MyTasks",
  data() {
    return {
      tasks: []
    };
  },
  mounted() {
    this.getTasks();
  },
  methods: {
    async getTasks() {
      this.$store.commit("setIsLoading", true);
      try {
        // Fetch the tasks assigned to the logged-in user
        const tasksResponse = await axios.get("/api/v1/get_my_tasks/");
        console.log("Tasks Response:", tasksResponse.data);

        this.tasks = tasksResponse.data;
      } catch (error) {
        console.log("Error:", error);
      }

      this.$store.commit("setIsLoading", false);
    }
  }
};
</script>

<style scoped>
</style>
