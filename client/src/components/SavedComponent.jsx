import React from "react";

const SavedComponent = ({ saved }) => {

  let savedItems = saved.map(item => (
    <ul key={saved.indexOf(item)}>
      <li>Strings: {item.str1} & {item.str2}</li>
      <li>Distance: {item.distance}</li>
    </ul>
  ));

  return (
    <div>
      <h3>Your Saved Results:</h3>
      <div>{savedItems.length ? savedItems : `Save something!`}</div>
    </div>
  );
};

export default SavedComponent;
