import { HttpErrorResponse, HttpHandlerFn, HttpInterceptorFn, HttpRequest } from "@angular/common/http";
import { inject } from "@angular/core";
import { catchError, switchMap, throwError } from "rxjs";
import { AuthService } from "../services/auth";

const tokenless_urls = ['api/token', 'api/register']

function isAuthRequest(req: HttpRequest<unknown>): boolean{
    for(let url of tokenless_urls){
        if(req.url.includes(url)) return true
    }
    return false
}

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const token = localStorage.getItem('access_token');
    const authService = inject(AuthService);

    if (token && !isAuthRequest(req)){
        const cloned = addAuthHeaders(req, token);

        return next(cloned).pipe(
            catchError((error) => {
                if (error instanceof HttpErrorResponse && error.status === 401 && !isAuthRequest(req)) {
                    return handle401Error(req, next, authService);
                }
                return throwError(() => error);
            })
        )
    }

    return next(req);
}

function addAuthHeaders(req: HttpRequest<unknown>, token: string){
    return req.clone({
            setHeaders: {
                Authorization: `Bearer ${token}`
            }
        })
}

function handle401Error(req: HttpRequest<any>, next: HttpHandlerFn, authService: AuthService){
    return authService.refreshToken().pipe(
        switchMap((tokens) => {
            const newRequest = addAuthHeaders(req, tokens.access);

            return next(newRequest);
        }),
        catchError((err) => {
            authService.logout();
            return throwError(() => err);
        })
    )
}