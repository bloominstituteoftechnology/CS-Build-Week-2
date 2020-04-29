/*

https://leetcode.com/problems/decode-string/

*/


/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let output = '';
    
    //This is the stack for processing. Each data item of the stack is a 2 element array
    //The 1st element is the integer number of times to repeat
    //The 2nd element is the string to be repeated
    //So for example a stack data can be [3,'qaz'], which is 'qazqazqaz'
    let stack = [];
    
    
    let sLen = s.length;
    let i = 0;
    
    while (i < sLen) {
        let num = Number(s.charAt(i));
        
        //If the character is a number
        if ((1 <= num) && (num <= 9)) {
            let numString = "" + s.charAt(i);
            i++;
            while (s.charAt(i) !== '[') {
                numString = numString + s.charAt(i);
                i++;    
            } 
            stack.push([Number(numString),'']);
            
            //current character must be a "[" so skip past it
            i++;
        }
        else if (s.charAt(i) === ']') {
            //Convert topmost stack data to a string
            let stackData = stack.pop();
            let convString = ''; //This points to the stackData converted to a string 
            for(let repeat=0; repeat<stackData[0]; repeat++) {
                convString = convString + stackData[1];
            }
            if (stack.length>0) {
                //If stack is not empty add the newly converted string to the string of 
                //the data element at the top of the stack
                let topStackData = stack.pop();
                topStackData[1] = topStackData[1] + convString;
                stack.push(topStackData);
            }
            else {
                //If stack is empty, then push converted string to output
                output = output + convString;
            }
            i++;
        }
        else {
            //Here we handle letter characters. 
            
            if (stack.length>0) {
                //Append them to the string part of the topmost 
                //data piece in the stack
                let stackData = stack.pop();
                stackData[1] = stackData[1] + s.charAt(i);
                stack.push(stackData);
                i++;
            } 
            else {
                //If stack is empty, then push character to output
                output = output + s.charAt(i);
                i++;
            }
        }
        
        
        
        
    }
    
    return output;
    // console.log(stack)
    
    
    
};
