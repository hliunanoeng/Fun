class Solution(object):
    def threeSumClosest(self, nums, target):
        record = 99999
        res = 0
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                dist = threeSum - target
                if dist > 0:
                    r -= 1
                else:
                    l += 1

                if abs(dist) < record:
                    record = abs(dist)
                    res = threeSum

        return res

