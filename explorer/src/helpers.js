
export class Stack {
    constructor(){
        this.stack = []
    }

    push(value) {
        this.stack.push(value)
    }
    pop() {
        if (this.size() > 0) {
            return this.stack.pop()
        }
        else {
            return null
        }
    }
    size() {
        return this.stack.length
    }
}

export class Queue {
    constructor(){
        this.queue = []
    }

    enqueue(value) {
        this.queue.push(value)
    }
    dequeue() {
        if (this.size() > 0) {
            return this.queue.shift()
        }
        else {
            return null
        }
    }
    size() {
        return this.queue.length
    }
}

// export const makePath = (player, room = {}) => {

//     let graph = {}
//     let path = []

//     while (graph.length < 500) {
//         console.log(`graph is this long ${graph.length}`)

//         let notExplored = []

//         const exits = room.exits

//         const current = room.room_id

//         if (!(current in graph)) {
//             graph[current] = {}
//             for (var x in exits) {
//                 graph[current][exits[x]] = '?'
//             }
//         }
        
//         for (var room in graph[current]) {
//             console.log(room)
//             if (room == "?") {
//                 notExplored.push(direction)
//             } 
//           }

//         if (notExplored.length > 0) {
//             let nextMove = getRandomDirection(notExplored)

//             //make axios call with next move, set new room
//             //on state 

//             graph[current][nextMove] = room.id
//             path.push(nextMove)
//             notExplored = []
//         } else {
//             let q = new Queue()
//             q.enqueue([current])

//             let checked = []
//             let returnPath = []

//             while (q.size() > 0) {
//                 checkPath = q.dequeue()
//                 let v = checkPath[-1]


//                 if (!(v in returnPath)) {
//                     let exists = Object.keys(graph[v]).some(function(k) {
//                         return returnPath[k] === "?";
//                     });
//                     if (exists == true) {
//                         returnPath = checkPath
//                         break
//                     }
//                     returnPath.append(v)
//                     for (way in graph[v]) {
//                         let new_path = [...checkPath]
//                         new_path.push(graph[v][way])
//                         q.enqueue(new_path)
//                     }
//                 }
//             }

//             let steps = []

//             for (i = 0; i < returnPath.length - 1; i++) { 
//                 for (direction in graph[returnPath[i]]) {
//                     if (graph[returnPath[i]][direction] == returnPath[i + 1]) {
//                         steps.push(direction)
//                     }
//                 }
//                 path = path.concat(steps)
//                 for (step in steps) {
//                     //axios call to have player move
//                 }
//               }
            
//         }
//     }

//     return path
// }

export const getRandomDirection = (exits) => {
    const chosenExit = exits[getRandomInt(0, exits.length)]
    return chosenExit
}

export function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
  }
    
export const flipDirection = (dir) => {
    if (dir == 'n'){
        return 's'
    }
    else if (dir =='e'){
        return 'w'
    }
    else if (dir == 's'){
        return 'n'
    }
    else if (dir == 'w'){
        return 'e'
    }
}
// {
//     "room_id": 0,
//     "title": "A Dark Room",
//     "description": "You cannot see anything.",
//     "coordinates": "(60,60)",
//     "exits": ["n", "s", "e", "w"],
//     "cooldown": 1.0,
//     "errors": [],
//     "messages": []
//   }