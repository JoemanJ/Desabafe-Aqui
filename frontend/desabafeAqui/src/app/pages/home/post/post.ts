import { Component, inject, input } from '@angular/core';
import { AuthService } from '../../../core/services/auth';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-post',
  imports: [NgClass],
  templateUrl: './post.html',
  styleUrl: './post.scss',
})
export class Post {
  authService = inject(AuthService);
  
  currentUser: string | null = null;
  constructor(){
    this.authService.username.subscribe((username) => this.currentUser = username);
  }

  username = input<string>();
  user_profile_picture = input<string>();
  text = input<string>();

  debug(){
    console.log(this.username(), this.currentUser);
  }
}
