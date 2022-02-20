
def is_prime(f):
    for i in range(2, f):
        if f % i == 0:
            return False
    return True


def prime_factors(n):
    result = []
    factor = 2
    while n > 1:
        if is_prime(factor):
            if n % factor == 0:
                n = n // factor
                result.append(factor)
            else:
                factor += 1
        else:
            factor += 1
    return result


if __name__ == "__main__":
    result = prime_factors(600851475143)
    print(max(result))
