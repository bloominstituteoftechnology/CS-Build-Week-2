// Update with your config settings.
require('dotenv').config();
const pg = require('pg');
pg.defaults.ssl = true;

module.exports = {
  development: {
    client: 'pg',
    connection: process.env.DATABASE_URL,
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      tableName: 'knex_migrations',
      directory: './data/migrations'
    },
    seeds: {
      directory: './data/seeds'
    },
    useNullAsDefault: true
  },

  testing: {
    client: 'pg',
    connection: process.env.TEST_DATABASE_URL,
    migrations: {
      directory: './data/migrations',
      tablename: 'knex_migrations'
    },
    seeds: {
      directory: './data/seeds'
    },
    pool: {
      min: 2,
      max: 10
    },
    useNullAsDefault: true
  },

  production: {
    client: 'pg',
    connection: process.env.DATABASE_URL,
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      tableName: 'knex_migrations',
      directory: './data/migrations'
    },
    seeds: {
      directory: './data/seeds'
    },
    useNullAsDefault: true
  }
};
