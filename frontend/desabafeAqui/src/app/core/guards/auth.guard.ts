import { inject } from "@angular/core";
import { CanActivateFn, Router } from "@angular/router";
import { AuthService } from "../services/auth";

export const authGuard: CanActivateFn = (route, state) => {
    const authService = inject(AuthService);
    const router = inject(Router);

    if (localStorage.getItem('access_token')) {
        return true;
    } else {
        return router.parseUrl('/login');
    }
}

export const notAuthGuard: CanActivateFn = (route, state) => {
    const authService = inject(AuthService);
    const router = inject(Router);

    if (localStorage.getItem('access_token')) {
        return router.parseUrl('/');
    } else {
        return true;
    }
}