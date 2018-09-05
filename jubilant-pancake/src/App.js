import React, { Component } from 'react';
import './App.css';

class StringInputForm extends Component {
  constructor(props) {
    super(props);
    this.handleValueInputChange = this.handleValueInputChange.bind(this);
    this.handleValueInputSubmit = this.handleValueInputSubmit.bind(this);
  }
  
  handleValueInputChange(e) {
    this.props.onValueChange(e);
  }

  handleValueInputSubmit(e) {
    this.props.onValueSubmit(e);
  }

  render() {
    return (
      <form onSubmit={this.handleValueInputSubmit}>
        <label>
          <p>
            Input 1:
            <input type="text" name="val_1" value={this.props.formValues['val_1']} onChange={this.handleValueInputChange} />
          </p>
          <p>
            Input 2:
            <input type="text" name="val_2" value={this.props.formValues['val_2']} onChange={this.handleValueInputChange} />
          </p>
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

class Result extends Component {
  constructor(props) {
    super(props);
    
  }

  calculate_edit_dist() {
    let v1 = this.props.formValues['val_1'];
    let v2 = this.props.formValues['val_2']
    return v1.length - v2.length;
  }

  render() {
    var edit_dist = this.calculate_edit_dist();
    if (this.props.hidden) {
      return null;
    }
    return (
      <p>Edit Distance: {edit_dist}</p>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      formValues: {'val_1': '', 'val_2': ''},
      submitted: false
    };
    
    this.handleValueChange = this.handleValueChange.bind(this); // for sending input back up the hierarchy
    this.handleValueSubmit = this.handleValueSubmit.bind(this);
  }

  handleValueChange(event) {
    event.preventDefault();
    let formValues = this.state.formValues;
    let name = event.target.name;
    let value = event.target.value;

    formValues[name] = value;

    this.setState({formValues})
  }

  handleValueSubmit(event) {
    event.preventDefault();
    this.setState({submitted: true})
    console.log(this.state.formValues);
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Edit Distance Calculator</h1>
        </header>
        <StringInputForm
          formValues={this.state.formValues}
          onValueChange={this.handleValueChange}
          onValueSubmit={this.handleValueSubmit}
          submitted={this.state.submitted}
        />
        <Result
          formValues={this.state.formValues}
          hidden={this.state.submitted !== true}
        />
      </div>
    );
  }
}

export default App;
