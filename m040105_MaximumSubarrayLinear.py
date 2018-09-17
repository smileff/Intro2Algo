def MaximumSubarrayLinear(nums):
    if len(nums) == 0:
        return (-1, -1, 0)
    elif len(nums) == 1:
        return (0, 1, nums[0])
    else:
        # Loop variant
        # maxSum is current maximum sub-array sum in nums[0:j].
        # pi is the least index let sum(nums[pi:j]) > 0
        maxSum = nums[0]
        mi, mj = 0, 1
        if nums[0] > 0:
            pi, pSum = 0, nums[0]
        else:
            pi, pSum = 1, 0
        for j in range(1, len(nums)):
            pSum += nums[j]
            if pSum > maxSum:
                mi, mj, maxSum = pi, j + 1, pSum
            if pSum < 0:
                pi, pSum = j + 1, 0
        return mi, mj, maxSum

if __name__ == "__main__":
    testNums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    i, j, sum = MaximumSubarrayLinear(testNums)
    print("Max sub-array sum: [{}, {}): {}".format(i, j, sum))