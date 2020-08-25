class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        # # solution 1
        # count = set()
        # for num in nums:
        #     if num in count:
        #         return True
        #     else:
        #         count.add(num)
        # return False

        # solution 2
        # reduces runtime significantly because it runs one comparison
        # instead of running one comparison per loop
        # has the same space complexity
        count = set(nums)
        return len(count) != len(nums)

        # # solution 3
        # # needs a base case
        # takes way too long to execute but should return correct results
        # this solution is very naive and has an undesirable time complexity
        # of n^2, with the unweighted upsaide of having n space complexity
        # if len(nums) <= 1:
        #     return False
        # for i in range(len(nums)):
        #     for j in range(len(nums[i + 1:])):
        #         # print(i, j + i)
        #         if nums[i] == nums[i + j + 1]:
        #             return True
        # return False


test = Solution()

ex1 = [1, 2, 3, 1]
ex2 = [1, 2, 3, 4]

print(test.containsDuplicate(ex1))
print(test.containsDuplicate(ex2))
