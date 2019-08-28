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
   headers: { Authorization: "Bearer " + token }
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

Once you've changed your name, reach out to your TL and they'll tell you the
next step. It'll be an interview, and once you've passed that, you'll get a hint
to where the mining room is.

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
