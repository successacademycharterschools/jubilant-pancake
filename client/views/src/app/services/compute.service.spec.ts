import { TestBed, inject } from '@angular/core/testing';
import { ComputeService } from './compute.service';
import { HttpClientModule } from '@angular/common/http';

describe('ComputeService', () => {
 beforeEach(() => {
   TestBed.configureTestingModule({
     providers: [ComputeService],
     imports:   [ HttpClientModule ],
   });
 });

 it('Compute service should be created', inject([ComputeService], (service: ComputeService) => {
   expect(service).toBeTruthy();
 }));

 it('should write a console service message "Service started to check Minimum Edit Distance!!!"', inject([ComputeService], (service: ComputeService) => {
  expect(service.serviceStarted());
 }));

});
