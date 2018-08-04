import React from "react";
import ResultComponent from "./ResultComponent.jsx";

class FormComponent extends React.Component {
  state = {
    str1: "",
    str2: "",
    distance: "",
    history: [],
    saved: []
  };

  handleInput = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  handleSubmit = e => {
    e.preventDefault();
    console.log(this.state);
    const { str1, str2, history } = this.state;
    let body = JSON.stringify({ str1, str2 });
    return fetch(`/`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body
    })
      .then(res => res.json())
      .then(json => {
        this.setState({
          distance: json.distance,
          history: [...history, json]
        });
      });
  };

  render() {
    const { str1, str2, distance } = this.state;
    return (
      <div className="FormComponent">
        <form>
          <input
            name="str1"
            type="text"
            value={str1}
            onChange={this.handleInput}
            placeholder="Enter First String"
            className="input-box"
          />
          <input
            name="str2"
            type="text"
            value={str2}
            onChange={this.handleInput}
            placeholder="Enter Second String"
            className="input-box"
          />
          <button className="button" onClick={this.handleSubmit}>
            Check Edit Distance
          </button>
          <br />
        </form>
        {distance !== "" ? (
          <ResultComponent distance={distance} str1={str1} str2={str2} />
        ) : null}
      </div>
    );
  }
}

export default FormComponent;
