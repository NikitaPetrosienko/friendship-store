// Composables
import { createRouter, createWebHistory } from 'vue-router'

const authGuard = function (to, from, next) {
  const isUserLoggedIn = localStorage.getItem('token');
  if (!isUserLoggedIn) next ({ name: 'LoginPage'});
  else next();
}

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'HomePage',
        component: () => import('@/views/HomePage.vue'),
        children: [
          {
            path: '',
            name: 'HomePageBrands',
            component: () => import('@/components/home-page/HomePageBrands.vue'),
          },
          {
            path: '/products/:category?:brand?',
            name: 'HomePageProducts',
            component: () => import('@/components/home-page/HomePageProducts.vue'),
          },
        ],
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
    path: '/albums',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'AlbumsPage',
        component: () => import('@/views/AlbumsPage.vue'),
      },
    ],
  },
  {
    path: '/news/:id',
    component: () => import('@/layouts/Default.vue'),
    children: [
      {
        path: '',
        name: 'NewsPage',
        component: () => import('@/views/NewsPage.vue'),
      },
    ],
  },
  {
    path: '/product/:category/:id',
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
        children: [
          {
            path: '',
            name: 'CartPageTable',
            component: () => import('@/components/cart-page/CartPageTable.vue'),
          },
          {
            path: '/form',
            name: 'CartPageForm',
            component: () => import('@/components/cart-page/CartPageForm.vue'),
          },
          {
            path: '/make-order',
            name: 'CartPageMakeOrder',
            component: () => import('@/components/cart-page/CartPageMakeOrder.vue'),
          },
        ],
      },
    ],
  },
  {
    path: '/favourites',
    component: () => import('@/layouts/Default.vue'),
    beforeEnter: authGuard,
    children: [
      {
        path: '',
        name: 'FavouritesPage',
        component: () => import('@/views/FavouritesPage.vue'),
        beforeEnter: authGuard,
      },
    ],
  },
  {
    path: '/login',
    component: () => import('@/layouts/Empty.vue'),
    children: [
      {
        path: '',
        name: 'LoginPage',
        component: () => import('@/views/LoginPage.vue'),
      },
    ],
  },
  {
    path: '/register',
    component: () => import('@/layouts/Empty.vue'),
    children: [
      {
        path: '',
        name: 'RegisterPage',
        component: () => import('@/views/RegisterPage.vue'),
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
      if (to.hash) {
        return {
          el: to.hash,
          behavior: 'smooth',
        };
      } else if (savedPosition) {
        return savedPosition;
      } else {
        return { top: 0 };
      }
    },
})

export default router
