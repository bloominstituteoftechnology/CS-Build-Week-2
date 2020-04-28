/*

https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

*/


'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the sockMerchant function below.
function sockMerchant(n, ar) {
    let sockPairs = 0;

    // In sockCounts, the key will be the unique sock number
    // and the value will be the number of those socks
    let sockCounts = {}; 

    let sock;
    

    for (sock of ar) {
        if (sockCounts.hasOwnProperty(sock)) {
            let count = sockCounts[sock];
            count++;
            sockCounts[sock] = count;
            if (count % 2 === 0) {
                sockPairs++;
            }
        }
        else {
            sockCounts[sock] = 1;
        }
    }
    
    return sockPairs;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = sockMerchant(n, ar);

    ws.write(result + "\n");

    ws.end();
}
