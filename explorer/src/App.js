import React from 'react';
import './App.css';

import { Stack, Queue } from './helpers'

class App extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      state: 'state'
    }
  }

  componentDidMount() {
    let qoo = new Queue
    this.setState({
      queue: qoo
    })
  }
 


  render() {
    return (
      <h2>Explorer</h2>
    );
  }
}

export default App;
