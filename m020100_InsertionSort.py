# Non-increasing insert short.

def InsertionSort(nums):
    # print("Input numbers: ", nums)
    for j in range(1, len(nums)):
        # Loop invariant: nums[0:j] is sorted.
        value = nums[j]
        i = j
        while i > 0 and nums[i - 1] > value:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = value
        # print("After {}-th iteration: ".format(j), nums)
    return nums

if __name__ == "__main__":
    from Test import TestSort
    TestSort.TestAscendingSort(InsertionSort, )


