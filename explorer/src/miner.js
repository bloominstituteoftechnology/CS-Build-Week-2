// import Hashes from 'jshashes'
const Hashes = require('jshashes')
// import utf8 from 'utf8'
const utf8 = require('utf8')

function get_proof(last_proof, proof, difficulty) {

    proof=1000000000
    last_proof = 17606371404
    let str = `${last_proof}${proof}`
    let hash = new Hashes.SHA256().hex(str)

    while (hash.slice(0,6) !== '000000') {
        // console.log(proof, hash)
        proof++
        let str = `${last_proof}${proof}`
        str = utf8.encode(str)
        // console.log(`string is ${str}`)
        hash = new Hashes.SHA256().hex(str)
    }

    console.log(proof)
    return hash
    //   .update(`${last_proof}${proof}`)
    //   .digest('hex')
    // return hash.substring(0, difficulty) === '0'.repeat(difficulty)
  }

  get_proof()