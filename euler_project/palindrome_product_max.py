
def is_palindrome(product):
    product = str(product)
    l = len(product) // 2
    if product[:l] == product[:l-1:-1]:
        return True
    return False


def loop_products(ceiling):
    palindromes = []
    for n1 in reversed(range(1, ceiling)):
        for n2 in reversed(range(1, ceiling)):
            p = n1 * n2
            if is_palindrome(p):
                palindromes.append((n1, n2, p))
    return palindromes


def isMax(n):
    return n[2]


if __name__ == "__main__":
    palindromes = loop_products(1000)
    m = max(palindromes, key=isMax)
    print(m)
