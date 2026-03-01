import { Component } from '@angular/core';
import { Header } from '../../components/header/header';

@Component({
  selector: 'app-login-register',
  imports: [],
  templateUrl: './login-register.html',
  styleUrl: './login-register.scss',
})
export class LoginRegister {
  login(username: string): void{
    console.log("Trying to login as:", username);
  }
}
