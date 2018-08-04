import React, { Component } from "react";
import WelcomeComponent from "./components/WelcomeComponent.jsx";
import FormComponent from "./components/FormComponent.jsx";

class App extends Component {
  render() {
    return (
      <div className="App">
        <WelcomeComponent />
        <br />
        <FormComponent />
        <br />
      </div>
    );
  }
}

export default App;
