import React from "react";

const ResultComponent = ({ result }) => {
  return (
    <div>
      <p>Edit Distance is {result.distance} for {result.str1} and {result.str2}</p>
    </div>
  );
};

export default ResultComponent;
