def NonincreasingInsertionSort(nums):
    # print("Input numbers: ", nums)
    for j in range(1, len(nums)):
        tmp = nums[j]
        i = j
        while i > 0 and nums[i - 1] < tmp:
            nums[i] = nums[i - 1]
            i = i - 1
        nums[i] = tmp
        # print("After {} iteration: ".format(j - 1), nums)
    return nums

if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestDescendingSort(NonincreasingInsertionSort)