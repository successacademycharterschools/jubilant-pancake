import React from 'react'
import PropTypes from 'prop-types'
import image from "../math.gif";

class Instructions extends React.Component {
  render() {
    return (<div className='instructions'>
      <img src={image} className='image'/>
      <p>Enter a string into the input labled "S", and a second string
        <br/>
        into the input labled "T" to get a result!</p>
    </div>)
  }
}

export default Instructions;
