import React from "react";

const FormComponent = ({ str1, str2, handleInput, handleSubmit }) => {
  // renders form for user input
  return (
    <div className="FormComponent child-component">
      <h2>Edit Distance</h2>
      <p>
        Input two strings, words or sentences to see what the{" "}
        <a
          href="https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm"
          target="_blank"
          rel="noopener noreferrer"
        >
          edit distance
        </a>{" "}
        between the two is using the Levenshtein Distance Metric.
      </p>
      <form>
        <input
          name="str1"
          type="text"
          value={str1}
          onChange={handleInput.bind(this)}
          placeholder="Enter First String"
          className="input-box"
        />
        <input
          name="str2"
          type="text"
          value={str2}
          onChange={handleInput.bind(this)}
          placeholder="Enter Second String"
          className="input-box"
        />
        <button className="button" onClick={handleSubmit.bind(this)}>
          Check Edit Distance
        </button>
        <br />
      </form>
    </div>
  );
};

export default FormComponent;
