# Return the factorial of a given number


def factorial(num, total = 0):
    if num == 1:
        return total + 1
    else:
        total += num
        num -= 1
        return factorial(num, total)


if __name__ == '__main__':
    print(factorial(6))
