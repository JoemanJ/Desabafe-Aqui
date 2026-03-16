import { Component, inject, input, isWritableSignal, linkedSignal, signal } from '@angular/core';
import { AuthService } from '../../../core/services/auth';
import { NgClass } from '@angular/common';
import { PostService } from '../../../core/services/post';

@Component({
  selector: 'app-post',
  templateUrl: './post.html',
  styleUrl: './post.scss',
})
export class Post {
  authService = inject(AuthService);
  postService = inject(PostService);

  username = input<string>();
  user_profile_picture = input<string>();
  slug = input<string>('');
  text = input<string>();
  likesCountInput = input<number>(0);
  likesCount = linkedSignal(() => this.likesCountInput());
  isLikedInput = input<boolean>(false);
  isLiked = linkedSignal(() => this.isLikedInput());

  isLoggedIn = signal<boolean>(false);
  
  currentUser: string | null = null;
  constructor(){
    this.authService.username.subscribe((username) => this.currentUser = username);
    this.authService.isLoggedIn.subscribe((status) => this.isLoggedIn.set(status));
  }


  isOwn(): boolean{
    return this.currentUser == this.username();
  }

  onlike(): void {
    const previousIsLiked: boolean = this.isLiked();
    const previousLikesCount: number = this.likesCount() ?? 0;
    
    const newIsLiked: boolean = !previousIsLiked;
    this.isLiked.set(newIsLiked);
    this.likesCount.update((v) => newIsLiked ? v+1 : v-1);

    this.postService.likePost(this.slug()).subscribe({
      error: (err) => {
        this.isLiked.set(previousIsLiked);
        this.likesCount.set(previousLikesCount);

        alert("Ops! Algo deu errado ao registrar seu like! Por favor tente novamente");
      }
    })
  }

  onEdit(): void {

  }

  onRemove(): void {

  }
}
