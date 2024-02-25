def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def simple(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def number_5(num):
    if num <= 0:
        return False
    while num % 5 == 0:
        num /= 5
    return num == 1