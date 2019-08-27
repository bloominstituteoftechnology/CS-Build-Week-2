import React from 'react';
import './App.css';
import axios from 'axios'

import { Stack, Queue, getRandomDirection, getRandomInt } from './helpers'

class App extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      state: 'state',
      currentRoom: null
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
    // console.log(Object.keys(graph).length)
    // Object.keys(myArray).length

    while (Object.keys(graph).length < 500) {
        for (var key in graph) {
          console.log(`console logging keys ${key}`)
        }
        // console.log(`graph is this long ${Object.keys(graph).length}`)

        let notExplored = []

        const exits = this.state.currentRoom.exits
        console.log(`exits ${exits}`)

        const current = this.state.currentRoom.room_id
        console.log(`current room ${current}`)

        if (!graph[current]) {
            graph[current] = {}
            console.log(graph[current])
            for (var x in exits) {
                graph[current][exits[x]] = '?'
            }
        } else {
          console.log('this is already in the graph')
        }
        
        for (var room in graph[current]) {
            console.log(room)
            if (graph[current][room] == "?") {
                notExplored.push(room)
                console.log(`the not explored array is ${typeof notExplored}`)
            } 
          }

        if (notExplored.length > 0) {
            console.log(`not explored length is ${notExplored}`)
            let nextMove = getRandomDirection(notExplored)

            console.log(`our next move will be ${nextMove}`)

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
 
movePlayer = (dir) => {

  console.log(`moving player to the ${dir}`)

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
  }

  const data = {
    direction: dir
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

      

      {this.state.currentRoom ?
      <>
        <h4>You're in {this.state.currentRoom.title}</h4>
        <h4>And {this.state.currentRoom.description}</h4>
        <h2>There are exits to the:</h2> 
         {this.state.currentRoom.exits.map(exit => 
          <p>{exit}</p>
        )}
        <h4>Messages:</h4><p>{this.state.currentRoom.messages}</p>
        <h4>Cooldown:</h4><p>{this.state.currentRoom.cooldown}</p>  
        <h4>Errors:</h4><p>{this.state.currentRoom.errors}</p>    
      </>
      : null
      }
     

      <button onClick={()=>this.movePlayer('w')}>Go West</button>
      <button onClick={()=>this.movePlayer('e')}>Go East</button>
      <button onClick={()=>this.movePlayer('n')}>Go North</button>
      <button onClick={()=>this.movePlayer('s')}>Go South</button>
      </>

// {
//   "room_id": 0,
//   "title": "A Dark Room",
//   "description": "You cannot see anything.",
//   "coordinates": "(60,60)",
//   "exits": ["n", "s", "e", "w"],
//   "cooldown": 1.0,
//   "errors": [],
//   "messages": []
// }
    );
  }
}

export default App;
