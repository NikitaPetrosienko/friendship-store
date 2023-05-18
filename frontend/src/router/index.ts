// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'HomePage',
        component: () => import('@/views/HomePage.vue'),
      },
    ],
  },
  {
    path: '/aboutus',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'AboutUsPage',
        component: () => import('@/views/AboutUsPage.vue'),
      },
    ],
  },
  {
    path: '/product/:id',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'ProductPage',
        component: () => import('@/views/ProductPage.vue'),
      },
    ],
  },
  {
    path: '/cart',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'CartPage',
        component: () => import('@/views/CartPage.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
