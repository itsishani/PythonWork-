#Write a function power(X,N) that will allow a floating-point number to be raised to an integer power and return the result. i.e. Y = X N . Write a Python program to invoke the function
def power(x,n):
    l = x**n
    return(l)
b = int(input())
c = int(input())
print(power(b,c))
#Define a function CheckOddEven(num) that checks if the num is odd or even; the function sets a flag accordingly and returns it. Use this function to find the sum of even and odd numbers separately, from a given input of N numbers.
def CheckOddEven(n):
    if n%2==0:
        Flag = True
        print("Number is even ")
    else:
        Flag = False
        print("Number is odd")
    return Flag
print(CheckOddEven(int(input())))
#Define a function to find the factors of the given number as an argument. If the number is not given, then display the factors of the default argument.
def factors(n):
    l =[]
    for i in range(1,n):
        if n%i == 0:
            l.append(i)
    return l

print(factors(int(input())))
#Calculate factorial of a given number using recursive function. The base case should handle the negative integers by printing an error message and returns none to indicate that something went wrong.
n = int(input("enter number:"))
i = 1
fac = 1
if n > 0:
    while i <= n:
        fac = fac*i
        i += 1
    print(fac)
else:
    print("Error")
#Compute the sum of the digits of a given number using recursion.
n = input("Give number: ")
s = 0
for digit in str(n):
    s += int(digit)
print(s)
#Check whether a given number is prime or not using recursive function.
num = int(input("give number: "))
if num>1:
    for i in range (2,num):
        if num%i == 0:
           print ("number is not prime")
           break
    else:
        print("number is prime")
#calculate gcd
a = int(input("Give number:  "))
b = int(input("Give Number: "))
def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y
# Driver code
g, x, y = gcdExtended(a, b)
print("gcd(", a, ",", b, ") = ", g)
#The Ackermann function, A(m, n) is defined as follows. Solve the above problem recursively for different values of m and n.
def A(m, n):
    if m == 0:
        f = n+1
    elif m > 0 and n == 0:
        f = A(m-1,1)
    elif m > 0 and n > 0:
        f = A(m-1, A(m, n-1))
    return f
s = int(input())
t = int(input())
print(A(s,t))
#Define a function to count the number of occurrences of a substring in a given string and print the starting index of the substring for each occurrence.
m = input()
def count(n):
    s = m.count(n)
    return s
n = input()
print(count(n))
print(m.index(n))
#Write a user-defined function to check whether a given text is palindrome or not using string slice method.
s = input()
reverse = s[::-1]
if s== reverse:
    print("it is a palindrome!")
else:
    print("It is not a palindrome.")
#Write a function strip_characters(str,chars) which removes the characters mentioned in chars from the string str. E.g strip_characters(‘The quick brown fox jumps over the lazy dog’,’aeiou’)
def strip_characters(str):
    h = str.replace('a','')
    t = h.replace('e','')
    y = t.replace('i','')
    a = y.replace('o','')
    q = a.replace('u','')
    return q
str = input()
print(strip_characters(str))


