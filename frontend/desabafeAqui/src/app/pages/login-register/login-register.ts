import { Component, inject, signal, WritableSignal } from '@angular/core';
import { AuthService } from '../../core/services/auth';
import { Router } from '@angular/router';
import { HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { RoundedButton } from "../../components/rounded-button/roundedButton";

@Component({
  selector: 'app-login-register',
  imports: [RoundedButton],
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
        this.authService.updateAuthState(true);
        this.router.navigate(['/']);
      },
      error: (res) => this.handleLoginError(res)
    });
  }

  private saveCredentials(res: any){
    localStorage.setItem("access_token", res.access);
    localStorage.setItem("refresh_token", res.refresh);
    localStorage.setItem("username", res.username);
  }

  private handleLoginError(res: HttpErrorResponse){
    this.loginErrorMessage.set(this.errorMessageForStatusCode(res.status));
  }

  private errorMessageForStatusCode(status: number){
    switch (status){
      case 0:
        return 'Não foi possível conectar ao servidor backend.';
      case 400:
        return "Email ou nome de usuário já cadastrado.";
      case 401:
        return 'Usuário ou senha inválidos.';
      default:
        return 'Um erro inesperado aconteceu. Tente novamente.';
    }
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
        this.login(username, password);

      },
      error: (res) => this.handleRegisterError(res)
    })
  }

  private handleRegisterError(res: HttpErrorResponse){
    this.registerErrorMessage.set(this.errorMessageForStatusCode(res.status))
  }
}
