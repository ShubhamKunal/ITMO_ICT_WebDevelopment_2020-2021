import Vue from 'vue'
import VueRouter from 'vue-router'

// импортируем все представления, по
// которым будем навигировать пользователя
import Greeting from '@/views/Greeting.vue'
import MainPage from '@/views/MainPage.vue'
import Classes from '@/views/Classes.vue'
import Prices from '@/views/Prices.vue'
import Timetable from '@/views/Timetable.vue'

Vue.use(VueRouter)

// заводим массив с роутами
const routes = [
  {
    path: '/greet',
    name: 'Greeting',
    component: Greeting
  },
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/classes',
    name: 'Classes',
    component: Classes
  },
  {
    path: '/prices',
    name: 'Prices',
    component: Prices
  },
  {
    path: '/timetable',
    name: 'Timetable',
    component: Timetable
  }
]

// создаём новый экземпляр класса
// VueRouter, с необходимыми параметрами
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// экспортируем сконфигурированный роутер
export default router
