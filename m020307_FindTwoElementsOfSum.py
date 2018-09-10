# Given n integers and an integer x, determine whether there are two elements in
#   the n integers, the sum of which equals x, in Theta(nlgn) time.

from m020302_MergeSort import AscendingMergeSort
from m020305_BinarySearch import BinarySearch

def FindTwoElementsOfSum(nums, x):
    # First sort the numbers using merge sort, which is in Theta(nlgn) time.
    AscendingMergeSort(nums)
    # Then find the two elment in a loop using binary search, so it is still in Thtea(nlgn) time.
    i = 0
    while i < len(nums):
        j = BinarySearch(nums[i + 1:], x - nums[i])
        if j != None:
            return (nums[i], nums[i + 1 + j])
        else:
            i += 1
    return None


if __name__ == "__main__":
    testData1 = [5, 2, 10, 32, 4, 21, 3232, 43, 23, 34, 3, 2]
    # Should found
    x = testData1[0] + testData1[-1]
    print("To find x: {} in nums: {}.".format(x, testData1))
    a = FindTwoElementsOfSum(testData1, x)
    if a != None:
        print("The first element: {}, the second element: {}.".format(*a))
    else:
        print("Error.")
    # Should not found
    x = 0
    print("To find x: {} in nums: {}.".format(x, testData1))
    a = FindTwoElementsOfSum(testData1, x)
    if a != None:
        print("Error.")
    else:
        print("No such elements in these numbers.")

