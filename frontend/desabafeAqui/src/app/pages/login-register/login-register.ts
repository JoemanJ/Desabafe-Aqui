import { Component, inject, signal, WritableSignal } from '@angular/core';
import { AuthService } from '../../core/services/auth';
import { Router } from '@angular/router';
import { HttpResponse } from '@angular/common/http';

@Component({
  selector: 'app-login-register',
  imports: [],
  templateUrl: './login-register.html',
  styleUrl: './login-register.scss',
})
export class LoginRegister {
  private authService = inject(AuthService)
  private router = inject(Router)

  loginErrorMessage: WritableSignal<string> = signal('');
  registerErrorMessage: WritableSignal<string> = signal('');

  login(username: string, password: string): void{
    const user_data = {username: username, password: password}

    this.authService.login(user_data).subscribe({
      next: (res) => {
        this.saveCredentials(res);
        this.router.navigate(['/']);
      },
      error: this.handleLoginError
    });
  }



  saveCredentials(res: any){
    localStorage.setItem("access_token", res.access);
    localStorage.setItem("refresh_token", res.refresh);
    localStorage.setItem("username", res.username);
  }

  handleLoginError(res: any){
    this.loginErrorMessage.set('Usuário ou senha inválidos')
    console.log(this.loginErrorMessage)
  
  }

  register(username: string, email: string, password: string, confirm_password: string): void {
    const new_user_data = {
      username: username,
      email: email,
      password: password,
      confirm_password: confirm_password
    }

    this.authService.register(new_user_data).subscribe({
      next: (res: any) => {
        this.login(username, password)
      },
      error: this.handleRegisterError
    })
  }

  handleRegisterError(res: any){
    console.log("Error: ", res)
        this.registerErrorMessage.set('Algo deu errado no registro')
  }
}
