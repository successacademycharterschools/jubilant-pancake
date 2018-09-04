import React, { Component } from 'react';
import './App.css';

class EditDistanceForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      formValues: {'val_1': '', 'val_2': ''}
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    event.preventDefault();
    let formValues = this.state.formValues;
    let name = event.target.name;
    let value = event.target.value;

    formValues[name] = value;

    this.setState({formValues})
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state.formValues);
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          <p>
            Input 1:
            <input type="text" name="val_1" value={this.state.formValues['val_1']} onChange={this.handleChange} />
          </p>
          <p>
            Input 2:
            <input type="text" name="val_2" value={this.state.formValues['val_2']} onChange={this.handleChange} />
          </p>
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Calculate Edit Distance</h1>
        </header>
        <NameForm />
      </div>
    );
  }
}

export default App;
