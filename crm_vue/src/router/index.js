import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'

import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Leads from '../views/dashboard/Lead/Leads.vue'
import Lead from '../views/dashboard/Lead/Lead.vue'
import AddLead from '../views/dashboard/Lead/AddLead.vue'
import EditLead from '../views/dashboard/Lead/EditLead.vue'
import AddTeam from '../views/dashboard/Team/AddTeam.vue'
import Team from '../views/dashboard/Team/Team.vue'
import TeamInfo from '../views/dashboard/Team/TeamInfo.vue'
import AddMember from '../views/dashboard/Member/AddMember.vue'
import Clients from '../views/dashboard/Client/Clients.vue'
import AddClient from '../views/dashboard/Client/AddClient.vue'
import Client from '../views/dashboard/Client/Client.vue'
import EditClient from '../views/dashboard/Client/EditClient.vue'
import AddNote from '../views/dashboard/Note/AddNote.vue'
import EditNote from '../views/dashboard/Note/EditNote.vue'
import EditMember from '../views/dashboard/Member/EditMember.vue'

import Plans from '../views/dashboard/Plan/Plans.vue'
import PlansThankyou from '../views/dashboard/Plan/PlansThankyou.vue'
import AddProject from "../views/dashboard/Project/AddProject";
import Projects from "../views/dashboard/Project/Projects";
import Project from "../views/dashboard/Project/Project";
import EditProject from "@/views/dashboard/Project/EditProject";
import AddTask from "@/views/dashboard/Task/AddTask";
import EditTask from "@/views/dashboard/Task/EditTask";
import Task from "@/views/dashboard/Task/Task";
import MyTasks from "@/views/dashboard/Task/MyTasks";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/my-account/:id',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team',
    name: 'Team',
    component: Team,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/:id',
    name: 'TeamInfo',
    component: TeamInfo,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/plans',
    name: 'Plans',
    component: Plans,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/plans/thankyou',
    name: 'PlansThankyou',
    component: PlansThankyou,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/edit-member/:id',
    name: 'EditMember',
    component: EditMember,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/team/add-member',
    name: 'AddMember',
    component: AddMember,
    meta: {
      requireLogin: true
    }
  },
 
  {
    path: '/dashboard/add-team',
    name: 'AddTeam',
    component: AddTeam,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads',
    name: 'Leads',
    component: Leads,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/add',
    name: 'AddLead',
    component: AddLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id',
    name: 'Lead',
    component: Lead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/leads/:id/edit',
    name: 'EditLead',
    component: EditLead,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients',
    name: 'Clients',
    component: Clients,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/add',
    name: 'AddClient',
    component: AddClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id',
    name: 'Client',
    component: Client,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/edit',
    name: 'EditClient',
    component: EditClient,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/add-note',
    name: 'AddNote',
    component: AddNote,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/dashboard/clients/:id/edit-note/:note_id',
    name: 'EditNote',
    component: EditNote,
    meta: {
      requireLogin: true
    }
  },
  
{
    path: '/dashboard/projects/add',
    name: 'AddProject',
    component: AddProject,
    meta: {
        requireLogin: true
    }
},
{
  path: '/dashboard/projects',
  name: 'Projects',
  component: Projects,
  meta: {
      requireLogin: true
  }
},
{
  path: '/dashboard/projects/:id',
  name: 'Project',
  component: Project,
  meta: {
      requireLogin: true
  }
},

{
  path: '/dashboard/projects/:id/edit',
  name: 'EditProject',
  component: EditProject,
  meta: {
      requireLogin: true
  }
},
{
  path: '/dashboard/projects/:id/add-task',
  name: 'AddTask',
  component: AddTask,
  meta: {
      requireLogin: true
  }
},

{
  path: '/dashboard/projects/:id/edit-task/:task_id',
  name: 'EditTask',
  component: EditTask,
  meta: {
      requireLogin: true
  }
},

{
  path: '/dashboard/projects/:id/task/:task_id',
  name: 'Task',
  component: Task,
  meta: {
      requireLogin: true
  }
},

{
  path: '/dashboard/my-tasks',
  name: 'MyTasks',
  component: MyTasks,
  meta: {
      requireLogin: true
  }
},





]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
