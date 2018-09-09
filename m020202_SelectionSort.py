
def AscendingSelectionSort(nums):
    # Loop invariant: nums[0:i-1] is sorted.
    # Maintaince: the smallest element in nums[i:] is switched to nums[i], so 
    #   after each iteration, nums[0:i] is sorted.
    # Termination: after len(nums) - 1 iterations, the loop ends and nums[0:] is sorted.
    i = 0
    while i < len(nums) - 1:
        smallest = i
        j = i
        while j < len(nums):
            if nums[j] < nums[smallest]:
                smallest = j
            j += 1
        nums[i], nums[smallest] = nums[smallest], nums[i]
        i += 1
    return nums

# Theres no best case or worst case, they are same.
# For an array of N elements, the algorithm runs N + (N - 1) + (N - 2) + (N - 3) + .. + 1, so the order of growth is Theta(N^2).

if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestAscendingSort(AscendingSelectionSort)
                 


