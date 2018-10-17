import React, { Component } from 'react';
import {Input} from './Input';

export class Form extends Component {
	constructor(props){
		super(props);	
		this.handleSubmit = this.handleSubmit.bind(this);
	}
	handleSubmit(event){
		console.log("todo");
	}
	render(){
		return (
			<form>
				 <Input default="string_one" />
				 <Input default="string_two" />
				 <input type="button" value="Submit" onClick={this.handleSubmit} />
			</form>
		);
	}
}