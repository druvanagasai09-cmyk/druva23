def calculate_sum(n) :
    if n == 1 :
        return 1
    else :
        return n + calculate_sum(n - 1)

n = int(input("enter a positive number :"))

result = calculate_sum(n)

print(" sum of first", n, "natural numbers =", result)