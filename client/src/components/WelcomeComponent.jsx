import React from "react";

class WelcomeComponent extends React.Component {
  // renders component that welcomes user
  render() {
    return (
      <div className="WelcomeComponent">
        <h1>Welcome!</h1>
        <p>
          Welcome to the Success Academy string edit distance app using the
          Levenshtein Distance Metric. <em>Redefining what's possible.</em>
        </p>
      </div>
    );
  }
}

export default WelcomeComponent;
