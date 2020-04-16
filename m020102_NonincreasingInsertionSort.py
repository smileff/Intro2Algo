def NonincreasingInsertionSort(nums):
    for j in range(1, len(nums)):
        # Loop invariant: nums[0:j] is descending sorted.
        tmp = nums[j]
        i = j - 1
        while i >= 0 and nums[i] < tmp:
            nums[i + 1] = nums[i]
            i = i - 1
        # So nums[i] is the first elem >= tmp, or i == -1
        nums[i + 1] = tmp
    return nums

if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestDescendingSort(NonincreasingInsertionSort)