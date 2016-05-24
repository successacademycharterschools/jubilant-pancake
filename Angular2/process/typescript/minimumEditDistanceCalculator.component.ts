import {Component} from 'angular2/core';
import {UtilsService} from './service/Utils.service';

@Component({
	selector: 'minimum-edit-distance-calculator',
	templateUrl: 'partials/minimumEditDistanceCalculator.html',
	styleUrls: ['css/minimumEditDistanceCalculator.css'],
	providers: [UtilsService]
})

export class MinimumEditDistanceCalculatorComponent { 

	string1 = '';
	string2 = '';
	message = '';
	messageMode = 'warning';

	constructor(private _utilsService: UtilsService) {
		this.message = 'Edit distance between these 2 strings will be calculated.';
	}

	onClick() {
		
		this.message = '';
		
		if (this.string1==='' && this.string2===''){
			this.message += 'I did not need to make the call since both strings were empty and I could easily give the result which is 0. ';
		} else if (this.string1 === '') {
			this.message += `I did not need to make the call since the first string was empty and I could easily give the result which is ${this.string2.length}. `;
		} else if (this.string2 === '') {
			this.message += `I did not need to make the call since the second string was empty and I could easily give the result which is ${this.string1.length}. `;
		}
		
		this._utilsService.getMinimumEditDistance(this.string1, this.string2).subscribe(
			data => { this.message += `Server response is ${data.minimumEditDistance}.`; this.messageMode = 'success'; },
			error => { this.message = 'Something went terribly wrong. Please try again.'; this.messageMode = 'danger'; }
		);
		
    }

}