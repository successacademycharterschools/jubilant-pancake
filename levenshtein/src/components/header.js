import React from "react";
import logo from "../Succes_Logo.png";
import PropTypes from "prop-types";

class Header extends React.Component {
  render() {
    return (
      <div className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    );
  }
}

export default Header;
