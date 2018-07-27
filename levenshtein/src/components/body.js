import React from "react";
import PropTypes from "prop-types";

class Body extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (<form onSubmit={this.props.mySubmit} className='form'>
      <input onChange={this.props.setter1} value={this.props.inputs.input1} type="text" placeholder="S"/>
      <br/>
      <input onChange={this.props.setter2} value={this.props.inputs.input2} type="text" placeholder="T"/>
      <br/>
      <input className='button' type="submit" value="SUBMIT"/>
    </form>);
  }
}

export default Body;
