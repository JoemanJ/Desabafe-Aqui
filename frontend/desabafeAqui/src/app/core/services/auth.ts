import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

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
  private httpClient = inject(HttpClient);
  private readonly LOGIN_URL = 'http://127.0.0.1:8000/api/token/'
  private readonly REGISTER_URL = 'http://127.0.0.1:8000/api/register/'

  login(credentials: LoginCredentials){
    return this.httpClient.post(this.LOGIN_URL, credentials);
  }

  register(credentials: RegisterCredentials){
    return this.httpClient.post(this.REGISTER_URL, credentials)
  }
}
