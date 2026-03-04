import { Component, inject, input } from '@angular/core';
import { LoginOrProfile } from './login-or-profile/login-or-profile';
import { NavigationEnd, Router } from '@angular/router';
import { filter } from 'rxjs';

@Component({
  selector: 'app-header',
  imports: [LoginOrProfile],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
  private router = inject(Router);

  showLoginProfileSection = true;

  constructor(){
    this.router.events.pipe(
      filter(e => e instanceof NavigationEnd)
    ).subscribe((e: NavigationEnd) => {
      this.showLoginProfileSection = e.urlAfterRedirects !== '/login'
    })
  }
}
