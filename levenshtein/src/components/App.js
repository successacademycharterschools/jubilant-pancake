import React, { Component } from "react";
import Header from "./header";
import Body from "./body";
import Welcome from "./welcome.js";
import Instructions from "./instructions";
import "../App.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input1: "",
      input2: ""
    }
  }

  setInput1 = (e) => {
    this.setState({input1: e.target.value})
  }

  setInput2 = (e) => {
    this.setState({input2: e.target.value})
  }

  handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:3001/api/v1/inputs', {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
        'input1': `${this.state.input1}`,
        'input2': `${this.state.input2}`
      })
    })
      .then(r => r.json())
      .then(data => alert(`There would need to be ${data.result} operations to make your two strings identical!`))
      .then(this.setState({input1:"", input2: ""}))
  }

  render() {
    console.log(this.state.output);
    return (
      <div className="App">
        <Header />
        <div className="content">
          <Welcome />
        <Instructions />
      <Body setter1={this.setInput1} setter2={this.setInput2} mySubmit={this.handleSubmit} inputs={this.state}/>
        </div>
      </div>
    );
  }
}

export default App;
