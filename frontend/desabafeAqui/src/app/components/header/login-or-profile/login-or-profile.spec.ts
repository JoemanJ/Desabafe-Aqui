import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginOrProfile } from './login-or-profile';

describe('LoginOrProfile', () => {
  let component: LoginOrProfile;
  let fixture: ComponentFixture<LoginOrProfile>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LoginOrProfile]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LoginOrProfile);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
