# CS Build Week 2

For your second CS Build Week, you and a small team will be competing against your fellow CS students in the ***Lambda Treasure Hunt***. To succeed, you will need to apply knowledge you've learned throughout your entire tenure at Lambda School -- CS, Labs and main track -- to efficiently traverse an island maze, collect treasure, solve puzzles, unearth powerful artifacts and more. Glory and riches await the victors!

## Roles

Each team must have a minimum of one Backend and one Frontend developer. The responsibilities will be as follows:

### Backend

As the backend developer, you will be implementing an automated traversal server. By sending POST requests to our LambdaMUD Island server and processing the response, your server will allow your team to move and collect treasure at all hours of the day and night. The teams with efficient traversal and treasure collection algorithms will find themselves prosperous.

### Frontend

As a frontend developer, you will be building a map of the island and implementing an interface to move your characters manually. You may do this by interfacing with your own backend server, connecting directly to the LambdaMUD Island server, or some combination of both (recommended).

![Lambda Treasure Hunt](img/treasure-hunt-1.png)
*Treasure Hunt interface courtesy of [Ryan Walker](http://ryanwalker.dev):*

The gods presiding over LambdaMUD Island favor beauty and elegance. Those with aesthetic interfaces might find themselves mysteriously blessed with powers throughout the week.

## Overview

You start the adventure unworthy, unequipped and anonymous. Your first task is to traverse the island and build a map for your personal use. Along the way, you will discover equipment, treasure and clues which will assist you on your quest for power, wealth and glory.

## Rooms

The map is laid out in a grid: Similar to your worlds from Week 1 of your CS training, each room may have exits in the cardinal directions: north, south, east and west. Each room also comes with a unique ID and coordinates for your convenience.

```
// Starting room
{
  "room_id": 0,
  "title": "Room 0",
  "description": "You are standing in an empty room.",
  "coordinates": "(60,60)",
  "players": [],
  "items": ["small treasure"],
  "exits": ["n", "s", "e", "w"],
  "cooldown": 60.0,
  "errors": [],
  "messages": []
}
```


## Cooldown

Your access to the server is restricted until you earn more power. Starting off, you are only allowed to make one request every 60 seconds. Sending another request before that time has elapsed will incur a penalty.

## Initialization

Test your API key with the init command. You can use this to get all relevant stats before you start moving.

`
curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/
`

This will return the following response:

```
{
  "room_id": 0,
  "title": "A Dark Room",
  "description": "You cannot see anything.",
  "coordinates": "(60,60)",
  "exits": ["n", "s", "e", "w"],
  "cooldown": 1.0,
  "errors": [],
  "messages": []
}
```

## Movement

All actions are executed via REST API commands to the Lambda Treasure Hunt server. Here is an example movement command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/
`

You will receive an authorization token following successful completion of Friday's Sprint Challenge. This serves as your unique identifier and authentication key. Don't share this key!

The URL will determine the command you are sending to the server.

Note the "direction" parameter, which determines which way you will move.


## Building your Map

Your first task is to build your map. Starting from `room 0`, you can begin to construct a graph of the map:

```
{0: {"n": "?", "s": "?", "e": "?", "w": "?"}}
```

Moving North from the starting room will return the following response:

```
{
  "room_id": 10,
  "title": "A Dark Room",
  "description": "You cannot see anything.",
  "coordinates": "(60,61)",
  "exits": ["n", "s", "w"],
  "cooldown": 100.0,
  "errors": [],
  "messages": ["You have walked north."]
}
```
This room has an ID of 10 and contains exits to the north, south and west. Now, you can fill out another entry in your graph:

```
{
  0: {"n": 10, "s": "?", "e": "?", "w": "?"},
  10: {"n": "?", "s": 0, "w": "?"}
}
```

There are a total of 500 rooms so be thoughtful about how you traverse the map. Note that you begin the hunt blind but will gain new powers as the hunt progresses.


## Wise Explorer

An accurate map is the wise explorer's best friend. By predicting the ID of the destination room, you can reduce your action cooldown by 50%. Say you are in `room 10` and moving back south to `room 0`:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"s", "next_room_id": "0"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/
`

Note the new parameter, `next_room_id`. Your map tells you that `room 0` lies south of `room 10`. This returns the following response:

```
{
  "room_id": 0,
  "title": "A Dark Room",
  "description": "You cannot see anything.",
  "coordinates": "(60,60)",
  "players": [],
  "items": [],
  "exits": ["n", "s", "e", "w"],
  "cooldown": 50.0,
  "errors": [],
  "messages": ["You have walked south.", "Wise Explorer: -50% CD"]
}
```

Note the `Wise Explorer` bonus and 50% cooldown reduction.



## Questions?

Patience: All will become clear soon enough. Here are some resources to peruse in the meantime.

* [Sample LambdaMUD spec/server](https://github.com/LambdaSchool/LambdaMUD-Project)
* [Legacy Lambda Treasure Hunt spec](https://github.com/LambdaSchool/Lambda-Treasure-Hunt)
* [Intro to Django github repo](https://github.com/LambdaSchool/Intro-Django)
* [CS12: Intro to Django: Setup, Models, and Migrations](https://www.youtube.com/watch?v=5rfCWD0jB9U)
* [CS12: Intro to Django: GraphQL and Graphene](https://www.youtube.com/watch?v=0qsOwWTo2wc)
* [CS12: Intro to Django: REST and Users](https://www.youtube.com/watch?v=yMGUq3i1qBY)
* [CS12: Intro to Django: Token Auth, GraphQL Mutations](https://www.youtube.com/watch?v=_8nTE2NE5tg)
* [Official Django documentation](https://docs.djangoproject.com/en/2.2/intro/)


