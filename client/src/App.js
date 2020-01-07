import React, { useState, useEffect } from 'react';
import { axiosWithAuth } from './util/axiosWithAuth.js';

import './App.scss';
import Navbar from './components/Navbar';

function App() {
  const [currentRoom, setCurrentRoom] = useState();

  useEffect(() => {
    const init = () => {
      return axiosWithAuth()
        .get('adv/init/')
        .then(res => setCurrentRoom(res.data))
        .catch(err => console.log(err));
    };
    init();
  }, []);

  return (
    <div className="App">
      <Navbar />

      {currentRoom && (
        <div>
          {currentRoom.title}
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
    </div>
  );
}

export default App;
