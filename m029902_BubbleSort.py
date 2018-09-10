def AscendingBubbleSort(nums):
    # Loop invariant: nums[i] < any elements in nums[i+1:]
    for i in range(len(nums) - 1):
        # Loop invariant: nums[j] < any elements in nums[j+1:]
        for j in range(len(nums) - 1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestAscendingSort(AscendingBubbleSort)