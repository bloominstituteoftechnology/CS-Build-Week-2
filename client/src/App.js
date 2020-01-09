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

  const modifyExitToObject = startingRoom => {
    const copyOfstartingRoom = { ...startingRoom };
    console.log(copyOfstartingRoom);
    const exitsObj = {};
    for (let exit of copyOfstartingRoom.exits) {
      exitsObj[exit] = '?';
    }
    copyOfstartingRoom.exits = exitsObj;
    return copyOfstartingRoom;
  };

  const move = async (direction, curr, visited) => {
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
      current = modifyExitToObject(res.data);
    } catch (error) {
      console.log(error);
    }

    return [prev, current];
  };

  // ====================
  const autoMove = (cd, dir, curr, visited) => {
    const time = cd * 1000;

    return new Promise(resolve => {
      setTimeout(async () => {
        const [prev, current] = await move(dir, curr, visited);
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
    console.log('exits in unxplored++++++', room.exits);
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

    /**************************************************
     * starting room
     * 1. modify exit to object
     * 2. store modified to visited
     * 3. add to stack
     * 4. choose direction
     *    - any direction no matter if '?' or dir
     *    - hardcoded(?)
     * 5. move direction
     * 6. update/track exit graph
     **************************************************/
    let prev;
    let current;
    const stack = [];
    let visitedGraph = {};
    try {
      const modifiedObject = modifyExitToObject(startingRoom);
      let currObject = {};
      currObject[modifiedObject.room_id] = modifiedObject;
      setVisited({
        ...visited,
        ...currObject
      });
      localStorage.setItem('visited', JSON.stringify(visited));

      // populate graph with initial value

      visitedGraph = {
        ...visited
      };

      stack.push(modifiedObject);

      current = modifiedObject;
      let dir = 'n';

      [prev, current] = await autoMove(
        current.cooldown,
        dir,
        current,
        visitedGraph
      );

      // graph to visited
      const prevObj = { ...prev };
      prevObj.exits[dir] = current.room_id;
      visitedGraph[prevObj.room_id] = { ...prevObj };
      localStorage.setItem('visited', JSON.stringify(visitedGraph));

      const currObj = { ...current };
      currObj.exits[opposites[dir]] = prev.room_id;

      visitedGraph[currObj.room_id] = { ...currObj };

      localStorage.setItem('visited', JSON.stringify(visitedGraph));

      let count = 0;
      let limit = 3;

      // While 'visited' still has "?"s left unfilled...
      while (count < limit) {
        // If we haven't visited the currentRoom...
        if (!visited[current.room_id]) {
          // Add it to 'visited' with "?"s as exits
          console.log(current);
          visitedGraph[current.room_id] = current;
          localStorage.setItem('visited', JSON.stringify(visitedGraph));
        }

        // If currentRoom has unexplored exits, pick the first one and move to it, filling out exit info for new room and previous room (PUT)
        let visitedFromLocal = JSON.parse(localStorage.getItem('visited'));
        if (getUnexploredExits(visitedFromLocal[current.room_id]).length > 0) {
          const unexploredRoom = getUnexploredExits(
            visitedFromLocal[current.room_id]
          )[0];
          console.log('unexploredRoom: ', unexploredRoom);
          console.log(
            'unexplored exits: ',
            getUnexploredExits(visitedFromLocal[current.room_id])
          );

          const [prevFromMove, currentFromMove] = await autoMove(
            current.cooldown,
            unexploredRoom,
            current,
            visitedGraph
          );

          prev = prevFromMove;
          current = currentFromMove;
          // graph to visited
          const prevObj = { ...prevFromMove };
          console.log('prevObj: ', prevObj, unexploredRoom, current.room_id);
          prevObj.exits[dir] = current.room_id;

          visitedGraph[prevObj.room_id] = { ...prevObj };
          localStorage.setItem('visited', JSON.stringify(visitedGraph));

          const currObj = { ...currentFromMove };
          console.log('current: ', currObj, unexploredRoom, prev.room_id);
          currObj.exits[opposites[dir]] = prev.room_id;

          visitedGraph[currObj.room_id] = { ...currObj };

          localStorage.setItem('visited', JSON.stringify(visitedGraph));
        } else {
          // TODO: backtrack using stack to last room with "?"s
          console.log('Hit a dead end! no ?s left');
        }
        count++;
        console.log(count);
        if (count === limit) {
          console.log('Done!');
        }
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
          onClick={() =>
            autoMove(currentRoom.cooldown, 'n', currentRoom, visited)
          }
        >
          N
        </button>
        <button
          onClick={() =>
            autoMove(currentRoom.cooldown, 's', currentRoom, visited)
          }
        >
          S
        </button>
        <button
          onClick={() =>
            autoMove(currentRoom.cooldown, 'e', currentRoom, visited)
          }
        >
          E
        </button>
        <button
          onClick={() =>
            autoMove(currentRoom.cooldown, 'w', currentRoom, visited)
          }
        >
          W
        </button>
      </div>
      <button onClick={() => traverseMap(currentRoom)}>TRAVERSE!</button>
    </div>
  );
}

export default App;
