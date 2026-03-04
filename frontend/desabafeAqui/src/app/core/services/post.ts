import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Post {
  private httpClient = inject(HttpClient);
  private readonly API_URL = 'http://127.0.0.1:8000/api/post';
}
