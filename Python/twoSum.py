class Solution:
    def twoSum(self, nums: List[int], target: int):
        listOfNums = {}
        for i in range(0, len(nums), 1):
            answer = target - nums[i]
            if answer in listOfNums:
                return [listOfNums[answer], i]
            else:
                listOfNums[nums[i]] = i
