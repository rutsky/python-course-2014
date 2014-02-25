def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

print("Factorial of 5 is", factorial(5))
