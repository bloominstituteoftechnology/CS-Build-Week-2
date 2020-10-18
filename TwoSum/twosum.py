# https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums, target):
        # Create working variables
        wrk_dict = {}

        # Iterate through the list of integers
        for idx, val in enumerate(nums):
            # Insert value into the working dict

            # Is the current value already in our dict?
            if val not in wrk_dict:
                # no: insert the value associate with a list
                #     containing the value's index in the list
                wrk_dict[val] = [idx]
                continue

            # Current value already exists, append this index
            wrk_dict[val].append(idx)

        # Iterate through the dictionary's keys
        for ky in wrk_dict.keys():
            # Calculate the difference between the target and current key
            diff = target - ky

            # Is the difference equal to the key (e.g. ky + ky = target)?
            if diff == ky:
                # yes: must have dupes, return multiple indices associated with 
                #      this list value
                if len(wrk_dict[ky]) == 1:
                    # the difference is equal to the key but only value found... keep processing
                    continue

                # return first two index values
                return wrk_dict[ky][0:2]

            # Is the diff in the dict?
            if diff in wrk_dict:
                # yes: return a list that includes the indices of the
                #      two keys
                ret_lst = [wrk_dict[ky][0]]
                ret_lst.append(wrk_dict[diff][0])
                return ret_lst

        # Finished iterating: no solution found
        return []


my_solv = Solution()

rslt = my_solv.twoSum([3,2,4], 6)
print(rslt)

              