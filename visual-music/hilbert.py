import numpy as np
import math


def create_array_16():
    return np.array([
        [0, 1, 14, 15],
        [3, 2, 13, 12],
        [4, 7, 8, 11],
        [5, 6, 9, 10]])


def create_array_64():
    return np.array([
        [0, 3, 4, 5, 58, 59, 60, 63],
        [1, 2, 7, 6, 57, 56, 61, 62],
        [14, 13, 8, 9, 54, 55, 50, 49],
        [15, 12, 11, 10, 53, 52, 51, 48],
        [16, 17, 30, 31, 32, 33, 46, 47],
        [19, 18, 29, 28, 35, 34, 45, 44],
        [20, 23, 24, 27, 36, 39, 40, 43],
        [21, 22, 25, 26, 37, 38, 41, 42]
    ])


def rotnflip(mtrx):
    try:
        return np.fliplr(np.rot90(mtrx))
    except:
        return mtrx


def hilb_line(matrix):
    if matrix.size == 1:
        return [matrix[0][0]]
    else:
        dx, _ = matrix.shape
        halfd = dx//2
        tl = hilb_line(np.transpose(matrix[:halfd, :halfd]))
        bl = hilb_line(matrix[halfd:, :halfd])
        br = hilb_line(matrix[halfd:, halfd:])
        tr = hilb_line(rotnflip(matrix[:halfd, halfd:]))
        return tl + bl + br + tr


def hilb_space(line):
    if len(line) == 1:
        return line[0]
    else:
        ln = len(line)//4
        d = int(math.sqrt(len(line)))
        halfd = d//2
        matrix = np.empty((d, d), dtype=int)
        matrix[:halfd, :halfd] = np.transpose(hilb_space(line[0: ln]))
        matrix[halfd:d, :halfd] = hilb_space(line[ln: 2*ln])
        matrix[halfd:d, halfd:d] = hilb_space(line[2*ln: 3*ln])
        matrix[:halfd, halfd:d] = rotnflip(hilb_space(line[3*ln: 4*ln]))
        return matrix


def matrix_equality(left, right):
    for lxs, rxs in zip(left, right):
        for ly, ry in zip(lxs, rxs):
            if ly != ry:
                return False
    return True


if __name__ == "__main__":
    matrix = create_array_64()
    line = hilb_line(matrix)
    print(line)

    reverted_matrix = hilb_space(line)
    print(matrix_equality(matrix, reverted_matrix))
