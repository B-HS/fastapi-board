import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import CKEditor from '@ckeditor/ckeditor5-vue';

// Bootstrap importing
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap"
        //Bootstrap Icon https://icons.getbootstrap.com/
        // import 'bootstrap-icons/font/bootstrap-icons.css'

createApp(App).use(store).use(router).use( CKEditor ).mount('#app')
