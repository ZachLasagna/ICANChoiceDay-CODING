#1
a = int(input("Enter a number: "))
b = int(input("Enter an exponent: "))
c = 1
for d in range(b):
    c = c * a
print(c)
print("")

#2
e = [1, 2, 3, 4, 5]
f = 1
for g in e:
    print(g * f)
    f = f * 10 + 1
print("")

#3
def loop():
    j = int(input("Enter a number: "))
    h = int(input("Enter another number: "))
    i = h - j + 1
    z = j - h + 1
    if i > j:
        for i in range(i):
            print(j)
            j += 1
    elif j > h:
        for i in range(z):
            print(j)
            j -= 1
loop()
print("")

#4
def prime(a):

    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5)+1):
        if a % i == 0:
            return False

    return True
def prime2():
    a = int(input("Enter a numer: "))
    b = int(input("Enter another number: "))
    if a > b:
        r = range(b, a)
    elif b > a:
        r = range(a, b)
    for w in r:
        if prime(w):
            print(w)
prime2()
print("")

#5
def factorial(number):
    a = 1
    b = range(1, (number+1))
    for i in b:
        a = a * i
    print(a)
number = int(input("Enter a number: "))
factorial(number)