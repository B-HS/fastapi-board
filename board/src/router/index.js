import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import write from '../views/WritePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/write',
    name: 'write',
    component: write
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
