import { Routes } from '@angular/router';
import { LoginRegister } from './pages/login-register/login-register';
import { Home } from './pages/home/home';

export const routes: Routes = [
    {
        path: "login",
        component: LoginRegister,
    },
    {
        path:'',
        component: Home
    }
];
