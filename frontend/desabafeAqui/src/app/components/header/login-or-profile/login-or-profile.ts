import { Component, inject } from '@angular/core';
import { RouterLink } from "@angular/router";
import { AuthService } from '../../../core/services/auth';
import { RoundedButton } from '../../rounded-button/roundedButton';

@Component({
  selector: 'app-login-or-profile',
  imports: [RouterLink, RoundedButton],
  templateUrl: './login-or-profile.html',
  styleUrl: './login-or-profile.scss',
})
export class LoginOrProfile {
  private authService = inject(AuthService);
  isLoggedIn = true;

  constructor(){
    this.authService.isLoggedIn.subscribe((status) => this.isLoggedIn = status);
  }

  logout(): void{
    this.authService.logout();
  }
}
