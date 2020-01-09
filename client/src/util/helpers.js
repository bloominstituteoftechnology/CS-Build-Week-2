const axios = require('axios');

const fs = require('fs');
const visited = {};
let currentRoom = {};

const options = {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token 64bc0785bdcd56d660079909cdd2267545dcdfa0`
  }
};
const baseURL = 'https://lambda-treasure-hunt.herokuapp.com/api/';

const writeToJson = visited => {
  fs.writeFile('../data/map.json', JSON.stringify(visited, null, 2), err => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File has been created');
  });
};

const modifyExitToObject = startingRoom => {
  const copyOfstartingRoom = { ...startingRoom };
  const exitsObj = {};
  for (let exit of copyOfstartingRoom.exits) {
    exitsObj[exit] = '?';
  }
  copyOfstartingRoom.exits = exitsObj;
  return copyOfstartingRoom;
};

const move = async (direction, curr) => {
  let prev;
  let current;
  const dirObj = { direction: direction };
  console.log(dirObj);

  axios
    .post(`${baseURL}adv/move/`, dirObj, options)
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err.response));
  // try {
  //   await axios.post(`${baseURL}adv/move/`, dirObj, options);
  //   // prev = visited[curr.room_id];
  //   // current = modifyExitToObject(res.data);
  // } catch ({ message }) {
  //   console.log(message);
  // }

  // return { prev, current };
  return dirObj;
};

const traverseMap = async startingRoom => {
  const opposites = { n: 's', s: 'n', e: 'w', w: 'e' };
  const stack = [];

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

  try {
    const modifiedObject = modifyExitToObject(startingRoom);

    visited[startingRoom.room_id] = { ...modifiedObject };
    writeToJson(visited);
    stack.push(modifiedObject);
    console.log(modifiedObject.room_id);

    // let dir = 'e'; // hardcoded val
    // console.log('hello');
    // const data = await move(dir, modifiedObject);
    // console.log(data);
    // let { prev, current } = await move(dir, modifiedObject);
    // let count = 0;

    // While 'visited' still has "?"s left unfilled...
    // while (count < 10) {
    //   // If we haven't visited the currentRoom...
    //   if (!visited[current.room_id]) {
    //     // Add it to 'visited' with "?"s as exits
    //     visited[startingRoom.room_id] = { ...modifiedObject };
    //     writeToJson(modifiedObject);
    //   }

    //   // If currentRoom has unexplored exits, pick the first one and move to it, filling out exit info for new room and previous room (PUT)
    //   if (currentRoom) {
    //     if (getUnexploredExits(visited[current.room_id]).length > 0) {
    //       const unexploredRoom = getUnexploredExits(
    //         visited[current.room_id]
    //       )[0];
    //       console.log('unexploredRoom: ', unexploredRoom);
    //       console.log(
    //         'unexplored exits: ',
    //         getUnexploredExits(visited[current.room_id])
    //       );
    //       try {
    //         [prev, current] = await autoMove(
    //           current.cooldown,
    //           unexploredRoom,
    //           current
    //         );
    //         // console.log(prev, current);

    //         const prevObj = {
    //           ...prev
    //         };
    //         console.log('CURRENT ROOM-----: ', current);
    //         console.log('PREVIOUS ROOM-----: ', prev);
    //         prevObj.exits[unexploredRoom] = current.room_id;

    //         // const prev = await updateVisited(prevObj);
    //         // setVisited({ ...visited, ...prevObj });
    //         // localStorage.setItem('visited', JSON.stringify(visited));

    //         // let nextNode = visited[current.room_id];
    //         // const nextObj = {
    //         //   ...nextNode
    //         // };
    //         current.exits[opposites[unexploredRoom]] = prev.room_id;

    //         setVisited({
    //           ...visited,
    //           [current.room_id]: current,
    //           [prevObj.room_id]: prevObj
    //         });
    //         localStorage.setItem('visited', JSON.stringify(visited));
    //       } catch (error) {
    //         console.log(error);
    //       }
    //     } else {
    //       // TODO: backtrack using stack to last room with "?"s
    //     }
    //     count++;
    //   }
    // }
  } catch ({ message }) {
    console.log(message);
  }
};

//start
const init = async () => {
  try {
    const res = await axios.get(`${baseURL}adv/init/`, options);

    currentRoom = { ...res.data };
    traverseMap(currentRoom);
  } catch ({ message }) {
    console.error(message);
  }
};
init();

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

const graphNodes = (prev, current) => {
  const prevObj = {
    ...prev
  };
  prevObj.exits[dir] = current.room_id;

  const nextObj = {
    ...current
  };
  nextObj.exits[opposites[dir]] = prev.room_id;

  return [prevObj, nextObj];
};





{"direction":"s", "next_room_id": "0"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/
POST