import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { axiosWithAuth } from './util/axiosWithAuth.js';

import './App.scss';
import Navbar from './components/Navbar';

function App() {
  const [currentRoom, setCurrentRoom] = useState();
  const [previousRoom, setPreviousRoom] = useState();
  const [visited, setVisited] = useState({});
  const [graph, setGraph] = useState({});

  useEffect(() => {
    const init = () => {
      return axiosWithAuth()
        .get('adv/init/')
        .then(res => {
          setCurrentRoom(res.data);
        })
        .catch(err => console.log(err));
    };
    setVisited(JSON.parse(localStorage.getItem('visited')));
    init();
  }, []);

  useEffect(() => {
    if (currentRoom) {
      console.log('CURRENT ROOM CHANGED');
      console.log(currentRoom.room_id);
      const func = async () => {
        const objtest = {};
        const copyOfCurrentRoom = {
          ...currentRoom
        };
        const exitsObj = {};
        for (let exit of copyOfCurrentRoom.exits) {
          exitsObj[exit] = '?';
        }
        copyOfCurrentRoom.exits = exitsObj;
        objtest[currentRoom.room_id] = copyOfCurrentRoom;
        setVisited({
          ...visited,
          ...objtest
        });
      };
      func();
    }
  }, [currentRoom]);

  const move = async (direction, curr) => {
    const dirObj = {
      direction: direction
    };

    let prev;
    let current;

    try {
      setPreviousRoom(visited[curr.room_id]);
      const res = await axiosWithAuth().post('adv/move/', dirObj);
      setCurrentRoom(res.data);
      prev = visited[curr.room_id];
      current = res.data;
    } catch (error) {
      console.log(error);
    }
    return [prev, current];
  };

  // ====================
  const autoMove = (cd, dir, curr) => {
    const time = cd * 1000;

    return new Promise(resolve => {
      setTimeout(async () => {
        const [prev, current] = await move(dir, curr);
        resolve([prev, current]);
      }, time); // ms
    });
  };

  // TODO! ******************
  // // Get treasure
  // const getTreasure = () => {
  //   return axiosWithAuth().post('adv/take/')
  // }

  // ====================
  const postVisited = async visitedNode => {
    try {
      await axios.post(
        'https://cs23-teamz-treasure-hunt.herokuapp.com/visited',
        visitedNode
      );
    } catch (error) {
      console.log("You've visited that area before");
    }
  };

  const updateVisited = async updates => {
    try {
      await axios.put(
        `https://cs23-teamz-treasure-hunt.herokuapp.com/visited/${updates.room_id}`,
        updates
      );
    } catch (error) {
      console.log(error);
    }
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

  // console.log('graph is not complete? ', graphIsNotComplete(visited));

  const traverseMap = async startingRoom => {
    const opposites = { n: 's', s: 'n', e: 'w', w: 'e' };

    //  Start in a room
    //  Add room to OUR graph with ?s for exits (100: n: ?, s: ?)
    //  Pick an unexplored exit and move to it. Also fill out exit for new room and previous room (put request). (move n to 76: s: 100, e: ?)
    //  When we hit a dead-end aka there are no more unexplored exits, we backtrack to a room with unexplored exits

    // Use a stack to hold path list to backtrack when we reach a dead-end
    const stack = [];

    // Add currentRoom to 'visited'
    // const visited = {};
    // visited[currentRoom.room_id] = currentRoom;
    // localStorage.setItem('visited', JSON.stringify(visited));
    const objtest = {};
    const copyOfCurrentRoom = {
      ...currentRoom
    };
    const exitsObj = {};
    for (let exit of copyOfCurrentRoom.exits) {
      exitsObj[exit] = '?';
    }
    copyOfCurrentRoom.exits = exitsObj;
    objtest[currentRoom.room_id] = copyOfCurrentRoom;
    setVisited({
      ...visited,
      ...objtest
    });
    let prev;
    let current = copyOfCurrentRoom;
    try {
      stack.push(currentRoom);

      let count = 0;

      // While 'visited' still has "?"s left unfilled...
      while (count < 10) {
        console.log('visited: ', visited);
        // If we haven't visited the currentRoom...
        if (!visited[current.room_id]) {
          // Add it to 'visited' with "?"s as exits
          const objtest = {};
          const copyOfCurrentRoom = {
            ...current
          };
          const exitsObj = {};
          for (let exit of copyOfCurrentRoom.exits) {
            exitsObj[exit] = '?';
          }
          copyOfCurrentRoom.exits = exitsObj;
          objtest[current.room_id] = copyOfCurrentRoom;
          setVisited({
            ...visited,
            ...objtest
          });
        }

        // If currentRoom has unexplored exits, pick the first one and move to it, filling out exit info for new room and previous room (PUT)
        if (getUnexploredExits(visited[current.room_id]).length > 0) {
          const unexploredRoom = getUnexploredExits(
            visited[current.room_id]
          )[0];
          console.log('unexploredRoom: ', unexploredRoom);
          console.log(
            'unexplored exits: ',
            getUnexploredExits(visited[current.room_id])
          );
          try {
            [prev, current] = await autoMove(
              current.cooldown,
              unexploredRoom,
              current
            );
            // console.log(prev, current);

            const prevObj = {
              ...prev
            };
            console.log('CURRENT ROOM-----: ', current);
            console.log('PREVIOUS ROOM-----: ', prev);
            prevObj.exits[unexploredRoom] = current.room_id;

            // const prev = await updateVisited(prevObj);
            // setVisited({ ...visited, ...prevObj });
            // localStorage.setItem('visited', JSON.stringify(visited));

            // let nextNode = visited[current.room_id];
            // const nextObj = {
            //   ...nextNode
            // };
            current.exits[opposites[unexploredRoom]] = prev.room_id;

            setVisited({
              ...visited,
              [current.room_id]: current,
              [prevObj.room_id]: prevObj
            });
            localStorage.setItem('visited', JSON.stringify(visited));
          } catch (error) {
            console.log(error);
          }
        } else {
          // TODO: backtrack using stack to last room with "?"s
        }
        count++;
      }
    } catch (error) {
      console.log(error);
    }
  };
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
  console.log('state', visited);
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
        <button
          onClick={() => autoMove(currentRoom.cooldown, 'n', currentRoom)}
        >
          N
        </button>
        <button
          onClick={() => autoMove(currentRoom.cooldown, 's', currentRoom)}
        >
          S
        </button>
        <button
          onClick={() => autoMove(currentRoom.cooldown, 'e', currentRoom)}
        >
          E
        </button>
        <button
          onClick={() => autoMove(currentRoom.cooldown, 'w', currentRoom)}
        >
          W
        </button>
      </div>
      <button onClick={() => traverseMap()}>TRAVERSE!</button>
    </div>
  );
}

export default App;
