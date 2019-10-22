import React from 'react';
import './CSS/App.css';
import { Promise } from 'q';
const axios = require('axios');
const token = process.env.TOKEN;

// Main axios call to api, using async and await to act as cooldown
async function playerCD(endpoint, method, data){
  try {
    let res = await axios({
      baseURL: 'https://lambda-treasure-hunt.herokuapp.com/api/',
      headers: {
          Authorization: `Token ${token}`,
          'content-Type': 'application/json'
      },
      method: `${method}`,
      url: `${endpoint}`,
      data: JSON.stringify(data)
    })
    res = await res.data
    await cooldown(res.cooldown * 1000)
    return res
  } catch (err) {
      console.error(err)
  }
}

function cooldown(cd) {
  return new Promise(resolve => setTimeout(resolve, cd))
}

function App() {
  return (
    <div className="App">
      <div className="Map">
        test
      </div>

      <div className="Info">  
        <div className="Character_stats">

        </div>
        <div className="Inventory">

        </div>
      </div>
    </div>
  );
}

export default App;

//API calls


//Map


//Play