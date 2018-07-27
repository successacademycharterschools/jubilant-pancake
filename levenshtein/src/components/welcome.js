import React from 'react'
import PropTypes from 'prop-types'

class Welcome extends React.Component {
  render() {
    return (<div className='welcome'>
      <h3>Levenshtein Distance</h3>
      <p>Levenshtein distance (LD) is a measure of the similarity
        <br/>
        between two strings, which we will refer to as the source
        <br/>
        string (S) and the target string (T). The distance is the number of
        <br/>
        deletions, insertions, or substitutions required to transform s into t.
      </p>
    </div>)
  }
}

export default Welcome;
