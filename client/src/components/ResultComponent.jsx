import React from "react";

const ResultComponent = ({ distance, str1, str2 }) => {
  return (
    <div>
      <p>Edit Distance is {distance} for {str1} and {str2}</p>
    </div>
  );
};

export default ResultComponent;
