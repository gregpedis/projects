
def calculate_sum(n):
    result = 0
    for x in range(n):
        if(x % 3 == 0) or (x % 5 == 0):
            result += x
    return result


if __name__ == "__main__":
    result = calculate_sum(1000)
    print(result)
