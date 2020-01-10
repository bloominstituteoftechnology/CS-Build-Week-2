import React, { useState } from 'react';
import data from '../data/test.json';

const Treasure = ({ currentRoom }) => {
  const [pathState, setPathState] = useState([]);
  const [bfs, setBfs] = useState('');

  const handleChange = e => {
    setBfs(e.target.value);
  };

  const traverseHandler = e => {
    e.preventDefault();
    bfsTraverse(currentRoom, bfs);
  };

  const bfsTraverse = async (startingVertex, target_id) => {
    startingVertex = data[0];

    const q = [];
    q.unshift([startingVertex]);
    const visited = {};
    while (q.length > 0) {
      let path = q.pop();
      let v = path[path.length - 1];
      if (!visited[v.room_id]) {
        visited[v.room_id] = path;

        for (const neighbors in data[v.room_id].exits) {
          if (data[v.room_id].room_id === Number(target_id)) {
            console.log('found!!! :)   ', path);
            setPathState(path);
            return path;
          }

          if (data[v.room_id].exits[neighbors] !== '?') {
            const new_path = [...path, data[data[v.room_id].exits[neighbors]]];
            q.unshift(new_path);
          }
        }
      }
      if (q.length === 0) {
        console.log('done!');
      }
    }
  };

  return (
    <>
      <div>
        <p>Starting: {currentRoom ? currentRoom.title : 'NA'}</p>
        <p>
          Destination:{' '}
          {pathState.length ? pathState[pathState.length - 1].title : 'NA'}
        </p>
        <p>Steps: {pathState.length && pathState.length}</p>
      </div>
      <form onSubmit={traverseHandler}>
        <label htmlFor="bfs">Find room path: </label>
        <input
          type="text"
          name="bfs"
          value={bfs}
          id="bfs"
          placeholder="Enter Room here"
          onChange={handleChange}
        />
        <button type="submit">Submit</button>
      </form>
    </>
  );
};

export default Treasure;
