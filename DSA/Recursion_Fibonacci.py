def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = input('Enter Number: ')
n = int(num)
for i in range(1,n+1):
    print(fibonacci(i), end=' ')