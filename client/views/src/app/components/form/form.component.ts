import { Component, OnInit } from '@angular/core';
import { ComputeService } from '../../services/compute.service';
import { NgForm } from '@angular/forms';
import { FormText } from '../../models/formtext.model';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  public panelHeading = 'Please enter text below';
  

  constructor(private computeService: ComputeService) { }

  ngOnInit() {
    this.computeService.serviceStarted();
  }


  

}