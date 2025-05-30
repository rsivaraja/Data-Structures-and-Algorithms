def sum(n):
    if n<=1:
        return 1
    else:
        return sum(n-1)+n
print(sum(5))


def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n
print(factorial(3))

def power_of_number(b,p):
    if p==0:
        return 1
    else:
        return power_of_number(b,p-1)*b
print(power_of_number(2,3))

def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

def sum_until(n):
    if n==0:
        return 1
    else:
        sum_until(n-1)
        print(n)
sum_until(5)

def reverse(n):
    return n[::-1]
print(reverse('hello'))