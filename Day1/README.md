# LeetCode Challenges: Day 1

## [Valid Palindrome](./validpalindrome.py)

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

>Note: For the purpose of this problem, we define empty string as valid palindrome.

Example Inputs:

``` python
1. "A man, a plan, a canal, Panama!"
2. "Abba"
3. "This one isn't"
```

Expected Outputs:

``` python
1. True
2. True
3. False
```

## [Contains Duplicates](./containsduplicate.py)

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example Inputs:

``` python
1. [1, 2, 3, 1]
2. [1, 2, 3, 4]
```

Expected Outputs:

``` python
1. True
2. False
```

## [Add Two Numbers](./addtwonumbers.py)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example Inputs:

``` python
1. 2 -> 4 -> 3
   5 -> 6 -> 4
2. 1 -> 2 -> 3
   3 -> 4 -> 5
```

Expected Outputs:

``` python
1. [7, 0, 8]
2. [4, 6, 8]
```

## [Minimum Swaps to Make Strings Equal](./minimumswaps.py)

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example Input:

``` python
1. "xx", "yy"
2. "xy", "yy"
3. "xy", "yx"
4. "xxyyxyxyxx", "xyyxyxxxyx"
```

Expected Output:

``` python
1. 1
2. -1
3. 2
4. 4
```

## [Longest Common Prefix](./longestcommonprefix.py)

Write a function to find the longest common prefix string amongst an array of strings.

>If there is no common prefix, return an empty string "".

Example Inputs:

``` python
1. ["flower", "flow", "flight"]
2. ["dog", "racecar", "car"]
```

Expected Output:

``` python
1. prefix: "fl"
1. prefix: ""
```
