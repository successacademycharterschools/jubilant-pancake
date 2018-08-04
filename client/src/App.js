import React, { Component } from "react";
import './App.css';
import WelcomeComponent from "./components/WelcomeComponent.jsx";
import DashboardComponent from "./components/DashboardComponent.jsx";

class App extends Component {
  render() {
    return (
      <div className="App">
        <WelcomeComponent />
        <br />
        <DashboardComponent />
        <br />
      </div>
    );
  }
}

export default App;
