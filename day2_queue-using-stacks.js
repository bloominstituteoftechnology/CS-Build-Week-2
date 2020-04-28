/*

https://leetcode.com/problems/implement-queue-using-stacks/

*/


/**
 * Initialize your data structure here.
 */
var MyQueue = function() {
    //stackForward, is the stack where the item with index=0 is the 
    //first item in the queue and item with index=(length_of_stackForward-1)
    //is the last item in the queue
    this.stackForward = [];  
    
    //stackReverse, is the stack where the item with index=0 is the 
    //last item in the queue and item with index=(length_of_stackReverse-1)
    //is the first item in the queue
    this.stackReverse = [];
    
    //Only one stack must hold the data of the queue at begining or end
    //of push/pop/peek/empty function execution
    
    //During the execution of these functions, there may be transition of
    //data betweeen the stacks
    
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    if (this.stackForward.length === 0) {
        this.R2F();
    }
    this.stackForward.push(x);
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    if (this.stackReverse.length === 0) {
        this.F2R();
    }
    return this.stackReverse.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if (this.stackReverse.length === 0) {
        this.F2R();
    }
    return this.stackReverse[this.stackReverse.length-1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if ( (this.stackReverse.length !== 0) || (this.stackForward.length !== 0) ) {
        return false;
    }
    return true;
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */


// Moves the queue data from the forward stack to the 
// reverse stack
MyQueue.prototype.F2R = function() {
    while (this.stackForward.length > 0) {
        let data = this.stackForward.pop();
        this.stackReverse.push(data);
    }
}

// Moves the queue data from the reverse stack to the 
// forward stack
MyQueue.prototype.R2F = function() {
    while (this.stackReverse.length > 0) {
        let data = this.stackReverse.pop();
        this.stackForward.push(data);
    }
}

// Test code block 1
// let myObjA = new MyQueue();
// myObjA.stackForward = [1,2,3];
// console.log("Before myObjA: ",myObjA);
// myObjA.F2R();
// console.log("After myObjA: ",myObjA);


// Test code block 2
// let myObjB = new MyQueue();
// myObjB.stackReverse = [4,5,6];
// console.log("Before myObjB: ",myObjB);
// myObjB.R2F();
// console.log("After myObjB: ",myObjB);

// Test code block 3
// let myObj3 = new MyQueue();
// myObj3.stackReverse = [4,5,6];
// console.log("Before myObj3: ",myObj3);
// myObj3.push(99);
// console.log("After myObj3: ",myObj3);
