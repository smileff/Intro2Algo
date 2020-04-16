# Helper functions for test sorting algorithm.

import random, time, sys


# Generate test data

def GetRandomIntegers(num = 100, minValue = 0, maxValue = 100):
    return [random.randint(minValue, maxValue) for i in range(num)]


# Check the result of sort algorithm

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


# Call these functions to test sorting algorithms.
# First generate 100/1000/10000/100000 numbers as the test data.
# Sort by calling the sortFunc.
# Then check the result with the checkFunc.
# Meanwhile profile this process.

def TestSort(sortFunc, checkFunc, maxTestListSize = 100000):    
    minValue, maxValue = -10000, 10000
    print("Start check sorting algorithm {}".format(sortFunc))

    numSize = 10
    while numSize <= maxTestListSize:
        sys.stdout.write("Sorting {:6} numbers ... ".format(numSize))

        # Generate test numbers
        nums = GetRandomIntegers(numSize, minValue, maxValue)

        # Sorting
        startTime = time.time()
        sortFunc(nums)
        endTime = time.time()
        elapsedTime = endTime - startTime

        # Print results
        if checkFunc(nums):
            print("in {:6.3} seconds.".format(elapsedTime))
        else:
            print("ERROR.")
            return
    
        # Next test.
        numSize *= 10

    # Passed all tests.
    print("All test cases passed.")


def TestAscendingSort(sortFunc, maxTestListSize = 100000):
    return TestSort(sortFunc, CheckNumbersInAscendingOrder, maxTestListSize)


def TestDescendingSort(sortFunc, maxTestListSize = 100000):
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
