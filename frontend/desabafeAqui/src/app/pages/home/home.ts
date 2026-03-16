import { Component, inject, OnInit, Signal, signal, WritableSignal, ɵgetUnknownPropertyStrictMode } from '@angular/core';
import { PostCreationModel, PostModel } from '../../core/models/post.model';
import { Post } from './post/post';
import { RoundedButton } from "../../components/rounded-button/roundedButton";
import { PostService } from '../../core/services/post';
import { AuthService } from '../../core/services/auth';

@Component({
  selector: 'app-home',
  imports: [Post, RoundedButton],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home implements OnInit{
  postService = inject(PostService)
  authService = inject(AuthService)

  username: string | null = null;

  posts: PostModel[] = [];

  feed_columns: WritableSignal<PostModel[][]> = signal([[],[],[],[]]);

  constructor(){
    this.authService.username.subscribe((username) => this.username = username);
  }

  ngOnInit(): void {
    this.username = this.authService.getUsername();
    this.fetchPosts();
  }

  private fetchPosts(): void{
    this.postService.getPosts().subscribe({
      next: (data) =>{
        this.posts = data;
        this.arrangePosts();
      },
      error: (err) => console.log("Falha ao carregar posts:", err)
    });
  }

  private arrangePosts(): void{
    let col = 0;
    let cols: PostModel[][] = [[],[],[],[]]
    for(const p of this.posts){
      cols[col].push(p);
      col = (col+1) % 4;
    }
    this.feed_columns.set(cols)
  }

  makeNewPost(post_text: string){
    const post_data: PostCreationModel = {
      text: post_text
    }
    this.postService.makeNewPost(post_data).subscribe({
      next: (res) => this.fetchPosts(),
      error: (err) => alert("Ops! Algo deu errado. Por favor tente novamente")
    });
  }

  onPostDeleted(){
    
  }
}
