import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RoundedButton } from './rounded-button';

describe('RoundedButton', () => {
  let component: RoundedButton;
  let fixture: ComponentFixture<RoundedButton>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RoundedButton]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RoundedButton);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
