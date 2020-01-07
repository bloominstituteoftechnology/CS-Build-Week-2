const knex = require('knex');

const config = require('../knexfile.js');

const dbEnv = 'production';

module.exports = knex(config[dbEnv]);
