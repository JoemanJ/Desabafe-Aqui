import { Component, input } from '@angular/core';

@Component({
  selector: 'app-post',
  imports: [],
  templateUrl: './post.html',
  styleUrl: './post.scss',
})
export class Post {
  username = input<string>();
  user_profile_picture = input<string>();
  text = input<string>();
}
