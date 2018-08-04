import React from "react";
import ResultComponent from "./ResultComponent.jsx";
import HistoryComponent from "./HistoryComponent.jsx";

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
          str1: "",
          str2: "",
          distance: json.distance,
          history: [...history, json]
        });
      });
  };

  handleSave = e => {
    e.preventDefault()
    console.log(e.target)
  }


  render() {
    const { str1, str2, distance, history } = this.state;
    let result = history[history.length-1]
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
          <ResultComponent result={result} />
        ) : null}
        <HistoryComponent history={history} save={this.handleSave}/>
      </div>
    );
  }
}

export default FormComponent;
