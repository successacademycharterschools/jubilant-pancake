import React, { Component } from "react";
import './App.css';
import WelcomeComponent from "./components/WelcomeComponent.jsx";
import DashboardComponent from "./components/DashboardComponent.jsx";
import NavBar from "./components/NavBar.jsx";
import Footer from "./components/Footer.jsx";

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar />
        <WelcomeComponent />
        <br />
        <DashboardComponent />
        <br />
        <Footer />
      </div>
    );
  }
}

export default App;
