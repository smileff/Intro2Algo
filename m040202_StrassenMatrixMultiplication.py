from m000000_Matrix import Matrix, SizeNotMatch, GetRandomMatrix
from m000000_Test import ReturnPerformance

@ReturnPerformance
def Multiply(mat1, mat2):
    if mat1.RowNum != mat2.RowNum or mat1.ColNum != mat2.ColNum:
        raise SizeNotMatch()
    res = Matrix(mat1.RowNum, mat2.ColNum)
    for r in range(mat1.RowNum):
        for c in range(mat2.ColNum):
            elem = 0
            for i in range(mat1.ColNum):
                elem += mat1.Get(r, i) * mat2.Get(i, c)
            res.Set(r, c, elem)
    return res

@ReturnPerformance
def StrassenMultiply(mat1, mat2):
    def Mul(mat1, mat2):
        rs1, re1, cs1, ce1 = 0, mat1.RowNum, 0, mat1.ColNum
        rs2, re2, cs2, ce2 = 0, mat2.RowNum, 0, mat2.ColNum

        if re1 - rs1 == 1:
            return Matrix(1, 1, [mat1.Get(0, 0) * mat2.Get(0, 0)])
        else:
            # Subdivide
            rm1 = int((rs1 + re1) / 2)
            cm1 = int((cs1 + ce1) / 2)
            rm2 = int((rs2 + re2) / 2)
            cm2 = int((cs2 + ce2) / 2)

            mat1_11 = mat1.GetSubMat(rs1, rm1, cs1, cm1)
            mat1_12 = mat1.GetSubMat(rs1, rm1, cm1, ce1)
            mat1_21 = mat1.GetSubMat(rm1, re1, cs1, cm1)
            mat1_22 = mat1.GetSubMat(rm1, re1, cm1, ce1)

            mat2_11 = mat2.GetSubMat(rs2, rm2, cs2, cm2)
            mat2_12 = mat2.GetSubMat(rs2, rm2, cm2, ce2)
            mat2_21 = mat2.GetSubMat(rm2, re2, cs2, cm2)
            mat2_22 = mat2.GetSubMat(rm2, re2, cm2, ce2)

            s1 = mat2_12 - mat2_22
            s2 = mat1_11 + mat1_12
            s3 = mat1_21 + mat1_22
            s4 = mat2_21 - mat2_11
            s5 = mat1_11 + mat1_22
            s6 = mat2_11 + mat2_22
            s7 = mat1_12 - mat1_22
            s8 = mat2_21 + mat2_22
            s9 = mat1_11 - mat1_21
            s10 = mat2_11 + mat2_12

            p1 = Mul(mat1_11, s1)
            p2 = Mul(s2, mat2_22)
            p3 = Mul(s3, mat2_11)
            p4 = Mul(mat1_22, s4)
            p5 = Mul(s5, s6)
            p6 = Mul(s7, s8)
            p7 = Mul(s9, s10)

            c11 = p5 + p4 - p2 + p6
            c12 = p1 + p2
            c21 = p3 + p4
            c22 = p5 + p1 - p3 - p7

            res = Matrix(mat1.RowNum, mat2.ColNum)
            res.SetSubMat(rs1, rm1, cs2, cm2, c11)
            res.SetSubMat(rs1, rm1, cm2, ce2, c12)
            res.SetSubMat(rm1, re1, cs2, cm2, c21)
            res.SetSubMat(rm1, re1, cm2, ce2, c22)

            return res

    return Mul(mat1, mat2)


if __name__ == "__main__":
    mat1 = Matrix(2, 2, [1, 3, 7, 5])
    mat2 = Matrix(2, 2, [6, 8, 4, 2])

    mat3, t0 = Multiply(mat1, mat2)
    print("Mul with brute force way, time: {}".format(t0))
    print(mat3)

    mat4, t0 = StrassenMultiply(mat1, mat2)
    print("Mul with strassen multipty, time: {}".format(t0))
    print(mat4)

    if mat3 == mat4:
        print("Two results match.")
    else:
        print("Two results do not match.")

    print("")

    matSizes = [2 ** 7, 2 ** 8, 2 ** 9]
    for matSize in matSizes:
        print("Matrix size: {}".format(matSize))
        mat1 = GetRandomMatrix(matSize, matSize)
        mat2 = GetRandomMatrix(matSize, matSize)

        mat3, t0 = Multiply(mat1, mat2)
        print("Mul with brute force way, time: {}".format(t0))

        mat4, t0 = StrassenMultiply(mat1, mat2)
        print("Mul with strassen multipty, time: {}".format(t0))

        if mat3 == mat4:
            print("Two results match.")
        else:
            print("Two results do not match.")