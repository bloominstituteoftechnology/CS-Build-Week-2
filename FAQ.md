# CS Build Week 2 FAQ

## Contents

* [What happens if we use the wrong next room ID for the wise explorer bonus?](#q200)
* [You're seeing this error because you have `DEBUG = True` in your Django settings file](#q100)
* [If we get `cooldown X` in our response, does that mean we have to wait X seconds before the next request?](#q300)
* [Does the treasure disappear after someone picks it up?](#q400)
* [I'm getting CORS errors hitting the server with axios](#q500)
* [I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`](#q600)
* [Where is Pirate Ry?](#q700)
* [Where do we mine the coins?](#q800)
* [Can I get to a specific room without needing to traverse?](#q900)
* [Do I need to download some kind of hashing package to mine coins?](#q1000)
* [`pg_config` command not found](#q1100)
* [What's the title of the blockchain miner room?](#q1200)
* [How many rooms are there?](#q1300)
* [Are we expected to have a backend? Are we expected to store any information in a database?](#q1400)
* [There is mention of a "weight" of items, but the weights aren't a part of the data. How do we know what the weight is that we are about to accept before we try to pick up an item?](#q1500)
* [It seems that requests such as moving, picking up items, selling, etc are governed by the cooldown period. Is a status check on our individual user counted in that?](#q1600)
* [If we pair program and another teammate types it up and pushes it, will that affect our scores for this sprint?](#q1700)
* [What responses can we expect to receive after sumbitting a `mine` request?](#q1800)


<!--

-->

## Answers

<a name="q100"></a>
### You're seeing this error because you have `DEBUG = True` in your Django settings file

That's not really the error. Look up at the top of the output for the actual error.

---------------------------------------------------------------------------------------

<a name="q200"></a>
### What happens if we use the wrong next room ID for the wise explorer bonus?

Try it and see!

---------------------------------------------------------------------------------------

<a name="q300"></a>
### If we get `cooldown X` in our response, does that mean we have to wait X seconds before the next request?

Yes.

---------------------------------------------------------------------------------------

<a name="q400"></a>
### Does the treasure disappear after someone picks it up?

Yes. Once they sell the treasure, it will respawn in a random room somewhere
else on the map, so the treasures should never run out.

---------------------------------------------------------------------------------------

<a name="q500"></a>
### I'm getting CORS errors hitting the server with axios

CORS is set up on the server to allow access from anywhere.

Make sure the authorization is set up correctly in the axios call, e.g.:

```js
post("URL", foo, {
   headers: { Authorization: "Token " + token }
})
```

---------------------------------------------------------------------------------------

<a name="q600"></a>
### I'm getting a huge error/something about `ssl` when installing `psycopg2` with `pipenv install`

_**Mac only!** These instructions won't work for Windows!_

Buried at the bottom of this error message is something that looks like this:

```
build/temp.macosx-10.14-x86_64-3.7/psycopg/microprotocols_proto.o
build/temp.macosx-10.14-x86_64-3.7/psycopg/typecast.o -L/usr/local/lib -lpq -lssl -lcrypto -o
build/lib.macosx-10.14-x86_64-3.7/psycopg2/_psycopg.cpython-37m-darwin.so',
'    ld: library not found for -lssl',
'    clang: error: linker command failed with exit code 1 (use -v to see invocation)',
"    error: command 'clang' failed with exit status 1", '    ----------------------------------------'
```

If you don't have brew installed, [install it](https://brew.sh/).

Then:

```sh
brew install openssl
sudo cp $(brew --prefix openssl)/lib/libssl.1.0.0.dylib /usr/local/lib
sudo cp $(brew --prefix openssl)/lib/libcrypto.1.0.0.dylib /usr/local/lib
sudo ln -s /usr/local/lib/libssl.1.0.0.dylib /usr/local/lib/libssl.dylib
sudo ln -s /usr/local/lib/libcrypto.1.0.0.dylib /usr/local/lib/libcrypto.dylib
```

then try `pipenv install` again.

---------------------------------------------------------------------------------------

<a name="q700"></a>
### Where is Pirate Ry?

In the room that has `Pirate Ry` in its title.

---------------------------------------------------------------------------------------

<a name="q800"></a>
### Where do we mine the coins?

You may find the path to wealth in the waters of the wishing well.

---------------------------------------------------------------------------------------

<a name="q900"></a>
### Can I get to a specific room without needing to traverse?

Barring any aquired special powers, no.

---------------------------------------------------------------------------------------

<a name="q1000"></a>
### Do I need to download some kind of hashing package to mine coins?

Python: No. Just use the built-in [`sha256` in
`hashlib`](https://docs.python.org/3/library/hashlib.html).

JavaScript: Yes-ish. Recommendations:
* [`js-sha256`](https://www.npmjs.com/package/js-sha256)
* [`sha.js`](https://github.com/crypto-browserify/sha.js/)
* [node has crypto built-in](https://nodejs.org/api/crypto.html#crypto_crypto)

Swift: No. Use the built-in [SHA256](https://developer.apple.com/documentation/cryptokit/sha256).

---------------------------------------------------------------------------------------

<a name="q1100"></a>
### `pg_config` command not found

If you get this when running `pipenv install`, first do this:

```sh
export PATH="/Applications/Postgres.app/Contents/Versions/10/bin:$PATH"
```

then run `pipenv install` again. This should fix it going forward.

---------------------------------------------------------------------------------------

<a name="q1200"></a>
### What's the title of the blockchain miner room?

Nothing special--it's just a generic name. See [Where do we mine the
coins?](#q800)

---------------------------------------------------------------------------------------

<a name="q1300"></a>
### How many rooms are there?

There are 500 rooms/nodes/vertexes.

---------------------------------------------------------------------------------------

<a name="q1400"></a>
### Are we expected to have a backend? Are we expected to store any information in a database?

You will want to store the graph somewhere after you have everything mapped out. And not just rooms #s & what room you'll get to moving `n`, `s`, `e`, `w`, but also name & other attributes.

After you have the graph mapped out, you'll want to smartly wander around, collecting treasure. Your player can only carry so much treasure, because they are human, so periodically  you'll have to sell it. Once enough treasure has been collected, you can exchange it for the True Name you'll need to mine Lambda Coins.

Any information you can't directly request from the server (ex. complete map of the island), you'll want your application to keep track of. How you do that is up to you.

---------------------------------------------------------------------------------------

<a name="q1500"></a>
### There is mention of a "weight" of items, but the weights aren't a part of the data. How do we know what the weight is that we are about to accept before we try to pick up an item?

Check out the `examine` request.

---------------------------------------------------------------------------------------

<a name="q1600"></a>
### It seems that requests such as moving, picking up items, selling, etc are governed by the cooldown period. Is a status check on our individual user counted in that?

No. There is a `MIN_COOLDOWN` of 1.0, so if you run the `status` command, you should see something between 1-`cooldown`, depending on how long since you last moved.

---------------------------------------------------------------------------------------

<a name="q1700"></a>
### If we pair program and another teammate types it up and pushes it, will that affect our scores for this sprint?

Not necessarily. You can get a 2 in each technical row on the rubric as long as you can provide a clear, thorough explanation of what different pieces of the application are doing. So understanding the code is "enough".

_BUT_ if you're shooting for 3's in any or all rows, make sure you can "demonstrate and explain code that you contributed for this part of the task".

---------------------------------------------------------------------------------------

<a name="q1800"></a>
### What responses can we expect to receive after sumbitting a `mine` request?

You will get back specific messages that let you know if you succeeded in mining a Lambda coin or not. In the event your request was not successful, you should receive a message about why (invalid proof, True Name not yet acquired, etc.)
