mod = 1_000_000_007
n = int(input())
A = [[1, 1], [1, 0]]
def mat_mul(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            tmp = 0
            for k in range(len(mat1[0])):
                tmp += mat1[i][k] * mat2[k][j]
            res[i].append(tmp % mod)
    return res
def mat_pow(mat, n):
    if n == 1:
        return mat
    ret = mat_pow(mat, n//2)
    if n % 2 == 0:
        return mat_mul(ret, ret)
    else:
        return mat_mul(mat_mul(ret, ret), mat)
print(mat_pow(A, n)[1][0])