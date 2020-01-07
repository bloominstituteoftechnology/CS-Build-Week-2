import axios from 'axios';

export const axiosWithAuth = () => {
  return axios.create({
    headers: {
      'Content-Type': 'application/json',
      Authorization: 'Token e5d7abe25f73d4753b3c7e52dc06e05ae2b5c26b'
    },
    baseURL: 'https://lambda-treasure-hunt.herokuapp.com/api/'
  });
};
