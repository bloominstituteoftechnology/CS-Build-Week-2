import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { axiosWithAuth } from './util/axiosWithAuth.js';

import './App.scss';
import Navbar from './components/Navbar';

function App() {
  const [currentRoom, setCurrentRoom] = useState();
  const [previousRoom, setPreviousRoom] = useState();
  const [visited, setVisited] = useState({});

  useEffect(() => {
    const init = () => {
      return axiosWithAuth()
        .get('adv/init/')
        .then(res => {
          setCurrentRoom(res.data);
          // postVisited(res.data)
          //   .then(() => {
          //     getVisitedInit();
          //   })
          //   .catch(err => console.log(err));
        })
        .catch(err => console.log(err));
    };
    init();
  }, []);

  useEffect(() => {
    getVisitedInit();
  }, []);

  const move = direction => {
    const dirObj = {
      direction: direction
    };
    return axiosWithAuth()
      .post('adv/move/', dirObj)
      .then(res => {
        setPreviousRoom(currentRoom);
        setCurrentRoom(res.data);
        // postVisited(res.data)
        //   .then(() => {
        //     getVisitedInit();
        //   })
        //   .catch(err => console.log(err));
      })
      .catch(err => console.log(err));
  };

  // ====================
  const autoMove = (cd, dir) => {
    const time = cd * 1000;
    setInterval(() => {
      move(dir);
    }, time); // ms
  };
  // ====================
  const postVisited = visitedNode => {
    return axios.post(
      'https://cs23-teamz-treasure-hunt.herokuapp.com/visited',
      visitedNode
    );
  };

  const updateVisited = updates => {
    return axios.put(
      `https://cs23-teamz-treasure-hunt.herokuapp.com/visited/${updates.room_id}`,
      updates
    );
  };

  const getVisitedInit = () => {
    return axios
      .get('https://cs23-teamz-treasure-hunt.herokuapp.com/visited')
      .then(res => {
        setVisited(res.data);
      })
      .then(() => traverseMap()) // currentroom
      .catch(() => console.log("You've visited that area before"));
  };

  // Checks entire 'visited' graph for unexplored exits
  const graphIsNotComplete = map => {
    let status = false;
    for (const room in map) {
      for (const exit in map[room].exits) {
        if (map[room].exits[exit] === '?') {
          status = true;
          break;
        }
      }
    }
    return status;
  };

  // Returns array of unexplored exits of a given room
  const getUnexploredExits = room => {
    let unexplored = [];
    for (const exit in room.exits) {
      if (room.exits[exit] === '?') {
        unexplored.push(exit);
      }
    }
    return unexplored;
  };

  console.log('graph is not complete? ', graphIsNotComplete(visited));

  const checkIfBothFalse = (bool1, bool2) => {
    const status = true;
    if (bool1 === false && bool2 === false) {
      status = false;
    }
    return status;
  };

  const traverseMap = startingRoom => {
    const opposites = { n: 's', s: 'n', e: 'w', w: 'e' };

    //  Start in a room
    //  Add room to OUR graph with ?s for exits (100: n: ?, s: ?)
    //  Pick an unexplored exit and move to it. Also fill out exit for new room and previous room (put request). (move n to 76: s: 100, e: ?)
    //  When we hit a dead-end aka there are no more unexplored exits, we backtrack to a room with unexplored exits

    // Use a stack to hold path list to backtrack when we reach a dead-end
    const stack = [];

    // Add currentRoom to 'visited'
    postVisited(currentRoom)
      .then(() => {
        // Add current room to stack
        stack.push(currentRoom);

        // While 'visited' still has "?"s left unfilled...
        while (graphIsNotComplete(visited)) {
          // If we haven't visited the currentRoom...
          if (!visited[currentRoom.room_id]) {
            // Add it to 'visited' with "?"s as exits
            postVisited(currentRoom);
          }

          // If currentRoom has unexplored exits, pick the first one and move to it, filling out exit info for new room and previous room (PUT)
          if (getUnexploredExits(currentRoom).length > 0) {
            const unexploredRoom = getUnexploredExits(currentRoom)[0];
            autoMove(currentRoom.cooldown, unexploredRoom);
            const prevObj = {
              ...previousRoom
            };
            prevObj.exits[unexploredRoom] = currentRoom.room_id;
            updateVisited(prevObj).then(() => {
              let nextNode = visited[currentRoom.room_id];
              const nextObj = {
                ...nextNode
              };
              nextObj.exits[opposites[unexploredRoom]] = previousRoom.room_id;
              updateVisited(nextObj);
            });
          } else {
            // TODO: backtrack using stack to last room with "?"s
          }
        }
      })
      .catch(err => console.log(err));
  };

  // OLD STUFF
  //   // While 'visited' still has "?"s left unfilled...
  //   while (
  //     // checkIfBothFalse(Object.keys(visited).length < 500, checkVisitedForQ())
  //     graphIsNotComplete(visited)
  //   ) {
  //     // Pop out first item in stack
  //     let currentNode = stack.pop();
  //     // Check if item has been visited yet
  //     if (!visited[currentNode.room_id]) {
  //       postVisited(currentNode)
  //         .then(() => {
  //           getVisitedInit().then(() => {
  //             let unexploredRoom;
  //             for (const dir in visited[currentRoom.room_id].exits) {
  //               if (visited[currentRoom.room_id].exits[dir] === '?') {
  //                 unexploredRoom = dir;
  //                 return;
  //               }
  //             }

  //             // update prev node's question to next node
  //             move(unexploredRoom);

  //             let prevNode = visited[currentRoom.room_id];
  //             const prevChangedObj = {
  //               ...prevNode
  //             };
  //             prevChangedObj.exits[unexploredRoom] = currentRoom.room_id;
  //             updateVisited(prevChangedObj);

  //             // update current node's question to previous node
  //             const currentChangedObj = {
  //               ...visited[currentRoom.room_id]
  //             };
  //             currentChangedObj.exits[opposites[unexploredRoom]] =
  //               prevNode.room_id;
  //             updateVisited(currentChangedObj);
  //             // autoMove(currentRoom.cooldown, exit); // room 76
  //           });
  //         })
  //         .catch(err => console.log(err));

  //       for (let exit in currentNode.exits) {
  //         // s
  //         autoMove(currentRoom.cooldown, exit); // room 76
  //         stack.push(currentRoom); // stack = [s: 76, w: 80, e: 50]
  //       }
  //     } else {
  //       // Handle if its already in visited obj, PUT request
  //       const changedObj = {
  //         ...currentNode,
  //         exits: { ...currentNode.exits, s: 4 }
  //       };
  //     }
  //   }
  // };

  /**
 * 
      queue = Queue()
      visited = set()
      queue.enqueue(starting_vertex)
      while queue.size() > 0:
          current_node = queue.dequeue()
          if current_node not in visited:
              visited.add(current_node)
              print("Node: ", current_node)
              for neighbor in self.get_neighbors(current_node):
                  queue.enqueue(neighbor)

 * 
 */

  console.log('visited: ', visited);
  return (
    <div className="App">
      <Navbar />

      {currentRoom && (
        <div>
          {currentRoom.title}
          <br />
          <br />
          {currentRoom.room_id}
          <br />
          <br />
          {currentRoom.description}
          <br />
          <br />
          Exits: {currentRoom.exits}
          <br />
          <br />
          Items:{' '}
          {currentRoom.items.length > 0
            ? currentRoom.items
            : 'No items in room'}
        </div>
      )}

      <div>
        <button onClick={() => move('n')}>N</button>
        <button onClick={() => move('s')}>S</button>
        <button onClick={() => move('e')}>E</button>
        <button onClick={() => move('w')}>W</button>
      </div>
    </div>
  );
}

export default App;
