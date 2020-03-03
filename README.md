# CS Build Week 2

For your second CS Build Week, you and a small team will be competing against your fellow CS students in the ***Lambda Treasure Hunt***. To succeed, you will need to apply knowledge you've learned throughout your entire tenure at Lambda School -- CS, Labs and main track -- to efficiently traverse an island maze, collect treasure, solve puzzles, unearth powerful artifacts and more. Glory and riches await the victors!

## Minimum Viable Product

Mine one Lambda Coin. That's it.


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

Your access to the server is restricted until you earn more power. Starting off, you are only allowed to make one request every 15 seconds. Sending another request before that time has elapsed will incur a penalty. The cooldown may decrease as the days wear on - make sure to keep an eye on your cohort's channel for important updates.

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

***You will be able to progress with future tasks much more quickly if you log ALL room info during your initial traversal / map building (not just room numbers & exits)***


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


## Treasure

You may have noticed the small treasure lying in the room. You can pick it up with the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/take/
`

You may drop items with the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/drop/
`

Note to collect enough treasure for later tasks, you'll want to automate the process of traversing the graph (once your map is complete) and picking up treasure

## Selling Treasure

First, you must find the shop. It's not too far from your starting location. Once you do, you can offer your treasure in exchange for gold.

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/
`

This will return:

```
{
  "room_id": "?",
  "title": "Shop",
  "description": "You are standing in a shop. You can sell your treasure here.",
  "coordinates": "?",
  "players": [],
  "items": [],
  "exits": ["e"],
  "cooldown": 2.0,
  "errors": [],
  "messages": ["I'll give you 100 gold for that Small Treasure.", "(include 'confirm':'yes' to sell Small Treasure)"]
}
```

Confirm the sale with the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"treasure", "confirm":"yes"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/
`

## Buy

You may find a shop that sells goods as well. You can buy with the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"donut"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/buy/
`

This will also ask for confirmation before completing the transaction:
`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"donut", "confirm":"yes"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/buy/
`


## Status, Inventory

You can check your status and inventory using the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
`

```
{
  "name": "br80",
  "cooldown": 2.0,
  "encumbrance": 2,  // How much are you carrying?
  "strength": 10,  // How much can you carry?
  "speed": 10,  // How fast do you travel?
  "gold": 400,
  "bodywear": "None",
  "footwear": "None",
  "inventory": ["Small Treasure"],
  "status": [],
  "errors": [],
  "messages": []
}
```


## Examine

You can examine players or items in your room or inventory using this command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF ITEM OR PLAYER]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/
`

## Equipment

Certain items can be worn on either your feet or your body for boosts in speed and/or power. You may wear items with this command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF WEARABLE]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/wear/
`

You may remove items with this command:
`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF WEARABLE]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/undress/
`

## Name Changer

You can change your name once you find the name changer using the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NEW NAME]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/change_name/
`

Without changing your name, you will be unable to mine Lambda Coins. Changing your name will require 1000 gold, so make sure you get started on collecting treasure early on.

## Shrine

If you find a shrine, you may pray at the shrine to earn some new powers:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/pray/
`

## Flight

Once earning the power of flight, you may use this ability to avoid movement penalties on elevated terrain:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/fly/
`


## Dash

Once mastering the dash, you may use this ability to cover many rooms in one direction quickly:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"direction":"n", "num_rooms":"5", "next_room_ids":"10,19,20,63,72"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/dash/
`

Formatting is very important for these commands: next_room_ids must match every room in a straight line and num_rooms must be the exact count for the dash to work successfully.


## Carry/Receive

You may come across a ghostly companion ease your encumbrance by holding your heaviest item:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[ITEM_NAME]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/carry/
`

If your item is being carried, you may receive it back using the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/receive/
`


## Warp

You may come across the ability to warp to an alternate dimension where you can compete with other players to search for the mysterious golden snitch. Note that warp travel is dangerous so you must be have both bodywear and footwear equipped to warp.

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/warp/
`

## Recall

You may come across the ability to recall to your starting location.

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/recall/
`


# Lambda Coins

Once you acquire your true name, you should seek out the wishing well. Peer into the waters of the well and you will find a clue that will lead you to the location of your Lambda Coin, eager to be mined with a valid proof.

You may mine for Lambda Coins using the following API endpoints:


## Mine
Submit a proposed proof and your game token to this endpoint to attempt to mine a block.  If successful, you will receive a Lambda Coin. First, you will need to find the appropriate room.


`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"proof":new_proof}' https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/
`

## Proof

Get the last valid proof to use to mine a new block.  Also returns the current difficulty level, which is the number of `0`'s required at the beginning of the hash for a new proof to be valid.  

The proof of work algorithm for this blockchain is not the same as we used in class. It uses a different method:

Does hash(last_proof, proof) contain N leading zeroes, where N is the current difficulty level?

`
curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/
`

```
{
  "proof": 123456,
  "difficulty": 8,
  "cooldown": 1.0,
  "messages": [],
  "errors": []
}
```

## Balance

Get your Lambda Coin balance.

`
curl -X GET -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/
`

```
{
   "cooldown": 1.0,
   "messages": ["You have a balance of 35.0 Lambda Coins"],
   "errors": []
}
```

## Transmogrify

You can spend your Lambda Coins to transform items into powerful equipment at the transmogrifier using the following command:

`
curl -X POST -H 'Authorization: Token 7a375b52bdc410eebbc878ed3e58b2e94a8cb607' -H "Content-Type: application/json" -d '{"name":"[NAME OF ITEM]"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/transmogrify/
`

