import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Response } from '@angular/http';
import { Observable } from 'rxjs';
import 'rxjs/Rx';

@Injectable()
export class ComputeService {

    result: any;

    constructor() { }

    serviceStarted() {
        console.log("Service started to check Minimum Edit Distance!!!");
    }
}