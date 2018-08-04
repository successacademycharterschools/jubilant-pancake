import React from "react";
import ResultComponent from "./ResultComponent.jsx";
import HistoryComponent from "./HistoryComponent.jsx";
import FormComponent from "./FormComponent.jsx";
import SavedComponent from "./SavedComponent.jsx";

class DashboardComponent extends React.Component {
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
