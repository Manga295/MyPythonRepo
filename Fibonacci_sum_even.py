def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)
Sum =0
for e in range(1,4000000):
    a= fibonacci(e)
    if(a%2 == 0):
        Sum=Sum+a
    print(Sum)
print(Sum)