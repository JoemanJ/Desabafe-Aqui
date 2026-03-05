import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

interface RegisterCredentials {
    username: string;
    email: string;
    password: string;
    confirm_password: string;
}

interface LoginCredentials {
    username: string;
    password: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly LOGIN_URL = 'http://127.0.0.1:8000/api/token/'
  private readonly REGISTER_URL = 'http://127.0.0.1:8000/api/register/'
  
  private httpClient = inject(HttpClient);
  private LoggedIn$ = new BehaviorSubject<boolean>(this.hasToken());
  isLoggedIn = this.LoggedIn$.asObservable();
  private username$ = new BehaviorSubject<string|null>(this.getUsername());
  username = this.username$.asObservable();

  login(credentials: LoginCredentials){
    return this.httpClient.post(this.LOGIN_URL, credentials);
  }

  logout(): void{
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('username');
    this.username$.next(null);
    this.updateAuthState(false);
  }

  register(credentials: RegisterCredentials){
    return this.httpClient.post(this.REGISTER_URL, credentials)
  }

  private hasToken(): boolean{
    return !!localStorage.getItem('access_token');
  }

  updateAuthState(status: boolean): void{
    this.LoggedIn$.next(status)
  }

  getUsername(): string | null {
    return localStorage.getItem('username');
  }
}
