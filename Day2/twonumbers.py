class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        brute-force: nested for loops
            solution timed out, reduce loops by cutting out unecessary j values
            indexing becomes difficult, and i'm getting wrong solutions -> moving to pen and paper to solve

        room for improvement:
            if I implement a cache, I can reduce speed by removing the inner loop
            this would increase memory consumption potentially significantly though
        """
        # brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]

        # brute force, reduce redundant calculations
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # hash table implementation
        # this implementation unsurprisingly saw a SIGNIFICANT speedup
        cache = {}
        for i in range(len(nums)):
            # check cache if we've seen the value yet
            if nums[i] not in cache:
                cache[nums[i]] = []
            # add the current index to the cache
            cache[nums[i]].append(i)
            # check if the cache has an index for target val - current val
            if target - nums[i] in cache and cache[target-nums[i]][0] != i:
                return [cache[target-nums[i]][0], i]
        """
        whereas the naive implementations had a time complexity of O(n^2), this
        implementation reduces the time complexity down to O(n). The space
        complexity has not increased by any noteworthy amount.
        """


test = Solution()

ex1 = [[2, 7, 11, 15], 9]
ex2 = [[3, 2, 4], 6]
ex3 = [[2, 3, 6, 7], 13]
ex4 = [[1, 3, 6, 7, 9], 15]

print(test.twoSum(*ex1))
print(test.twoSum(*ex2))
print(test.twoSum(*ex3))
print(test.twoSum(*ex4))
