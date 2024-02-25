from utils.py import factorial
n =int(input())
result = factorial(n)
print(result)

from utils.py import simple
number=int(input())
if simple(number):
    print("просте число")
else:
    print("не просте число")

from utils.py import number5
n =int(input())
    if number5(number):
        print(f"{n} є степенем числа 5")
    else:
        print(f"{n} не є степенем числа 5")