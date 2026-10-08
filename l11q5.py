def recursive_factorial(n) :
    if n==0 or n==1:
        return 1
    else:
        return n * recursive_factorial(n-1)

def iterative_factorial(n):
    result = 1

    for i in range(1, n + 1):
       result =  result * i
    return result    

n = int(input("Enter a number: "))

recursive_result = recursive_factorial(n)
iterative_result = iterative_factorial(n)

print("\n======FACTORIALCOMPARISON======")
print("Recursive result :", recursive_result)
print("Iterative result :", iterative_result)

if recursive_result == iterative_result:
    print("Both methods give the same result.")