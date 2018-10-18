import React, { Component } from 'react';

export class Input extends Component {
	constructor(props){
		super(props);
		this.name = this.props.name;
		this.state = {val: props.value};
	}
	handleChange(event){
		this.setState({val: event.target.value});
	}
	render(){
		return (
			<div className="Input">
				<p>
					<input type="text" name={this.name} className="Input-text" value={this.state.val} onChange={this.handleChange.bind(this)}/>
				</p>
			</div>
		);
	}
}
