from m000000_Test import PrintPerformance

@PrintPerformance
def BruteForceMaximumSubarray(nums):
    if len(nums) < 1:
        return (-1, -1, 0)
    if len(nums) == 1:
        return (0, 1, nums[0])
    # Setup an scan array for fast subarray summing.
    scan = [0]
    sum = 0
    for n in nums:
        sum += n
        scan.append(sum)
    # Brute force finding.
    mi, mj = 0, 0
    maxSum = scan[mj + 1] - scan[mi]
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums) + 1):
            subarraySum = scan[j] - scan[i]
            if subarraySum > maxSum:
                maxSum = subarraySum
                mi, mj = i, j 
    return (mi, mj, maxSum)



if __name__ == "__main__":
    testNums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    i, j, sum = BruteForceMaximumSubarray(testNums)
    print("Max sub-array sum: [{}, {}): {}".format(i, j, sum))
    


    

    