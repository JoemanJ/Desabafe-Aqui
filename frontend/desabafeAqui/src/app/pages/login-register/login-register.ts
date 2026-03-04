import { Component, inject, signal, WritableSignal } from '@angular/core';
import { AuthService } from '../../core/services/auth';

@Component({
  selector: 'app-login-register',
  imports: [],
  templateUrl: './login-register.html',
  styleUrl: './login-register.scss',
})
export class LoginRegister {
  private authService = inject(AuthService)
  loginErrorMessage: WritableSignal<string> = signal('');
  registerErrorMessage: WritableSignal<string> = signal('');

  login(username: string, password: string): void{
    const user_data = {username: username, password: password}

    this.authService.login(user_data).subscribe({
      next: (res: any) => {
        localStorage.setItem("access_token", res.access);
        localStorage.setItem("refresh_token", res.refresh);
        localStorage.setItem("username", res.username);
      },
      error: (res) => {
        this.loginErrorMessage.set('Usuário ou senha inválidos')
        console.log(this.loginErrorMessage)
      }
    });
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
        console.log("Usuário registrado:", username);
        this.login(username, password)
      },

      error: (res) => {
        console.log("Error: ", res)
        this.registerErrorMessage.set('Algo deu errado no registro')
      }
    })
  }
}
