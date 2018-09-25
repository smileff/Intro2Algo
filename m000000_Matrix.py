from m000000_Test import GetRandomIntegers
import copy

class SizeNotMatch(Exception):
    pass

class Matrix:
    def __init__(self, rowNum, colNum, elems = None):
        # Row major
        self.rowNum, self.colNum = rowNum, colNum

        if elems != None:
            if len(elems) != rowNum * colNum:
                raise SizeNotMatch()
            self.elems = copy.copy(elems)
        else:
             self.elems = [0 for i in range(rowNum * colNum)]

    @property
    def RowNum(self):
        return self.rowNum

    @property
    def ColNum(self):
        return self.colNum

    def Get(self, r, c):
        return self.elems[r * self.colNum + c]

    def GetSubRow(self, r, c0, c1):
        offset = r * self.colNum
        return self.elems[offset + c0 : offset + c1]

    def GetRow(self, r):
        return self.GetSubRow(r, 0, self.colNum)

    def GetSubMat(self, r0, r1, c0, c1):
        elems = []
        for r in range(r0, r1):
            elems.extend(self.elems[r * self.colNum + c0 : r * self.colNum + c1])
        return Matrix(r1 - r0, c1 - c0, elems)

    def Set(self, r, c, v):
        self.elems[r * self.colNum + c] = v

    def SetSubRow(self, r, c0, c1, elems):
        assert c1 - c0 == len(elems)
        self.elems[r * self.colNum + c0 : r * self.colNum + c1] = elems

    def SetRow(self, r, elems):
        self.SetSubRow(r, 0, self.colNum, elems)

    def SetSubMat(self, r0, r1, c0, c1, subMat):
        if r1 - r0 != subMat.rowNum or c1 - c0 != subMat.colNum:
            raise SizeNotMatch
        for r in range(r0, r1):
            dstOffset = r * self.ColNum
            srcOffset = (r - r0) * subMat.colNum
            self.elems[dstOffset + c0 : dstOffset + c1] = subMat.elems[srcOffset : srcOffset + subMat.colNum]

    # Arithmetic operations

    def __add__(self, mat):
        if self.rowNum != mat.rowNum or self.colNum != mat.colNum:
            raise SizeNotMatch()
        return Matrix(self.rowNum, self.colNum, [v0 + v1 for v0, v1 in zip(self.elems, mat.elems)])

    def AddSubMap(self, r0, r1, c0, c1, mat, y0, y1, x0, x1, resMat = None, a = None, b = None):
        assert r1 - r0 == y1 - y0 and c1 - c0 == x1 - x0
        rn = r1 - r0
        cn = c1 - c0
        if resMat == None:
            resMat = Matrix(rn, cn)
            a = 0
            b = 0
        for r in range(rn):
            resMat.SetSubRow(a + r, b, b + cn, [m + n for m, n in zip(self.GetSubRow(r0 + r, c0, c1), mat.GetSubRow(y0 + r, x0, x1))])
        return resMat

    def __sub__(self, mat):
        if self.rowNum != mat.rowNum or self.colNum != mat.colNum:
            raise SizeNotMatch()
        return Matrix(self.rowNum, self.colNum, [v0 - v1 for v0, v1 in zip(self.elems, mat.elems)])

    def SubtractSubMap(self, r0, r1, c0, c1, mat, y0, y1, x0, x1, resMat = None, a = None, b = None):
        assert r1 - r0 == y1 - y0 and c1 - c0 == x1 - x0
        rn = r1 - r0
        cn = c1 - c0
        if resMat == None:
            resMat = Matrix(rn, cn)
            a = 0
            b = 0
        for r in range(rn):
            resMat.SetSubRow(a + r, b, b + cn, [m - n for m, n in zip(self.GetSubRow(r0 + r, c0, c1), mat.GetSubRow(y0 + r, x0, x1))])

    def __mul__(self, scalar):
        return Matrix(self.rowNum, self.colNum, [v * scalar for v in self.elems])

    def __eq__(self, mat):
        for v1, v2 in zip(self.elems, mat.elems):
            if v1 != v2:
                return False
        return True

    def __str__(self):
        s = ""
        for r in range(self.rowNum):
            for c in range(self.colNum):
                s += "{:8}".format(self.Get(r, c))
            s += '\n'
        return s

def GetRandomMatrix(rowNum, colNum):
    return Matrix(rowNum, colNum, GetRandomIntegers(rowNum * colNum))

if __name__ == "__main__":
    # Unit test
    a = Matrix(2, 2, [1, 2, 3, 4])
    print(a)

    print("Multiply 10:")
    b = a * 10
    print(b)

    print("Sum of 2 matrixs:")
    c = a + b
    print(c)

    print("Submat of right part of a:")
    d = a.GetSubMat(0, a.RowNum, 1, a.ColNum)
    print(d)

    print("Modify the right part of a:")
    a.SetSubMat(0, a.RowNum, 1, a.ColNum, d * 10)
    print(a)

    # Raise exception
    # a + Matrix(2, 3)