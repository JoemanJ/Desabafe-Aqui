import { Routes } from '@angular/router';
import { LoginRegister } from './pages/login-register/login-register';
import { Home } from './pages/home/home';
import { notAuthGuard } from './core/guards/auth.guard';

export const routes: Routes = [
    {
        path: "login",
        component: LoginRegister,
        canActivate: [notAuthGuard],
    },
    {
        path:'',
        component: Home
    },
    {
        path: "**",
        redirectTo: "/"
    }
];
