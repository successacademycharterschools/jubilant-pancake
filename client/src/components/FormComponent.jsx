import React from "react";

const FormComponent = ({ str1, str2, handleInput, handleSubmit }) => {

  return (
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
  );
};

export default FormComponent;
