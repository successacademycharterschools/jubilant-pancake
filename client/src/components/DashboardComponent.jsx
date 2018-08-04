import React from "react";
import ResultComponent from "./ResultComponent.jsx";
import HistoryComponent from "./HistoryComponent.jsx";
import FormComponent from "./FormComponent.jsx";
import SavedComponent from "./SavedComponent.jsx";

class DashboardComponent extends React.Component {
  // set state with empty strings, distance, history and saved.
  // str1 and str2 will be the user input. distance will be the Levenshtein
  // distance calculated in the backend
  state = {
    str1: "",
    str2: "",
    distance: "",
    history: [],
    saved: []
  };

  // sets state equal to user input for str1 and str2
  handleInput = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  // sends POST request to backend for Levenshtein distance calculation,
  // clears user input, and sets history and distance in state
  handleSubmit = e => {
    e.preventDefault();
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

  // saves the result to the saved array in state
  handleSave = e => {
    e.preventDefault();
    const { saved, history } = this.state;
    let save = history[history.length - 1];
    this.setState({
      saved: [...saved, save]
    });
  };

  render() {
    console.log(this.state);
    const { str1, str2, distance, history, saved } = this.state;
    let result = history[history.length - 1];
    return (
      <div className="DashboardComponent">
        <FormComponent
          str1={str1}
          str2={str2}
          handleInput={this.handleInput}
          handleSubmit={this.handleSubmit}
        />
        {distance !== "" ? (
          <div>
            <ResultComponent result={result} />
            <button className="button" onClick={this.handleSave}>
              Save Result
            </button>
          </div>
        ) : null}
        <HistoryComponent history={history} />
        <SavedComponent saved={saved} />
      </div>
    );
  }
}

export default DashboardComponent;
