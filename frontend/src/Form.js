import React, { Component } from 'react';
import {Input} from './Input';

//react http library
import axios from 'axios';

export class Form extends Component {
	constructor(props){
		super(props);	
		this.handleSubmit = this.handleSubmit.bind(this);
		//state is managed by the component, props are read only
		this.state = {
			result :"no result yet!"
		};
	}
	handleSubmit(event){
		event.preventDefault();//don't reload
		axios.get("http://localhost:5000", {
			params: {
				val1: event.target.input1.value,
				val2: event.target.input2.value
			}
		})
			.then(
				response => {
					console.log(response);
					this.setState({
						result: response.data.result
					});
			});
	}
	render(){
		return (
			<form onSubmit={this.handleSubmit}>
				 <Input name="input1" value='string_one' />
				 <Input name="input2" value='string_two' />
				 <input type="submit" value="Submit"/>
			<div>Your result: {this.state.result}</div>
			</form>
		);
	}
}
