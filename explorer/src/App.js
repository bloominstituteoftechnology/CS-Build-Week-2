import React from 'react';
import './App.css';
import axios from 'axios'

import { Stack, Queue, getRandomDirection, getRandomInt, flipDirection } from './helpers'

class App extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      state: 'state',
      currentRoom: null,
      errors: null,
      graph: {},
      cooling: false,
      lastRoom: null
    }
  }

  componentDidMount() {
    // let qoo = new Queue()
    // if (Object.keys(this.state.graph).length < 1 && localStorage.getItem('map')) {
    //   var map = localStorage.getItem('map')
    //   this.setState({
    //     graph: map
    //   })
      
    // }
  }

  makePath = () => {

    console.log("firing button")

    let graph = {}
    let path = []
    // console.log(Object.keys(graph).length)
    // Object.keys(myArray).length

    // while (Object.keys(this.state.graph).length < 500) {
    while (this.state.currentRoom.room_id !== 250) {
        
        console.log(`the graph's length is ${Object.keys(this.state.graph).length}`)
        console.log(`Path is ${path}`)
        let notExplored = []

        const exits = this.state.currentRoom.exits
        console.log(`exits ${exits}`)

        const current = this.state.currentRoom.room_id
        console.log(`current room ${current}`)

        if (!this.state.graph[this.state.currentRoom.room_id]) {

          let newRoom = {
            room_title: '',
            exits: {}
          }
          newRoom['room_title'] = this.state.currentRoom.title
          for (var x in exits) {
            newRoom['exits'][exits[x]] = '?'
          }
          
          this.setState({
            graph: {
              ...this.state.graph,
              [current]: newRoom 
                }
          })

          localStorage.setItem('map', JSON.stringify(this.state.graph))
        } else {
          console.log('this is already in the graph')
        }
        
        console.log(this.state.graph[current])
        for (var room in this.state.graph[current]['exits']) {
            console.log(room)
            if (this.state.graph[current]['exits'][room] == "?") {
                notExplored.push(room)
                console.log(`the not explored array is ${notExplored}`)
            } 
          }

        let nextMove = getRandomDirection(notExplored)  
        this.movePlayer(nextMove)

    //     if (notExplored.length > 0) {
    //         console.log(`not explored length is ${notExplored.length}`)
    //         let nextMove = getRandomDirection(notExplored)

    //         console.log(`our next move will be ${nextMove}`)

    //         this.movePlayer(nextMove)
            
    //         path.push(nextMove)
    //         notExplored = []
    //     } else {
    //         let q = new Queue()
    //         q.enqueue([current])

    //         let checked = []
    //         let returnPath = []

    //         while (q.size() > 0) {
    //             let checkPath = q.dequeue()
    //             console.log(`checkpath is ${checkPath}`)
    //             let v = checkPath.slice(-1)[0]
    //             console.log(v)
    //             console.log(this.state.graph[v])

    //             if (!(v in returnPath)) {
    //                 let exists = Object.keys(this.state.graph[v]['exits']).some(function(k) {
    //                     return returnPath[k] === "?";
    //                 });
    //                 if (exists == true) {
    //                     returnPath = checkPath
    //                     break
    //                 }
    //                 returnPath.push(v)
    //                 for (var way in this.state.graph[v]['exits']) {
    //                     let new_path = [...checkPath]
    //                     new_path.push(this.state.graph[v]['exits'][way])
    //                     q.enqueue(new_path)
    //                 }
    //             }
    //         }

    //         let steps = []

    //         for (var i = 0; i < returnPath.length - 1; i++) { 
    //             for (var direction in this.state.graph[returnPath[i]]) {
    //                 console.log(`steps loop direction is ${direction}`)
    //                 console.log(`returnpath[i] is ${returnPath[i]}`)
    //                 if (this.state.graph[returnPath[i]][direction] == returnPath[i + 1]) {
    //                     steps.push(direction)
    //                 }
    //             }
    //             path = path.concat(steps)
    //             for (var step in steps) {
                  
    //               this.movePlayer(steps[step])
    //             }
    //           }       
    //     }
    }

    return path
}
 
