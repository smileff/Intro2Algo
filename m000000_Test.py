import random, time

# Run function and statistic performance.
def PrintPerformance(func):
    def RunFunctionAndPrintPerformance(*args, **kw):
        startTime = time.time()
        retValue = func(*args, **kw)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print("Run {} in {:6.3} seconds.".format(func, elapsedTime))
        return retValue
    return RunFunctionAndPrintPerformance

def ReturnPerformance(func):
    def RunFunctionAndReturnPerformance(*args, **kw):
        startTime = time.time()
        retValue = func(*args, **kw)
        endTime = time.time()
        elapsedTime = endTime - startTime
        return (retValue, elapsedTime)
    return RunFunctionAndReturnPerformance

# Generate test data

def GetRandomIntegers(num = 100, minValue = 0, maxValue = 100):
    return [random.randint(minValue, maxValue) for i in range(num)]


# 

def CheckNumbersInAscendingOrder(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


def CheckNumbersInDescendingOrder(nums):
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            return False
    return True


def TestSort(sortFunc, checkFunc):
    numSizes = [10, 100, 1000, 10000, 100000]
    minValue, maxValue = -10000, 10000
    print("Start check sorting algorithm {}".format(sortFunc))
    error = False
    for numSize in numSizes:
        nums = GetRandomIntegers(numSize, minValue, maxValue)
        # Sorting
        startTime = time.time()
        sortFunc(nums)
        endTime = time.time()
        elapsedTime = endTime - startTime

        if checkFunc(nums):
            print("Sorted {} numbers in {:6.3} seconds.".format(numSize, elapsedTime))
        else:
            print("Sorted {} numbers: ERROR.".format(numSize))
            error = True
            break
    if not error:
        print("All test cases passed.")
    else:
        print("Algorithm has errors!")


def TestAscendingSort(sortFunc):
    return TestSort(sortFunc, CheckNumbersInAscendingOrder)


def TestDescendingSort(sortFunc):
    return TestSort(sortFunc, CheckNumbersInDescendingOrder)
        

def TestSearchInAscendingSortedNums(searchFunc):
    numSizes = [10, 100, 1000, 10000, 100000]
    minValue, maxValue = -10000, 10000
    error = False
    for numSize in numSizes:
        # Test case 1, should found
        nums1 = GetRandomIntegers(numSize, minValue, maxValue)
        key1 = random.randint(minValue, maxValue)
        if not key1 in nums1:
            nums1.append(key1)
        nums1 = sorted(nums1)
        # Search
        startTime1 = time.time()
        idx = searchFunc(nums1, key1)
        endTime1 = time.time()
        elapsedTime1 = endTime1 - startTime1
        if idx == None or idx < 0 or idx >= len(nums1) or nums1[idx] != key1:
            print("Search in {:10} sorted numbers, case in array: ERROR.".format(numSize))
            error = True
            break
        # Test case 2, should not found
        nums2 = GetRandomIntegers(numSize, minValue, maxValue)
        key2 = random.randint(minValue, maxValue)
        while key2 in nums2:
            nums2.remove(key2)
        nums2 = sorted(nums2)
        # Search
        startTime2 = time.time()
        idx = searchFunc(nums2, key2)
        endTime2 = time.time()
        elapsedTime2 = endTime2 - startTime2
        if idx != None:
            print("Search in {:10} sorted numbers, case not in array: ERROR.".format(numSize))
            error = True
            break
        print("Search in {:10} sorted numbers, case in array: {:6.3} seconds, "
            "case not in array: {:6.3} seconds".format(numSize, elapsedTime1, elapsedTime2))

    if not error:
        print("All test cases passed.")
    else:
        print("Algorithm has errors!")

        