import { Component } from '@angular/core';
import { Router, ɵEmptyOutletComponent } from '@angular/router';

@Component({
  selector: 'app-rounded-button',
  imports: [ɵEmptyOutletComponent],
  templateUrl: './roundedButton.html',
  styleUrl: './roundedButton.scss',
})
export class RoundedButton {
  private router = Router
}
