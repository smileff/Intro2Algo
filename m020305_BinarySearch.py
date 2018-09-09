def BinarySearch(sortedNums, k):
    # Assuming sortedNums are in ascending order.
    # Loop invariant:
    #   Before sorting, sortedNums[i] <= k <= sortedNums[j - 1]
    i = 0
    j = len(sortedNums)
    while i < j:
        m = int((i + j) / 2)
        if sortedNums[m] == k:
            return m
        elif k < sortedNums[m]:
            j = m
        else:
            i = m + 1
    # Not found
    return None

if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestSearchInAscendingSortedNums(BinarySearch)

    
