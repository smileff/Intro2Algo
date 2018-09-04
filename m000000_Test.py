import random, time

def GetRandomIntegers(num = 100, minValue = 0, maxValue = 100):
    return [random.randint(minValue, maxValue) for i in range(num)]


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
        