import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { PostCreationModel, PostModel } from '../models/post.model';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PostService {
  private httpClient = inject(HttpClient);
  private readonly API_URL = 'http://127.0.0.1:8000/api/posts/';

  getPosts(): Observable<PostModel[]> {
    return this.httpClient.get<PostModel[]>(this.API_URL);
  }

  makeNewPost(post: PostCreationModel){
    return this.httpClient.post(this.API_URL, post);
  }

  likePost(postSlug: string){
    return this.httpClient.post(`${this.API_URL}${postSlug}/like/`, '');
  }

  editPost(postSlug: string, newText: string){
    const body = {text: newText}
    return this.httpClient.patch(`${this.API_URL}${postSlug}/`, body);
  }

  deletePost(postSlug: string){
    return this.httpClient.delete(`${this.API_URL}${postSlug}/`);
  }
}
