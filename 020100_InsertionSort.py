def InsertionSort(nums):
    print("Input numbers: ", nums)
    for j in range(1, len(nums)):
        value = nums[j]
        i = j
        while i > 0 and nums[i - 1] > value:
            nums[i] = nums[i - 1]
            i += 1
        nums[i] = value
        print("After {}-th iteration: ".format(j), nums)
    return nums

if __file__ == "__main__":
    

