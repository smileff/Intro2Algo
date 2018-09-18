from m000000_Test import PrintPerformance, GetRandomIntegers

def BruteForceFindMaximumSubarray(nums, b, e):

    if e - b < 1:
        return (-1, -1, 0)
    if e - b == 1:
        return (0, 1, nums[b])
    # Setup an scan array for fast subarray summing.
    scan = [0]
    sum = 0
    for n in range(b, e):
        sum += nums[n]
        scan.append(sum)
    # Brute force finding.
    mi, mj = 0, 0
    maxSum = scan[mj + 1] - scan[mi]
    for i in range(0, e - b):
        for j in range(i + 1, e - b + 1):
            subarraySum = scan[j] - scan[i]
            if subarraySum > maxSum:
                maxSum = subarraySum
                mi, mj = i, j 
    return (b + mi, b + mj, maxSum)


@PrintPerformance
def BruteForceMaximumSubarray(nums):
    return BruteForceFindMaximumSubarray(nums, 0, len(nums))


# Find max crossing subarray
def FindMaxCrossingSubarray(nums, b, m, e):
    left, leftSum, leftMaxSum = m - 1, nums[m - 1], nums[m - 1]
    for i in range(m - 2, b - 1, -1):
        leftSum += nums[i]
        if leftSum > leftMaxSum:
            left, leftMaxSum = i, leftSum
    right, rightSum, rightMaxSum = m, nums[m], nums[m]
    for j in range(m + 1, e):
        rightSum += nums[j]
        if rightSum > rightMaxSum:
            right, rightMaxSum = j, rightSum
    return (left, right + 1, leftMaxSum + rightMaxSum)


@PrintPerformance
def RecursiveMaximumSubarray(nums):
        
    def RecursiveFunc(nums, b, e):
        if b == e:
            return (-1, -1, 0)
        elif b + 1 == e:
            return (b, e, nums[b])
        else:
            # Subdivide
            m = int((b + e) / 2)
            # Conquer
            s1 = RecursiveFunc(nums, b, m)
            s2 = RecursiveFunc(nums, m, e)
            # Combine
            s3 = FindMaxCrossingSubarray(nums, b, m, e)
            if s3[2] >= s1[2] and s3[2] >= s2[2]:
                return s3
            elif s1[2] >= s2[2] and s1[2] >= s3[2]:
                return s1
            else:
                return s2
            
    return RecursiveFunc(nums, 0, len(nums))


@PrintPerformance
def CombineMaximumSubarray(nums, n0 = 50):

    def RecursiveFunc(nums, b, e, n0):
        if e - b <= n0:
            return BruteForceFindMaximumSubarray(nums, b, e)
        else:
            # Subdivide
            m = int((b + e) / 2)
            # Conquer
            s1 = RecursiveFunc(nums, b, m, n0)
            s2 = RecursiveFunc(nums, m, e, n0)
            # Combine
            s3 = FindMaxCrossingSubarray(nums, b, m, e)
            if s3[2] >= s1[2] and s3[2] >= s2[2]:
                return s3
            elif s1[2] >= s2[2] and s1[2] >= s3[2]:
                return s1
            else:
                return s2
            
    return RecursiveFunc(nums, 0, len(nums), n0)


if __name__ == "__main__":
    testNums = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print("Find maximum subarray in {}".format(testNums))
    i, j, sum = BruteForceMaximumSubarray(testNums)
    print("Use the brute force method, max sub-array sum: [{}, {}): {}".format(i, j, sum))
    i, j, sum = RecursiveMaximumSubarray(testNums)
    print("Use the recursive method, max sub-array sum: [{}, {}): {}".format(i, j, sum))
    i, j, sum = CombineMaximumSubarray(testNums)
    print("Use the combine method, max sub-array sum: [{}, {}): {}".format(i, j, sum))
    print("")

    numSizes = [100, 1000, 10000, 100000]
    for numSize in numSizes:
        nums = GetRandomIntegers(numSize, -100, 100)
        print("Find maximum subarray in {} numbers".format(numSize))
        # The brute force method
        if numSize <= 10000:
            i, j, sum = BruteForceMaximumSubarray(nums)
            print("Use the brute force method, max sub-array sum: [{}, {}): {}".format(i, j, sum))
        # Recursive method
        i, j, sum = RecursiveMaximumSubarray(nums)
        print("Use the recursive method, max sub-array sum: [{}, {}): {}".format(i, j, sum))
        # Combine method
        for n0 in (10, 50, 100, 200):
            i, j, sum = CombineMaximumSubarray(nums, n0)
            print("Use the recursive method with n0: {}, max sub-array sum: [{}, {}): {}".format(n0, i, j, sum))

        print("")
    


    

    