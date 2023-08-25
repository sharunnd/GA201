import { createRouter, createWebHistory } from 'vue-router'
import MenuList from '../components/MenuList'

const routes = [
    {path:'/menu',name:'menu',component:MenuList}
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router;