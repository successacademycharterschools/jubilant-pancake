import React from "react";
import PropTypes from "prop-types";

class Body extends React.Component {
  render() {
    return (
      <form>
        <input type="text" value="Success" />
        <br />
        <input type="text" value="Academy" />
        <br />
      <input className='button' type="submit" value="Submit" />
      </form>
    );
  }
}

export default Body;
