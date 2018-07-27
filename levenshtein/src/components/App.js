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
      input2: "",
      output: ""
    }
  }

  setInput1 = (e) => {
    this.setState({input1: e.target.value})
    console.log("My state is", this.state.input1);
  }

  setInput2 = (e) => {
    this.setState({input2: e.target.value})
    console.log("My state is", this.state.input2);
  }

  render() {
    return (
      <div className="App">
        <Header />
        <div className="content">
          <Welcome />
        <Instructions />
      <Body setter1={this.setInput1} setter2={this.setInput2}/>
        </div>
      </div>
    );
  }
}

export default App;
