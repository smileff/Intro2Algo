def AscendingMergeSort(nums, b = -1, e = -1):

    def Merge(nums, p, q, r):
        L = nums[p:q]
        R = nums[q:r]
        i = 0
        j = 0
        for k in range(p, r):
            if i >= len(L):
                nums[k] = R[j]
                j += 1
            elif j >= len(R):
                nums[k] = L[i]
                i += 1
            else:
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1

    # Check the special condition that sort the whole array.
    if b == -1 or e == -1:
        b = 0
        e = len(nums)
    
    if e == b or e == b + 1:
        pass
    else:
        # Divide
        m = int((b + e) / 2)
        # Conquer
        AscendingMergeSort(nums, b, m)
        AscendingMergeSort(nums, m, e)
        # Combine
        Merge(nums, b, m, e)


if __name__ == "__main__":
    import m000000_Test as Test
    Test.TestAscendingSort(AscendingMergeSort)