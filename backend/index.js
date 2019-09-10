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
// // Uncomment These as you need them...
const takeUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/';
const dropUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/';
const sellUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/';
// const statusUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/';
const examineUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/';
// const wearUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/';
// const changeNameUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/';
// const prayUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/';
// const flyUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/';
// const dashUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/';
// const carryUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/';
// const receiveUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/';
// const mineUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/';
// const proofUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/';
// const balanceUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/';
// const transmorgrifyUrl = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/transmogrify/';
const params = {
  // // K-token
  // TOKEN: '65ef3fd1d9226f97f50a440cb4dd09b64e0d6a8c'
  // // B-token
  TOKEN: '75578be1cf6136d88fb6b170e43b7da71dea5f84'
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

async function take() {
  const config = {
    method: 'post',
    url: takeUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      name: 'treasure'
    }
  };
  await axios({
    method: config.method,
    url: takeUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

async function drop() {
  const config = {
    method: 'post',
    url: dropUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      name: 'treasure'
    }
  };
  await axios({
    method: config.method,
    url: dropUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

async function sell() {
  const config = {
    method: 'post',
    url: sellUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      name: 'treasure'
    }
  };
  await axios({
    method: config.method,
    url: sellUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

async function confirmSell() {
  const config = {
    method: 'post',
    url: sellUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      name: 'treasure',
      confirm: 'yes'
    }
  };
  await axios({
    method: config.method,
    url: sellUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

// status function here

async function examine() {
  const config = {
    method: 'post',
    url: examineUrl,
    headers: {
      Authorization: `Token ${params.TOKEN}`
    },
    body: {
      name: 'treasure'
    }
  };
  await axios({
    method: config.method,
    url: examineUrl,
    data: config.body,
    headers: config.headers
  })
    .then(res => {
      console.log(res.data);
    })
    .catch(err => console.log(err));
}

getRoom();
// move();
// take();
// drop();
// sell();
// confirmSell();
// status();
// examine();




server.listen(PORT, () => {
  console.log(`Server is listening on Port ${PORT}`);
});
