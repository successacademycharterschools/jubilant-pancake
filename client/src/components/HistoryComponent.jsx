import React from "react";

const HistoryComponent = ({ history }) => {
  let historyItems = history.map(item => (
    <ul key={history.indexOf(item)}>
      <li>
        Strings: {item.str1} & {item.str2}
      </li>
      <li>Distance: {item.distance}</li>
    </ul>
  ));

  return (
    <div>
      <h3>Your Previous Searches:</h3>
      <div>{historyItems.length ? historyItems : `No history to display.`}</div>
    </div>
  );
};

export default HistoryComponent;
