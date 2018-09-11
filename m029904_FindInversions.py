from m000000_Test import PrintPerformance

@PrintPerformance
def FindInversionInN2(nums):
    numOfInversion = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                numOfInversion += 1
    return numOfInversion

@PrintPerformance
def FindInversionInNLogN(nums, b = -1, e = -1):
    def Merge(L, R):
        # Assume both L and R are in ascending order.
        # Return number of inversion between L and R, and merged array of L and R (in ascending order).
        nSum = 0
        j = 0
        M = []  
        for l in L:
            while j < len(R) and l > R[j]:
                M.append(R[j])
                j += 1
            # All elements in R[0:j] is smaller than l
            nSum += j
            M.append(l)
        # Don't forget the rest of R
        M.extend(R[j:])
        return (nSum, M)

    def FindInversionRecurisve(nums, b, e):
        if b == e:
            return (0, [])
        if b + 1 == e:
            return (0, [nums[b], ])
        else:
            # Divide
            m = int((b + e) / 2)
            # Conquer
            n1, L = FindInversionRecurisve(nums, b, m)
            n2, R = FindInversionRecurisve(nums, m, e)
            # Combine
            n3, LR = Merge(L, R)

            return (n1 + n2 + n3, LR)

    if b == -1 or e == -1:
        b = 0
        e = len(nums)

    n, L = FindInversionRecurisve(nums, b, e)
    return n


if __name__ == "__main__":
    import m000000_Test as Test

    # Case have answer
    nums = [2, 3, 8, 6, 1]
    print("Find number of inversions in {}".format(nums))
    n = FindInversionInN2(nums)
    print("FindInversionInN2: {} inversions.".format(n))
    n = FindInversionInNLogN(nums)
    print("FindInversionInNLogN: {} inversions.".format(n))

    # Test cases
    numSizes = [100, 1000, 10000, 100000]
    for num in numSizes:
        nums = Test.GetRandomIntegers(num)
        print("Find number of inversions in list of {} elements".format(num))
        n = FindInversionInN2(nums)
        print("FindInversionInN2: {} inversions.".format(n))
        n = FindInversionInNLogN(nums)
        print("FindInversionInNLogN: {} inversions.".format(n))

