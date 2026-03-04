import { Component, inject, OnInit, Signal, signal, WritableSignal } from '@angular/core';
import { PostModel } from '../../core/models/post.model';
import { Post } from './post/post';
import { RoundedButton } from "../../components/rounded-button/roundedButton";
import { PostService } from '../../core/services/post';

@Component({
  selector: 'app-home',
  imports: [Post, RoundedButton],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home implements OnInit{
  postService = inject(PostService)
  
  posts: PostModel[] = [];

  feed_columns: WritableSignal<PostModel[][]> = signal([[],[],[],[]]);
  ngOnInit(): void {
    this.postService.getPosts().subscribe({
      next: (data) =>{
        this.posts = data;
        this.arrangePosts();
        console.log(this.feed_columns());
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
}
