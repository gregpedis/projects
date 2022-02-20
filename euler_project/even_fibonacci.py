
def even_fibo_sum(n):
    result = 0
    a = 1
    b = 2

    while b <= n:
        if b % 2 == 0:
            result += b
        c = a+b
        a = b
        b = c
    return result


if __name__ == "__main__":
    result = even_fibo_sum(4000000)
    print(result)
