exports.up = function(knex) {
  return knex.schema.createTable('node', tbl => {
    tbl.increments('id');
    tbl.integer('room_id');
    tbl.string('title');
    tbl.string('description');
    tbl.string('coordinates');
    tbl.json('exits');
    tbl.decimal('cooldown', 8, 1);
    tbl.json('errors');
    tbl.json('messages');
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
