import React from "react";

const HistoryComponent = ({ history }) => {

  let historyItems = history.map(item =>
    <ul key={history.indexOf(item)}>
      <li>String1: {item.str1}</li>
      <li>String2: {item.str2}</li>
      <li>Distance: {item.distance}</li>
    </ul>
  );

  return (
    <div>
      <h3>Your Previous Searches:</h3>
      <div>{historyItems}</div>
    </div>
  );

};

export default HistoryComponent;
