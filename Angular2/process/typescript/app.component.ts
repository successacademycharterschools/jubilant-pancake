import {Component} from 'angular2/core';
import {MinimumEditDistanceCalculatorComponent} from './minimumEditDistanceCalculator.component'

@Component({
	selector: 'my-app',
	templateUrl: 'partials/app.html',
	directives: [MinimumEditDistanceCalculatorComponent],
	styleUrls: ['css/app.css']
})

export class AppComponent {}