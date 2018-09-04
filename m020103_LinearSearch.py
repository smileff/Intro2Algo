# Linear search

def LinearSearch(nums, val):
    # Loop invariant:
    # At the start of each iteration, nums[0:j-1] do not contain val.
    j = 0
    # Initialization: j-1 == -1, which is out the range of array.
    while (j < len(nums)):
        if nums[j] != val:
            # Maintenmance: as nums[j] != val, after j+=1 nums[0:j-1] do not contain val, as nums[0:j-2]
            j += 1
        else:
            # Termination, value found, return the index.
            return j
    # Termination, value is not found, return None
    return None
    
            
if __name__ == "__main__":
    testNums = [1, 5, 4, 6, 7, 9]
    testVal = 7
    idx = LinearSearch(testNums, testVal)
    print("To find {} in {}, result idx: {}", testVal, testNums, idx)