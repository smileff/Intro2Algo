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

    def GetSubMat(self, r0, r1, c0, c1):
        elems = []
        for r in range(r0, r1):
            elems.extend(self.elems[r * self.colNum + c0 : r * self.colNum + c1])
        return Matrix(r1 - r0, c1 - c0, elems)

    def Set(self, r, c, v):
        self.elems[r * self.colNum + c] = v

    def SetSubMat(self, r0, r1, c0, c1, subMat):
        if r1 - r0 != subMat.rowNum or c1 - c0 != subMat.colNum:
            raise SizeNotMatch
        for r in range(r0, r1):
            for c in range(c0, c1):
                self.elems[r * self.colNum + c] = subMat.elems[(r - r0) * subMat.colNum + c - c0]

    def __add__(self, mat):
        if self.rowNum != mat.rowNum or self.colNum != mat.colNum:
            raise SizeNotMatch()
        return Matrix(self.rowNum, self.colNum, [v0 + v1 for v0, v1 in zip(self.elems, mat.elems)])
    
    def __mul__(self, scalar):
        return Matrix(self.rowNum, self.colNum, [v * scalar for v in self.elems])

    def __sub__(self, mat):
        return self.__add__(mat * -1)

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