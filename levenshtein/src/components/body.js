import React from "react";
import PropTypes from "prop-types";

class Body extends React.Component {
  render() {
    return (
      <form className='form'>
        <input type="text" placeholder="S" />
        <br />
      <input type="text" placeholder="T" />
        <br />
      <input className='button' type="submit" value="SUBMIT" />
      </form>
    );
  }
}

export default Body;
