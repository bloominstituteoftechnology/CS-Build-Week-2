const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const cors = require('cors');

const server = express();

const nodeRouter = require('./routes/nodeRouter');

server.use(express.json());
server.use(morgan('dev'));
server.use(helmet());
server.use(cors());

server.use('/visited', nodeRouter);

server.use('/', (req, res) => {
  res.send(`
    <h1>Server Works</h1>
  `);
});

module.exports = server;
