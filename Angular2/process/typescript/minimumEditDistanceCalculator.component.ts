import {Component} from 'angular2/core';
import {UtilsService} from './service/Utils.service';

@Component({
	selector: 'minimum-edit-distance-calculator',
	templateUrl: 'partials/minimumEditDistanceCalculator.html',
	styleUrls: ['css/minimumEditDistanceCalculator.css'],
	providers: [UtilsService]
})

export class MinimumEditDistanceCalculatorComponent { 

	private maximumTotalLength = 1920; // an approximate limit: 2048 byte IE limit minus aproximately 450byte minimum request length
	private defaultMessage = 'Edit distance between these 2 strings will be calculated.';
	public string1 = '';
	public string2 = '';
	public message = '';
	public messageMode = '';

	constructor(private _utilsService: UtilsService) {
		this.display(this.defaultMessage);
	}

	onClick() {
		
		if (this.string1.length + this.string2.length > this.maximumTotalLength) {
			this.display('The strings are too long.', 'danger');
		} else {
			this.display('Calculating. Please wait.', 'warning');
			this._utilsService.getMinimumEditDistance(this.string1, this.string2).subscribe(
				data => this.display(`Server response is ${data.minimumEditDistance}.`, 'success'),
				error => this.display('Something went terribly wrong. Please try again.', 'danger')
			);
		}

    }

    onKeyup() {
		this.display(this.defaultMessage);
    }

    display(copy, mode='info'){
		this.message = copy; 
		this.messageMode = mode;
    }

}