movePlayer = (dir) => {


  console.log(`moving player to the ${dir}`)

  var exits = this.state.currentRoom.exits

  let newRoom = {
    room_title: '',
    exits: {}
  }
  newRoom['room_title'] = this.state.currentRoom.title

    for (var x in exits) {
      newRoom['exits'][exits[x]] = '?'
    }
    
    this.setState({
      graph: {
        ...this.state.graph,
        [this.state.currentRoom.room_id]: newRoom 
          }
    })

    localStorage.setItem('map', JSON.stringify(this.state.graph))
  
  // if (!this.state.graph[this.state.currentRoom.room_id]) {
  //   this.state.graph[this.state.currentRoom.room_id] = {
  //                                                   room_title: '',
  //                                                   exits: {}
  //                                                 }
  //   this.state.graph[this.state.currentRoom.room_id]['room_title'] = this.state.currentRoom.title
  //   // console.log(this.state.graph[this.state.currentRoom.room_id])
  //   for (var x in exits) {
  //     this.state.graph[this.state.currentRoom.room_id]['exits'][exits[x]] = '?'
  //   }
  //   localStorage.setItem('map', JSON.stringify(this.state.graph))
  // } else {
  //   console.log('this is already in the graph')
  // }

  this.sleep(10001)

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
  }

  const data = {
    direction: dir
  }

  console.log(`data is ${data.direction} ${typeof data.direction}`)
  
  // return new Promise((resolve, reject) => {
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
      console.log('Made my API request')

      console.log(`resetting ${this.state.graph[this.state.currentRoom.room_id]['exits'][dir]} to ${res.data.room_id}`)
      this.setState({
        graph: {
          ...this.state.graph, 
          [this.state.graph[this.state.currentRoom.room_id]['exits'][dir]]: [res.data.room_id],
          // [this.state.graph[res.data.room_id][flipDirection(dir)]] : this.state.currentRoom.room_id
        }
      })
      // this.state.graph[this.state.currentRoom.room_id]['exits'][dir] = res.data.room_id
      localStorage.setItem('map', JSON.stringify(this.state.graph))
      
      
      this.setState({
          currentRoom: res.data
        })
        console.log(`current room is ${this.state.currentRoom.room_id}`)
        
      // resolve(res)

      })
      .catch((err) => {
        console.log('Error thrown', err)
        // reject(err)
        this.setState({
          errors: err.data
        })
      })
  }
// }

sleep = (delay) => {
  console.log(`sleeping for ${delay} seconds`)
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

startGame = () => {

  if (localStorage.getItem('map')) {
    var map = JSON.parse(localStorage.getItem('map'))
    this.setState({
      graph: map
    })
    
  }

  const headers = {
    'Authorization': 'Token 314369d39e5bdc8abb7f7c40689cb34de2d56669'
  }
  
  axios
    .get('https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', {headers})
    .then((res) => {
      console.log(res)
      var exits = res.data.exits
      var starterGraph = {[res.data.room_id]: {
                                        room_title: res.data.title,
                                        exits: {}
                                      }}

      for (var x in exits) {
        console.log(starterGraph, exits[x])
        starterGraph[res.data.room_id]['exits'][exits[x]] = '?'
    }

    this.setState({
      currentRoom: res.data,
    })
    console.log(starterGraph)
      if (Object.keys(this.state.graph).length < 1) {
        this.setState({
          graph: starterGraph
        })
        localStorage.setItem('map', JSON.stringify(this.state.graph))
      }
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
        <h4>You're in room {this.state.currentRoom.room_id} with the title {this.state.currentRoom.title}</h4>
        <h4>And {this.state.currentRoom.description}</h4>
        <h2>There are exits to the:</h2> 
         {this.state.currentRoom.exits.map(exit => 
          <p>{exit}</p>
        )}
        <h4>Messages:</h4><p>{this.state.currentRoom.messages}</p>
        <h4>Cooldown:</h4><p>{this.state.currentRoom.cooldown}</p> 
        <h4>Treasure:</h4>
        {this.state.currentRoom.items.map(item => 
          <p>{item}</p>
        )}
      </>
      : null
      }
     {this.state.errors ?
     <div>
        <h4>Errors:</h4>
        {this.state.errors.errors.map(err => 
          <p>{err}</p>
        )}
        <p>{this.state.errors.cooldown}</p> 
        </div>
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
