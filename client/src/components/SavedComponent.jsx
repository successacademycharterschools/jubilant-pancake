import React from "react";

const SavedComponent = ({ saved }) => {

  // renders component that will display the list of searches the user has saved
  let savedItems = saved.map(item => (
    <ul key={saved.indexOf(item)} className="list-item">
      <li>Strings: {item.str1} & {item.str2}</li>
      <li>Distance: {item.distance}</li>
    </ul>
  ));

  return (
    <div className="SavedComponent child-component">
      <h3>Your Saved Results:</h3>
      <div className="list-items">{savedItems.length ? savedItems : `Save something!`}</div>
    </div>
  );
};

export default SavedComponent;
