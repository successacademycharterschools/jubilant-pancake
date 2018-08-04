import React from "react";
import PropTypes from "prop-types";

class WelcomeComponent extends React.Component {
  render() {
    return (
      <div className="WelcomeComponent">
        <h1>Welcome!</h1>
        <h3>
          Welcome to the Success Academy edit distance app using the Levenshtein
          distance.
        </h3>
      </div>
    );
  }
}

export default WelcomeComponent;
