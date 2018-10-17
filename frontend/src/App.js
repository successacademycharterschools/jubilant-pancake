import React, { Component } from 'react';
import './App.css';
import {Input} from './Input'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
		Welcome to the Jubilant Pancake
        </header>
		<body>
			<div className="App-body">
				<Input/>
				<Input/>
			</div>
		</body>
      </div>
    );
  }
}

export default App;
