import React from "react";
import logo from "../Success_Logo.png";
import PropTypes from "prop-types";

class Header extends React.Component {
  render() {
    return (<div className="header">
      <img src={logo} className="App-logo" alt="logo"/>
    </div>);
  }
}

export default Header;
