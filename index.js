require('dotenv').config();
const server = require('./server');

const port = process.env.PORT || 4500;
server.listen(port, () => {
  console.log(`
  *                         *
  *      Server Works       *
  *      at port ${port}       *
  *                         *
  *                         *
  `);
});
