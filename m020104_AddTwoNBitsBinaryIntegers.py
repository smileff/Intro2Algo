def AddTwoNBitsBinaryIntegers(num1Bits, num2Bits):
    i, j = 0, 0
    sumBits = []
    addon = 0
    while i < len(num1Bits) or j < len(num2Bits):
        i, b1 = (i + 1, num1Bits[i]) if i < len(num1Bits) else (i, 0)
        j, b2 = (j + 1, num2Bits[j]) if j < len(num2Bits) else (j, 0)
        bSum = b1 + b2 + addon
        addon = 1 if bSum >= 2 else 0
        bSum -= addon * 2
        sumBits.append(bSum)
    sumBits.append(addon)
    return sumBits


if __name__ == "__main__":
    testNum1Bits = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    testNum2Bits = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
    sumBits = AddTwoNBitsBinaryIntegers(testNum1Bits, testNum2Bits)
    print("Num1: {}".format(testNum1Bits))
    print("Num2: {}".format(testNum2Bits))
    print("Sum:  {}".format(sumBits))