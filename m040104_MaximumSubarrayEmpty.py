from m000000_Test import ReturnPerformance, GetRandomIntegers

def BruteForceFindMaximumSubarray(nums, b, e):
    ''' '''
    if e - b <= 0:
        return (-1, -1, 0)
    # Setup an scan array for fast subarray summing.
    scan = [0]
    sum = 0
    for i in range(b, e):
        sum += nums[i]
        scan.append(sum)
    # Brute force finding.
    mi, mj = -1 - b, -1 - b
    maxSum = 0
    for i in range(0, e - b):
        for j in range(i + 1, e - b + 1):
            subarraySum = scan[j] - scan[i]
            if subarraySum > maxSum:
                maxSum = subarraySum
                mi, mj = i, j 
    return (b + mi, b + mj, maxSum)


@ReturnPerformance
def BruteForceMaximumSubarray(nums):
    return BruteForceFindMaximumSubarray(nums, 0, len(nums))


# Find max crossing subarray
def FindMaxCrossingSubarray(nums, b, m, e):
    left, leftSum, leftMaxSum = -1, 0, 0
    for i in range(m - 1, b - 1, -1):
        leftSum += nums[i]
        if leftSum > leftMaxSum:
            left, leftMaxSum = i, leftSum
    right, rightSum, rightMaxSum = -1, 0, 0
    for j in range(m, e):
        rightSum += nums[j]
        if rightSum > rightMaxSum:
            right, rightMaxSum = j, rightSum

    if left == -1 and right == -1:
        return (-1, -1, 0)
    elif left == -1 and right != -1:
        return (m, right + 1, rightMaxSum)
    elif right != -1 and right == -1:
        return (left, m, leftMaxSum)
    else:
        return (left, right + 1, leftMaxSum + rightMaxSum)


@ReturnPerformance
def RecursiveMaximumSubarray(nums):
        
    def RecursiveFunc(nums, b, e):
        if b == e:
            return (-1, -1, 0)
        if b + 1 == e:
            if nums[b] >= 0:
                return (b, e, nums[b])
            else:
                return (-1, -1, 0)
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


@ReturnPerformance
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
    (i, j, sum), t = BruteForceMaximumSubarray(testNums)
    print("Use the brute force method, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(i, j, sum, t))
    (i, j, sum), t = RecursiveMaximumSubarray(testNums)
    print("Use the recursive method, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(i, j, sum, t))
    (i, j, sum), t = CombineMaximumSubarray(testNums)
    print("Use the combine method, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(i, j, sum, t))
    print("")

    numSizes = [100, 1000, 10000, 100000]
    for numSize in numSizes:
        nums = GetRandomIntegers(numSize, -100, 0)
        print("Find maximum subarray in {} numbers".format(numSize))
        # The brute force method
        if numSize <= 10000:
            (i, j, sum), t = BruteForceMaximumSubarray(nums)
            print("Use the brute force method, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(i, j, sum, t))
        # Recursive method
        (i, j, sum), t = RecursiveMaximumSubarray(nums)
        print("Use the recursive method, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(i, j, sum, t))
        # Combine method
        for n0 in (10, 50):
            (i, j, sum), t = CombineMaximumSubarray(nums, n0)
            print("Use the recursive method with n0: {}, max sub-array sum: [{}, {}): {}, time: {:6.3}".format(n0, i, j, sum, t))

        print("")
    


    

    