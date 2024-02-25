from utils.py import factorial
n = int(input())
result = factorial(n)
print(result)

from utils.py import simple
number = int(input())
if simple(number):
    print("просте число")
else:
    print("не просте число")