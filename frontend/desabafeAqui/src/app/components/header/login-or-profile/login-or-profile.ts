import { Component } from '@angular/core';

@Component({
  selector: 'app-login-or-profile',
  imports: [],
  templateUrl: './login-or-profile.html',
  styleUrl: './login-or-profile.scss',
})
export class LoginOrProfile {
  isLoggedIn: boolean = false;

  toggleLoggedIn() {
    this.isLoggedIn = !this.isLoggedIn;
    console.log(this.isLoggedIn);
  }
}
