def factorial(n):
    if n < 0:
        return "Undefined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
fact = factorial(num)
if isinstance(fact, str):
    print(fact)
else:
    print(f"The factorial of {num} is {fact}.")