import { HttpInterceptorFn, HttpRequest } from "@angular/common/http";

const tokenless_urls = ['api/token', 'api/register']

function isAuthRequest(req: HttpRequest<unknown>): boolean{
    for(let url of tokenless_urls){
        if(req.url.includes(url)) return true
    }
    return false
}

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const token = localStorage.getItem('access_token');

    if (token && !isAuthRequest(req)){
        const cloned = req.clone({
            setHeaders: {
                Authorization: `Bearer ${token}`
            }
        });
        return next(cloned);
    }

    return next(req);
}