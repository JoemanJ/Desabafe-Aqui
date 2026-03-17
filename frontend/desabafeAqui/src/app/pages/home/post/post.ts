import { Component, inject, input, isWritableSignal, linkedSignal, output, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../../core/services/auth';
import { PostService } from '../../../core/services/post';
import { RoundedButton } from "../../../components/rounded-button/roundedButton";

@Component({
  selector: 'app-post',
  imports: [RoundedButton, FormsModule],
  templateUrl: './post.html',
  styleUrl: './post.scss',
})
export class Post {
  authService = inject(AuthService);
  postService = inject(PostService);

  username = input<string>();
  user_profile_picture = input<string>();
  slug = input<string>('');
  textInput = input.required<string>();
  text = linkedSignal(() => this.textInput());
  likesCountInput = input<number>(0);
  likesCount = linkedSignal(() => this.likesCountInput());
  isLikedInput = input<boolean>(false);
  isLiked = linkedSignal(() => this.isLikedInput());

  isLoggedIn = signal<boolean>(false);
  deleted = output<string>();

  isEditing = signal<boolean>(false);
  isConfirmingDelete = signal<boolean>(false);
  
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

        alert("Ops! Algo deu errado ao registrar seu like! Por favor tente novamente!");
      }
    })
  }


  toggleEdit(): void {
    // Revert to original text if we're done editing
    if (this.isEditing()){
      this.text.set(this.textInput());
    }
    this.isEditing.update((v)=>!v);
  }

  saveEdit(): void{
    const newText = this.text();

    this.postService.editPost(this.slug(), this.text()).subscribe({
      next: (response) => {
        this.isEditing.set(false);
      },
      error: (err) => alert("Ops! Algo deu errado ao editar seu post! Por favor tente novamente!")
    })
  }

  toggleDelete(): void {
    this.isConfirmingDelete.update((v)=>!v);
  }

  confirmDelete(): void {
    this.postService.deletePost(this.slug()).subscribe({
      next: (response) => {
        this.deleted.emit(this.slug());
      },
      error: (err) => alert("Ops! Algo deu errado ao apagar seu post! Por favor tente novamente!")
    })
  }
}
