import React, { Component } from "react";
import './App.css';
import WelcomeComponent from "./components/WelcomeComponent.jsx";
import DashboardComponent from "./components/DashboardComponent.jsx";
import NavBar from "./components/NavBar.jsx";

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar />
        <WelcomeComponent />
        <br />
        <DashboardComponent />
        <br />
      </div>
    );
  }
}

export default App;
