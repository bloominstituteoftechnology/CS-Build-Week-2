# Build Week: Day 2

## [Roman Numerals](./romannumerals.py)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```table
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X + II`. The number twenty seven is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* `I` can be placed before `V (5)` and `X (10)` to make `4` and `9`.
* `X` can be placed before `L (50)` and `C (100)` to make `40` and `90`.
* `C` can be placed before `D (500)` and `M (1000)` to make `400` and `900`.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from `1` to `3999`.

Example Inputs:

``` python
1. "IX"
2. "III"
3. "XX"
4. "CXLIV"
5. "LVIII"
6. "MCMXCIV"
```

Expected Outputs:

``` python
1. 9
2. 3
3. 20
4. 144
5. 58
6. 1994
```

## [Balance Binary Tree](./balancedbinarytree.py)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

>a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example Inputs:

``` python
1. [3,9,20,None,None,15,7]

>>    3
>>   / \
>>  9  20
>>    /  \
>>   15   7

2. [1,2,2,3,3,None,None,4,4]

>>       1
>>      / \
>>     2   2
>>    / \
>>   3   3
>>  / \
>> 4   4

3. []
```

Expected Outputs:

``` python
1. True
2. False
3. True
```

## [Two Numbers](./twonumbers.py)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example Inputs:

```python
1. [2, 7, 11, 15], 9
2. [3,2,4], 6
3. [2, 3, 6, 7], 13
4. [1, 3, 8, 7, 9], 15
```

Expected Outputs:

```python
1. [0, 1]
2. [1, 2]
3. [2, 3]
4. [2, 4]
```
