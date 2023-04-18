from math import factorial

n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

def calculate_1(n,x):

 term = lambda i: n ** i / factorial(i)

 terms = [term(i) for i in range(x + 1)]

 result = sum(terms)
 return result


n = int(input("Enter the value of n: "))

def calculate_2(n):
    global total
    if n == 0:
        return

    term = (-1)**(n-1)/n
    total += term
    calculate_2(n-1)


total = 0


print('Result for question1= ',calculate_1(n,x))
print(calculate_2(n))



















