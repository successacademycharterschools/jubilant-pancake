import React, { Component } from 'react';

export class Input extends Component {
	/*constructor(props){
		super(props);	
	}*/
	render(){
		return (
			<div className="Input">
				<p>
					<input id="this.props.id" type="text" className="Input-text" />
				</p>
			</div>
		);
	}
}
