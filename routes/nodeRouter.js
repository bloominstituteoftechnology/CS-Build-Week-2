const express = require('express');
const db = require('../data/dbConfig');

const router = express.Router();

router.get('/', async (req, res) => {
  try {
    const data = await db('node');
    console.log(data);
    res.status(200).json(data);
  } catch ({ message }) {
    console.error(message);
    res.status(500).json({ message });
  }
});

router.post('/', async (req, res) => {
  const {
    room_id,
    title,
    description,
    coordinates,
    exits,
    cooldown,
    errors,
    messages
  } = req.body;
  if (
    !room_id ||
    !title ||
    !description ||
    !coordinates ||
    !exits ||
    !cooldown ||
    !errors ||
    !messages
  ) {
    res.status(422).json({ message: 'missing fields required' });
  }
  try {
    const data = await db('node').insert({
      room_id,
      title,
      description,
      coordinates,
      exits: JSON.stringify(exits),
      cooldown,
      errors: JSON.stringify(errors),
      messages: JSON.stringify(messages)
    });
    console.log(data);
    res.status(201).json({ message: 'node has been created' });
  } catch ({ message }) {
    console.error(message);
    res.status(500).json({ message });
  }
});

router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    await db('node')
      .where({ id })
      .del();
    res.status(200).json({ message: `node has been deleted` });
  } catch ({ message }) {
    console.error(message);
    res.status(500).json({ message });
  }
});

module.exports = router;
