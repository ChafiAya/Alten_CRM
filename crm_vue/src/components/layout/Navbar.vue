<template>
  <nav>
    <div class="title">
     Alten<br>CRM
    </div>
    <div class="menu-items">
      <template v-if="$store.state.isAuthenticated">
        <router-link
          to="/dashboard/leads"
          tag="button"
          exact
          class="side-btn "
          active-class="active"
        >
          Leads
        </router-link>
        <router-link
          to="/dashboard/clients"
          tag="button"
          class="side-btn"
          active-class="active"
        >
          Clients
        </router-link>
        <router-link
          to="/dashboard/team"
          tag="button"
          class="side-btn"
          active-class="active"
        >
          Team
        </router-link>
        <router-link
          to="/dashboard/projects"
          tag="button"
          class="side-btn"
          active-class="active"
        >
          Projects
        </router-link>
       
      </template>

      <div class="buttons">
        <template v-if="!$store.state.isAuthenticated">
          <router-link to="/sign-up" class="button is-primary" active-class="active">
            <strong>Sign up</strong>
          </router-link>
          <router-link to="/log-in" class="button is-light" active-class="active">
            Log in
          </router-link>
        </template>

        <template v-else>
          <router-link
    :to="'/dashboard/my-account/' + $store.state.user.id" 
    class="side-btn"
    active-class="active"
  >
    My account
  </router-link>
      
        </template>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
/* Navbar styles */
nav {
  background-color: teal;

}

.title {
  color: white;
  font-size: 24px;
  margin-bottom: 10px;
}

.menu-items {
  display: flex;
  flex-direction: column;
  margin-top: 200px;
 
}

.menu-items > * {
  margin-top: 0px; /* Adjust the spacing between menu items */
}

/* Sidebar button styles */
.side-btn {
  border: none;
  padding: 20px 50px; /* Adjust button padding */
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  color: rgb(255, 255, 255);
  background-color: transparent;
  transition: background-color 0.3s;
  position: relative;
  flex:1;
  margin-bottom:8px;
}

.side-btn.active {
  background-color: white;
  color: teal;
  font-weight: 600;
  border-radius: 0px 30 30 0px;
}
body {
  margin: 0;
}
.side-btn.active::before,
.side-btn.active::after {
  content: "";
  position: absolute;
  height: 60px;
  width: 60px;
  border-radius: 50%;
  background-color: rgb(255, 255, 255);
  z-index: -1; /* Add this to position the circles behind the active button */
  opacity: 0; /* Add this to make the circles initially invisible */
  transform: scale(0); /* Add this to make the circles initially small */
  transition: transform 0.3s, opacity 0.3s; /* Add transitions for smooth animation */
}
.side-btn.active::before {
  top: 30px;
 
}

.side-btn.active::after {
  bottom: 30px;
}

/* Loading animation styles */
.is-loading-bar {
  height: 0;
  overflow: hidden;
  transition: height 0.3s;
}

.is-loading-bar.is-loading {
  height: 80px;
}

.is-loading-bar .lds-dual-ring {
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px auto;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Other styles */
.app-container {
  display: grid;
  grid-template-columns: 1fr 5fr;
  background-color: teal;
  height: 100vh;
  width: 100vw;
}

.dashboard {
  background-color: white;
  border-radius: 20px;
 
}

/* Button color on hover */
.side-btn:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

</style>