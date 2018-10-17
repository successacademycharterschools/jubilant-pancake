import React, { Component } from 'react';
import './App.css';
import {Form} from './Form';

class App extends Component {

	handleSubmit(event){

	}

  render() {
    return (
      <div className="App">
        <header className="App-header">
		Welcome to the Jubilant Pancake
        </header>
		<div className="App-body">
			<Form/>
		</div>
      </div>
    );
  }
}

export default App;
