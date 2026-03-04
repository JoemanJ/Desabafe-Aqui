import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ProfileService {
  private httpClient = inject(HttpClient);
  private readonly API_URL = 'http://127.0.0.1:8000/api/profile'
  private readonly API_URL_mini = 'http://127.0.0.1:8000/api/profilemini'

  getMyProfile(username: string): Observable<any> {
    return this.httpClient.get(`${this.API_URL}/${username}/`)
  }
}
