import React from "react";

const ResultComponent = ({ result }) => {
  // renders the result of the edit distance calculation from the POST request
  return (
    <div>
      <p>Edit Distance is {result.distance} for {result.str1} and {result.str2}</p>
    </div>
  );
};

export default ResultComponent;
