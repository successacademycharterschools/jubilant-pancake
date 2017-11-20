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

  public panelHeading: string = "Please enter text below";
  public texts: FormText;
  public distOper: string;

  constructor(private computeService: ComputeService) { }

  ngOnInit() {
    this.computeService.serviceStarted();
  }


  onSubmit(form: NgForm) {
    this.texts = form.value;
    // console.log("FORM OBJECT SUBMITTED: ", this.texts);

    this.computeService.computeTexts(this.texts)
      .subscribe(
        data =>
        // console.log(data.distOper),
          this.distOper = data.distOper,
        error => console.error(error)
    );

    form.reset();
  }

}