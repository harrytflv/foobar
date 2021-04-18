from fractions import Fraction

def solution(m):
    if size(m) < 2:
        return [1,1]

    # Normalize
    sums = [0 for i in range(size(m))]
    for i in range(size(m)):
        sums[i] = sum(m[i])
        if sums[i] != 0:
            for j in range(size(m)):
                m[i][j] = Fraction(m[i][j], sums[i])

    # Canonical form
    t = sum(1 if sum(m[i]) != 0 else 0 for i in range(size(m)))
    r = size(m) - t
    Q_matrix, R_matrix = [[0 for j in range(t)] for i in range(t)], [[0 for j in range(r)] for i in range(t)]
    i_p = 0
    for i in range(size(m)):
        if sum(m[i]) > 0:
            j_p = 0
            for j in range(size(m)):
                if sum(m[j]) > 0:
                    Q_matrix[i_p][j_p] = m[i][j]
                    j_p += 1
                else:
                    R_matrix[i_p][j - j_p] = m[i][j]
            i_p += 1
    
    F_matrix = inverse(matrix_minus(identity_matrix(size(Q_matrix)), Q_matrix))
    FR = matrix_multiply_matrix(F_matrix, R_matrix)

    # Shortcut for [1, 0, ... 0] * fundamental_matrix
    ret = FR[0]

    sum_of_ret = sum(ret)
    ret = map(lambda x: x / sum_of_ret, ret)
    dom = 1
    for i in range(len(ret)):
        if ret[i] != 0:
            curr_dom = ret[i].denominator
            dom *= curr_dom
            for j in range(len(ret)):
                ret[j] *= curr_dom
    ret = map(lambda x: x if x == 0 else x.numerator, ret)
    ret.append(dom)

    return ret

def rest_of_matrix(m, position):
    rows = filter(lambda x: x != position[0], range(size(m)))
    cols = filter(lambda x: x != position[1], range(size(m)))
    return [[m[r][c] for c in cols] for r in rows]

def determinant(m):
    if size(m) == 1:
        return m[0][0]
    sign, det = 1, 0
    for j in range(size(m)):
        det += sign * m[0][j] * determinant(rest_of_matrix(m, (0, j)))
        sign = -sign
    return det

def scalar_multiply_matrix(a, m):
    return [[a * m[i][j] for j in range(size(m))] for i in range(size(m))]

def matrix_multiply_matrix(m1, m2):
    return [[sum([m1[i][k]*m2[k][j] for k in range(len(m2))]) for j in range(len(m2[0]))] for i in range(len(m1))]

def adjugate(m):
    return [[(1 if even(i+j) else -1) * determinant(rest_of_matrix(m, (i, j))) for j in range(size(m))] for i in range(size(m))]

def transpose(m):
    return [[m[j][i] for j in range(size(m))] for i in range(size(m))]

def even(num):
    return num % 2 == 0

def matrix_minus(m1, m2):
    return [[m1[i][j] - m2[i][j] for j in range(size(m1))] for i in range(size(m1))]

# Size of matrix m assuming square matrix.
def size(m):
    return len(m)

def inverse(m):
    d = determinant(m)
    if isinstance(d, int):
        d = float(d)
    return scalar_multiply_matrix(1 / d, transpose(adjugate(m)))

def identity_matrix(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def print_matrix(m):
    for i in range(len(m)):
        print([(m[i][j].numerator, m[i][j].denominator) for j in range(len(m[0]))])
    print()

def main():
    t = Test(solution)
    t.add_test_case([7, 6, 8, 21], [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    t.add_test_case([0, 3, 2, 9, 14], [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])
    t.add_test_case([10, 5, 3, 18], [
        [0, 2, 0, 1, 0, 0],
        [0, 0, 3, 0, 1, 0],
        [4, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ])
    t.add_test_case([1, 17, 18], [
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 2],
        [0, 3, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ])
    t.add_test_case([1, 1], [
        [1]
    ])
    t.run()

from datetime import datetime
import copy

class Test:
    def __init__(self, f):
        self.f = f
        self.test_cases = []

    def add_test_case(self, expected_out, *argv):
        self.test_cases.append((expected_out, argv))

    def run(self):
        start = datetime.now()

        passed = True
        for test_case in self.test_cases:
            res = self.f(*(copy.deepcopy(test_case[1])))
            if res == test_case[0]:
                continue
            print("Input:           ", test_case[1])
            print("Expected Output: ", test_case[0])
            print("Output:          ", res)
            print()
            passed = False

        end = datetime.now()
        print(end - start)

        if passed:
            print("PASSED")

if __name__ == "__main__":
    main()
