exports.up = function(knex) {
  return knex.schema.createTable('node', tbl => {
    tbl.increments('id');
    tbl
      .integer('room_id')
      .notNullable()
      .unique();
    tbl.string('title').notNullable();
    tbl.string('description').notNullable();
    tbl.json('coordinates').notNullable();
    tbl.json('exits').notNullable();
    tbl.float('cooldown', 8, 1).notNullable();
    tbl.json('errors').notNullable();
    tbl.json('messages').notNullable();
  });
};

exports.down = function(knex) {
  return knex.schema.dropTableIfExists('node');
};

/**
 *   "room_id": 0,
  "title": "A Dark Room",
  "description": "You cannot see anything.",
  "coordinates": "(60,60)",
  "exits": ["n", "s", "e", "w"],
  "cooldown": 1.0,
  "errors": [],
  "messages": []
 */
