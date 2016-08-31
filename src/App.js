import React, { Component } from 'react';
import './App.css';

class App extends Component {
    constructor() {
        super();

        this.state = {data: '...'};

        this.getEditDistance = this.getEditDistance.bind(this);
    };

    getEditDistance(){
        var matrix = [],
            word1 = document.getElementById('word1').value,
            word2 = document.getElementById('word2').value;

        if(word1.length === 0) return word2.length;
        if(word2.length === 0) return word1.length;

        for(var i = 0; i <= word2.length; i++){
            matrix[i] = [i];
        }

        for(var j = 0; j <= word1.length; j++){
            matrix[0][j] = j;
        }

        for(i = 1; i <= word2.length; i++){
            for(j = 1; j <= word1.length; j++){
                if(word2.charAt(i - 1) === word1.charAt(j - 1)){
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] =
                        Math.min(matrix[i - 1][j - 1] + 1,
                        Math.min(matrix[i][j - 1] + 1,
                            matrix[i - 1][j] + 1));
                }
            }
        }

        this.setState({data: matrix[word2.length][word1.length]});
    }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Edit Distance: <span id="distance">{this.state.data}</span></h2>
        </div>
          <div className="App-intro">
              <label htmlFor="word1">A:&nbsp;</label>
              <input id="word1" type="text" onChange={this.getEditDistance}/>
              <br />
              <label htmlFor="word2">B:&nbsp;</label>
              <input id="word2" type="text" onChange={this.getEditDistance}/>
              <br />
          </div>
      </div>
    );
  }
}

export default App;
