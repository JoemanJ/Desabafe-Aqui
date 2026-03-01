import { Component, input } from '@angular/core';
import { LoginOrProfile } from './login-or-profile/login-or-profile';

@Component({
  selector: 'app-header',
  imports: [LoginOrProfile],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
  omitLoginProfile = false;

  hideLoginProfile(): void{
    this.omitLoginProfile = false;
  }

  showLoginProfile(): void{
    this.omitLoginProfile = true;
  }
}
