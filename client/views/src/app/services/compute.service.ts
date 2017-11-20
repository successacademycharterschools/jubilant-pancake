import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';
import { FormText } from '../models/formtext.model';

@Injectable()
export class ComputeService {

    result: any;

    constructor(private httpClient: HttpClient) { }


    
    // --- Function for console log message: Begin ---
    serviceStarted() {
        console.log("Service started to check Minimum Edit Distance!!!");
    }
    // --- Function for console log message: End ---



    // ---Function to communicate with backend server: Begin---
    computeTexts(texts: FormText) {
        const body = JSON.stringify(texts);
        // console.log("FORM OBJECT RECEIVED BY SERVICE", body);

        const headers = new HttpHeaders({'Content-Type': 'application/json'});
        this.result = this.httpClient.post('http://localhost:4500/api/compute', body, {headers: headers})
            .map((response: Response) => response)
            .catch((error: Response) => Observable.throw(error));
            return this.result;
    }
    // --- Function to communicate with backend server: End ---
}