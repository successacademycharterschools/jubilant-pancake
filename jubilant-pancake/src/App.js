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

  // Tested this with:
  // v1 = 'intention', v2 = 'execution', expected output = 8
  // v1 = 'cat', v2 = 'cat', expected output = 0
  // v1 = 'cat', v2 = 'dog', expected output = 6
  // v1 = <no input>, v2 = <no input>, expected output = <no output>
  calculate_min_edit_dist() {
    let v1 = this.props.formValues['val_1'];
    let v2 = this.props.formValues['val_2'];

    // initiate matrix
    let matrix = [],
    rows = v1.length,
    cols = v2.length;
    for ( var x = 0; x <= rows; x++ ) {  // create n rows and m columns
      matrix[x] = Array(cols).fill(0);  // start with all values 0
    }
    for ( x = 1; x <= rows; x++ ) {  // initiatilize first column values
      matrix[x][0] = x;
    }
    for ( var y = 1; y <= cols; y++ ) {  // initiatilize first row values
      matrix[0][y] = y;
    }

    // calculate edit distanceusing dynamic programming
    for ( var i = 1; i <= rows; i++) {
      for ( var j = 1; j <= cols; j++) {
        let added_val = 0;
        if (v1[i-1] !== v2[j-1]){  // if values at same spot are not equal
          added_val = 2;  // cost = 1 to delete and 1 to add correct letter = 2
        }
        
        // diff edit distance possibilities
        let same_row = matrix[i - 1][j] + 1,
        same_col = matrix[i][j-1] + 1,
        new_vals = matrix[i-1][j-1] + added_val;

        matrix[i][j] = Math.min(same_row, same_col, new_vals);  // min edit distance
        
      }
    }

    return matrix[rows][cols];
  }

  render() {
    let min_edit_dist = this.calculate_min_edit_dist();
    if (this.props.hidden) {
      return null;
    }
    return (
      <p>Edit Distance: {min_edit_dist}</p>
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
    this.setState({submitted: false});
    event.preventDefault();
    let formValues = this.state.formValues;
    let name = event.target.name;
    let value = event.target.value;

    formValues[name] = value;

    this.setState({formValues});
  }

  handleValueSubmit(event) {
    event.preventDefault();
    this.setState({submitted: true});
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Minimum Edit Distance Calculator</h1>
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
