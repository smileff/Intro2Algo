from m020302_MergeSort import AscendingMergeSort, Merge
from m020100_InsertionSort import InsertionSort

def AscendingMergeSortWithSmallInsertionSort(nums, k = 10, b = -1, e = -1):
    if b == -1 or e == -1:
        b = 0
        e = len(nums)

    if e - b < k:
        # Small enough for insertion sort
        nums[b:e] = InsertionSort(nums[b:e])
    else:
        # Divide
        m = int((b + e) / 2)
        AscendingMergeSortWithSmallInsertionSort(nums, k, b, m)
        AscendingMergeSortWithSmallInsertionSort(nums, k, m, e)
        Merge(nums, b, m, e)

if __name__ == "__main__":
    from m000000_Test import TestAscendingSort
    TestAscendingSort(AscendingMergeSortWithSmallInsertionSort)
