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

from utils.py import number_5
number =int(input())
    if number_5(number):
        print(f"{number} є степенем числа 5")
    else:
        print(f"{number} не є степенем числа 5")