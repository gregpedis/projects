
def is_prime(n):
    if n in (1, 2):
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorize(number, factors, powers):
    if is_prime(number):
        if number in factors:
            idx = factors.index(number)
            powers[idx] += 1
        else:
            factors.append(number)
            powers.append(1)
    else:
        divisor = 2
        while number % divisor != 0:
            divisor += 1

        if divisor in factors:
            idx = factors.index(divisor)
            powers[idx] += 1
        else:
            factors.append(divisor)
            powers.append(1)
        factorize(number // divisor, factors, powers)


def smallest_multiple(number):
    result_factors = []
    result_powers = []
    for i in range(1, number+1):
        factors = []
        powers = []
        factorize(i, factors, powers)
        for idx, factor in enumerate(factors):
            if factor in result_factors:
                result_idx = result_factors.index(factor)
                result_powers[result_idx] = max(
                    result_powers[result_idx], powers[idx])
            else:
                result_factors.append(factor)
                result_powers.append(powers[idx])

    return (result_factors, result_powers)


if __name__ == "__main__":
    factors, powers = smallest_multiple(20)
    result = 1
    for f, p in list(zip(factors, powers)):
        result *= f**p

    print(result)
