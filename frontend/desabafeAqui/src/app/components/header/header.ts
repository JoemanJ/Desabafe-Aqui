import { Component, inject, input } from '@angular/core';
import { LoginOrProfile } from './login-or-profile/login-or-profile';

@Component({
  selector: 'app-header',
  imports: [LoginOrProfile],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
}
