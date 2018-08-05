import React from "react";
import saLogo from "../images/sa-large-logo.jpg";

class NavBar extends React.Component {
  render() {
    return (
      <div className="navbar">
        <img src={saLogo} alt="logo" className="saLogo" />
        <div className="navbar-item item-border"> <p>Visit Us</p></div>
        <div className="navbar-item item-border"> <p>Ed Institute</p>  </div>
        <div className="navbar-item item-border"> <p>Giving</p>  </div>
        <div className="navbar-item item-border"> <p>Schools</p>  </div>
        <div className="navbar-item item-border"> <p>Results</p> </div>
        <div className="navbar-item item-border"> <p>Our Approach</p> </div>
        <div className="navbar-item first-item"> <p>About</p>  </div>
      </div>
    );
  }
}

export default NavBar;
