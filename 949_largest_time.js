var largestTimeFromDigits = function(A) {
    
    const getPermutations = (arr, perms=[], len=arr.length) => {
        if(len === 1) perms.push(arr.slice(0))
        
        for(let i = 0; i < len; i++){
            getPermutations(arr, perms, len-1)
        
        
        if(len % 2){
            [arr[0], arr[len-1]] = [arr[len-1], arr[0]]
        } else {
            [arr[i], arr[len - 1]] = [arr[len-1], arr[i]]
         }
        }
        return perms
    }              
    const permus = getPermutations(A)
    
    let maxTime = [-1, -1]
    
    permus.forEach(a => {
        let hour = String(a[0]) + String(a[1])
        let minute = String(a[2]) + String(a[3])
        
        if(hour > maxTime[0] && hour < 24 && minute < 60){
            maxTime = [hour, minute]
        } else if(hour === maxTime[0] && minute > maxTime[1] && minute < 60){
            maxTime = [maxTime[0], minute]
        }
        
    })
    
    return maxTime.includes(-1) ? '' : `${maxTime[0]}:${maxTime[1]}`
    
};

/* 
Reflect:
had to look up how to find permutations; take some time to learn this, it will probably be valuable

*/