
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
    pop() {
        if (this.size() > 0) {
            return this.stack.shift()
        }
        else {
            return null
        }
    }
    size() {
        return this.stack.length
    }
}