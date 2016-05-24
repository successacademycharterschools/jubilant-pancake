import {Injectable} from "angular2/core"
import {Http} from 'angular2/http';
import 'rxjs/Rx'
 
@Injectable()
export class UtilsService{
 
	 api_url:String = "http://localhost:3000/api/1/Utils/";
 
	 constructor(private http: Http){
			 this.http = http;
	 }

	 getMinimumEditDistance(string1, string2) {
			var body = "?string1=" + string1 + "&string2=" + string2;
			return this.http.get(this.api_url + 'minimumEditDistance'+body).map(res => res.json());
	 }
}