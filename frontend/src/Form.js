import React, { Component } from 'react';
import {Input} from './Input';

export class Form extends Component {
	/*constructor(props){
		super(props);	
	}*/
	handleSubmit(event){
		console.log("todo");
	}
	render(){
		return (
			<form onClick={this.handleSubmit}>
				 <Input id="input1" />
				 <Input id="input2" />
				 <input type="button" value="Submit"/>
			</form>
		);
	}
}
