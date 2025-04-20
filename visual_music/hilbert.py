import numpy as np
import math


# Creates an 4 by 4 Hilbert Curve for testing purposes.
def _create_array_16():
    return np.array([
        [0, 1, 14, 15],
        [3, 2, 13, 12],
        [4, 7, 8, 11],
        [5, 6, 9, 10]])


# Creates an 8 by 8 Hilbert Curve for testing purposes.
def _create_array_64():
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


# Rotates 90 degrees and flips a matrix left to right.
def _rotnflip(mtrx):
    try:
        return np.fliplr(np.rot90(mtrx))
    except:
        return mtrx


# Takes a hilbert curve as a 2-D matrix
# and returns a line as a 1-D matrix.
def hilb_line(matrix):
    if matrix.size == 1:
        return [matrix[0][0]]
    else:
        dx, _ = matrix.shape
        halfd = dx//2
        tl = hilb_line(np.transpose(matrix[:halfd, :halfd]))
        bl = hilb_line(matrix[halfd:, :halfd])
        br = hilb_line(matrix[halfd:, halfd:])
        tr = hilb_line(_rotnflip(matrix[:halfd, halfd:]))
        return tl + bl + br + tr


# Takes a line as a 1-D matrix
# and returns a hilbert curve as a 2-D matrix.
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
        matrix[:halfd, halfd:d] = _rotnflip(hilb_space(line[3*ln: 4*ln]))
        return matrix


# Normalizes a 1-D matrix line to a hilbert-compliant 1-D line matrix.
def normalize_line_size(line):
    np_line = np.array(line)
    l = np_line.size

    if not l:
        return None

    np_line = np_line.reshape(l)

    if l == 1:
        return np_line[0]

    # To use hilbert convertion the line has to be a power of 4.
    scale = int(math.log(l, 4))
    new_l = 4**scale

    # Trimming the line, first doing floor division
    # and then substraction in case of odd, which has non-zero remainder.
    # Substraction is used instead of modulus %, since it's faster.
    trim_l = l - new_l
    trim_ll = trim_l // 2
    trim_lr = trim_l - trim_ll

    # Voila, returns a 1-D line matrix with hilbert-compliant size.
    return np_line[trim_ll: -trim_lr]


# Normalizes a 2-D matrix to a square, hilbert-compliant 2-D matrix.
def normalize_matrix_size(matrix):
    np_matrix = np.array(matrix)
    x, y = np_matrix.shape
    # Normalizing according to minimum dimension,
    # since the result is a square matrix.
    min_d = min(x, y)

    if not min_d:
        return None
    if min_d == 1:
        return np_matrix[0, 0]

    # To use hilbert convertion each dimension
    # has to be a power of 2.
    scale = int(math.log2(min_d))
    new_d = 2**scale

    # Trimming each size, first doing floor division
    # and then substraction in case of odd, which has non-zero remainder.
    # Substraction is used instead of modulus %, since it's faster.
    trim_x, trim_y = x-new_d, y-new_d
    trim_xl, trim_yl = trim_x//2, trim_y//2
    trim_xr, trim_yr = trim_x-trim_xl, trim_y-trim_yl

    # Voila, returns a square 2-D matrix with hilbert-compliant size.
    return np_matrix[trim_xl: -trim_xr, trim_yl: -trim_yr]


# Compares the size and the elements, one by one,
# of two matrices.
def matrix_equality(left, right):
    for lxs, rxs in zip(left, right):
        for ly, ry in zip(lxs, rxs):
            if ly != ry:
                return False
    return True


# Ze main entrypoint.
if __name__ == "__main__":
    matrix = _create_array_64()
    line = hilb_line(matrix)
    print(line)

    reverted_matrix = hilb_space(line)
    print(matrix_equality(matrix, reverted_matrix))
