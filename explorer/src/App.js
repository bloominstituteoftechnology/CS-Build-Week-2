import React from 'react';
import './App.css';
import axios from 'axios'

import { Stack, Queue, getRandomDirection, getRandomInt } from './helpers'

class App extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      state: 'state',
      currentRoom: {}
    }
  }

  componentDidMount() {
    let qoo = new Queue()
    this.setState({
      queue: qoo
    })
  }

  makePath = () => {

    console.log("firing button")

    let graph = {}
    let path = []
    console.log(graph.length, path)
    // Object.keys(myArray).length

    while (Object.keys(graph).length < 500) {
        console.log(`graph is this long ${graph.length}`)
        localStorage.setItem('map', JSON.stringify(graph))

        let notExplored = []

        const exits = this.state.currentRoom.exits

        const current = this.state.currentRoom.room_id

        if (!(current in graph)) {
            graph[current] = {}
            for (var x in exits) {
                graph[current][exits[x]] = '?'
            }
        }
        
        for (var room in graph[current]) {
            console.log(room)
            if (graph[current][room] == "?") {
                notExplored.push(room)
            } 
          }

        if (notExplored.length > 0) {
            let nextMove = getRandomDirection(notExplored)

            this.movePlayer(nextMove)

            graph[current][nextMove] = this.state.currentRoom.room_id
            path.push(nextMove)
            notExplored = []
        } else {
            let q = new Queue()
            q.enqueue([current])

            let checked = []
            let returnPath = []

            while (q.size() > 0) {
                let checkPath = q.dequeue()
                let v = checkPath.slice(-1)[0]


                if (!(v in returnPath)) {
                    let exists = Object.keys(graph[v]).some(function(k) {
                        return returnPath[k] === "?";
                    });
                    if (exists == true) {
                        returnPath = checkPath
                        break
                    }
                    returnPath.push(v)
                    for (var way in graph[v]) {
                        let new_path = [...checkPath]
                        new_path.push(graph[v][way])
                        q.enqueue(new_path)
                    }
                }
            }

            let steps = []

            for (var i = 0; i < returnPath.length - 1; i++) { 
                for (var direction in graph[returnPath[i]]) {
                    if (graph[returnPath[i]][direction] == returnPath[i + 1]) {
                        steps.push(direction)
                    }
                }
                path = path.concat(steps)
                for (var step in steps) {
                    this.movePlayer(step)
                }
              }
            
        }
    }

    return path
}
 
movePlayer = (direction) => {

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
  }

  const data = {
    direction: 'e'
  }
  
  axios(
    {
      method: 'post', //you can set what request you want to be
      url: 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/',
      data: data,
      headers: {
        Authorization: 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
      }
    }
  )
    .then((res) => {
      console.log(res)
      this.setState({
        currentRoom: res.data
      })
    })
    .catch((err) => {
      console.log(err)
    })
}

startGame = () => {

  const headers = {
    'Authorization': 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
  }
  
  axios
    .get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', {headers})
    .then((res) => {
      console.log(res)
      this.setState({
        currentRoom: res.data
      })
    })
    .catch((err) => {
      console.log(err)
    })
}

  render() {
    return (
      <>
      <h2>Explorer</h2>
      <button onClick={this.startGame}>Start Game</button>
      <button onClick={this.movePlayer}>Move Player</button>
      <button onClick={this.makePath}>Start Exploring</button>
      </>
    );
  }
}

export default App;
