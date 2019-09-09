const express = require('express');
const server = express();
// const db = require('./data/dbHelpers');
const cors = require('cors');
const axios = require('axios');

// -------- Pseudo DB until static db is created ----------

class Room {
  constructor(room_id, title, coordinates, items, exits, cooldown) {
    this.room_id = room_id;
    this.title = title;
    this.coordinates = coordinates;
    this.items = items;
    this.exits = exits;
    this.cooldown = cooldown;
  }
}

var stack = [];

server.use(express.json(), cors());

const PORT = 5050;

const getUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/';
const moveUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/';
const params = {
  TOKEN: '65ef3fd1d9226f97f50a440cb4dd09b64e0d6a8c'
};

async function getRoom() {
  const config = {
    method: 'get',
    url: getUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    }
  };
  let res = await axios(config).catch(err => console.log(err));
  const room = new Room(
    res.data.room_id,
    res.data.title,
    res.data.coordinates,
    res.data.items,
    res.data.exits,
    res.data.cooldown
  );
  stack.push(room);
  console.log(room);
}

async function move() {
  const config = {
    method: 'post',
    url: moveUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      direction: 'n'
    }
  };
  await axios({
    method: config.method,
    url: moveUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

//getRoom();
move();

server.listen(PORT, () => {
  console.log(`Server is listening on Port ${PORT}`);
});
