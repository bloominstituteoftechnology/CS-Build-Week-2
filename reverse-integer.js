var reverse = function(x) {
    
    let negative = x < 0; // keep track if variable is negative
    let reverse = 0; // instantiate 0
    
    if (negative) { 
        x *= -1;    // make x positive
    }
    
    while (x > 0) {
        reverse = (reverse * 10) + (x % 10)
        x = Math.floor(x / 10); // remove last digit of x
    }
    if (reverse > (2 ** 31 - 1)) {
        return 0;
    }
    return negative ? (reverse * -1) : reverse;
};