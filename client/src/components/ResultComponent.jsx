import React from "react";

const ResultComponent = ({ result }) => {
  // renders the result of the edit distance calculation from the POST request
  return (
    <div className="ResultComponent child-component">
      <p>
        <strong>
          Edit Distance is <u>{result.distance}</u> for "{result.str1}" and "{result.str2}"
        </strong>
      </p>
    </div>
  );
};

export default ResultComponent;
