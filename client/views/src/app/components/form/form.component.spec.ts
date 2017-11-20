import { HttpClientModule } from '@angular/common/http';
import { ComputeService } from './../../services/compute.service';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormComponent } from './form.component';
import { FormsModule, NgForm } from '@angular/forms';
// import { CUSTOM_ELEMENTS_SCHEMA, OnInit } from '@angular/core';

describe('FormComponent', () => {
 let component: FormComponent;
 let fixture: ComponentFixture<FormComponent>;
 let complied: any;
 let computeService: ComputeService;

 beforeEach(async(() => {
   TestBed.configureTestingModule({
       imports:      [ FormsModule, HttpClientModule ],
       declarations: [ FormComponent ],
       providers: [ ComputeService ]
      //  schemas: [CUSTOM_ELEMENTS_SCHEMA]
   })
   .compileComponents();
 }));

 beforeEach(() => {
   fixture = TestBed.createComponent(FormComponent);
   component = fixture.debugElement.componentInstance;
   fixture.detectChanges();
   this.compiled = fixture.debugElement.nativeElement;
   this.computeService = fixture.debugElement.injector.get(ComputeService);
 });

 it('should create the form component', () => {
   expect(component).toBeTruthy();
 });

 it('should have panel heading as "Please enter text below"', () => {
   expect(this.compiled.querySelector('h3.panel-title').textContent).toContain('Please enter text below');
 });

 it('should have label of "Source"', () => {
   expect(this.compiled.querySelector('label[for="text1"]').textContent).toContain('Source');
 });

 it('should have label of "Target"', () => {
   expect(this.compiled.querySelector('label[for="text2"]').textContent).toContain('Target');
 });

 it('shouldn\'t allow to submit when "Source" is empty', () => {
   expect(this.compiled.querySelector('input#text1').placeholder).toContain('Enter source');
 });

 it('shouldn\'t allow to submit when "Target" is empty', () => {
   expect(this.compiled.querySelector('input#text2').placeholder).toContain('Enter target');
 });

 it('should have button text as "Check"', () => {
   expect(this.compiled.querySelector('button.sbmt-btn-custom').textContent).toContain('Check');
 });

 it('should have textbox for "Source"', () => {
   expect(this.compiled.querySelector('input#text1')).toBeTruthy();
 });

 it('should have textbox for "Target"', () => {
   expect(this.compiled.querySelector('input#text2')).toBeTruthy();
 });

 it('should have button', () => {
   expect(this.compiled.querySelector('button.sbmt-btn-custom')).toBeTruthy();
 });

  it('should write a console service message "Service started to check Minimum Edit Distance!!!"', async() => {
   expect(this.computeService.serviceStarted());
 });


});
