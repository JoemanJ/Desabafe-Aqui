import { Component } from '@angular/core';
import { RouterLink } from "@angular/router";

@Component({
  selector: 'app-login-or-profile',
  imports: [RouterLink],
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
