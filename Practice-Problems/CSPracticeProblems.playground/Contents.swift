// LeetCode Practice Problems: Algorithms

//---------------------------------------------------------------------------------------------

// MARK: - Binary Search Problems
// Key Words: sorted, range
// Notes:
//   - Binary search should be muscle memory
//   - Can be implemented iteratively or recursively

//---------------------------------------------------------------------------------------------

// Sqrt(x)
// Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
// Since the return type is an integer, the decimal digits are truncated and only the integer
// part of the result is returned.

func squareRoot(_ x: Int) -> Int {
    var min = 0
    var max = x
    var res = 0
    
    while min <= max {
        let mid = Int((min + max) / 2)
        let squared = mid * mid
        if squared == x {
            return mid
        } else if squared > x {
            max = mid - 1
        } else {
            min = mid + 1
            res = mid
        }
    }
    
    return res
}

print(squareRoot(16))   // 4
print(squareRoot(9))    // 3
print(squareRoot(8))    // 2
print(squareRoot(1))    // 1
print(squareRoot(0))    // 0

//---------------------------------------------------------------------------------------------
