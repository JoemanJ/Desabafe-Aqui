import { Component } from '@angular/core';
import { PostModel } from '../../core/models/post.model';
import { Post } from './post/post';

@Component({
  selector: 'app-home',
  imports: [Post],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  private test_post = {
    text: 'test_post',
    slug: 'abcde',
    created_at: "today",
    author_details: {
        username: "test_user",
        picture: "blank_user.png"
    }
  }

  feed_columns: PostModel[][] = [
    [this.test_post, this.test_post, this.test_post],
    [this.test_post, this.test_post, this.test_post],
    [this.test_post, this.test_post, this.test_post],
    [this.test_post, this.test_post, this.test_post] 
  ]
}
