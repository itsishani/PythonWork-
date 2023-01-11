#Read a list of elements from the user and perform the following operations using functions: search(key): to find the given key in the list and display the position of the key if found, otherwise display appropriate message, maximum(Lst) and minimum(Lst) to find the maximum and minimum number respectively from the list.
m = int(input())
l = []
for i in range(m):
    n = int(input())
    l.append(n)
f = int(input("Key to be searched :"))
if f in l:
    print("Key is present")
else:
    print("Key is not present")
l.sort()
s = l[0]
b = l[-1]
print("Minimum in the list is ",s)
print("maximum in the list is ",b)
#Write a function sorted that takes a list as a parameter and sort the elements in lexicographical order. Test the function for a list of names and print the sorted list
a_list = ['Aashu','Ishani','Sam']
b_list = sorted(a_list, key=str.lower)
print(b_list)
#A list of students registered for Python course. Perform the following operations (use inbuilt functions) and print the output:
l = ['a', 'b', 'c', 'd']
# 1 new student
s = input("Enter the name of new student: ")
l.append(s)
# 2 no of students
e = len(l)
print("Number of students registered: ", e)
# 3 sorting the list
q = l.sort()
print(q)
# 4 inserting
n = input("Name to be inserted: ")
l.append(n)
# 5 Search
w = input("Name to be searched: ")
if w in l:
    print("Student is present")
else:
    print("Student is absent")
# 6 Remove
l.remove('a')
print(l)
#Consider a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers present at odd index into a new tuple.
t = (1,3,2,4,6,5)
def oddTuples(aTup):
    return aTup[::2]
nt = oddTuples(t)
print(nt)
#Consider a list containing food items. Another list contains its corresponding price. Create these two lists by getting the input from user. Now get the items ordered by the customer in a tuple. Display the total cost of the ordered food.
#Example: Available Fruits: Oranges, Mangoes, Apple, Grapes, Papaya 
#Price per Kg: 60, 80, 220, 80, 90
#Your order (in Kgs): 2, 0, 1, 0, 0.500 
#Total Amount: Rs. 340
n = int(input())
l1 = []
l2 = []
l3 = []
st = 0
for i in range (n):
    f = input()
    p = int(input())
    o = int(input())
    st = st + p*o
    l1.append(f)
    l2.append(p)
    l3.append(o)
print(l1)
print(l2)
print(l3)
print(st)
#Matrix is a rectangular array of data or numbers.Get the values of r and c from the user. Write a function to create and return the r X c matrix with the user input. Write another function to print the sums of each row.
r = int(input())
c = int(input())
l1 = []
for i in range (c):
    l2 = []
    for i in range (r):
        n = input()
        l2.append(n)
    l1.append(l2)
print(l1)

print ('\n'.join([' '.join(row) for row in l1]))
#Find the transpose of a given matrix using list comprehension.
r = int(input())
c = int(input())
l1 = []
for i in range (c):
    l2 = []
    for i in range (r):
        n = input()
        l2.append(n)
    l1.append(l2)
print(l1)
for cols in zip(*l1):  # transposed
    print(' '.join(cols))
#Write a user-defined function to print and store squares of numbers for the given range into a dictionary.
#Example: For range 2 to N (both inclusive): If N = 5, the contents of the dictionary would be {2: 4, 3: 9, 4: 16, 5: 25}
n = int(input())
d ={}
for i in range(2,n+1):
    d[i]=i**2
print(d)
#Create a new dictionary by combining two dictionaries whose key-value pairs are given. The new dictionary has to be created by adding values for common keys from the two dictionaries. 
#Dict1 = {'A': 100, 'B': 200, 'C':300}
#Dict2 = {'A': 300, 'B': 500, 'D':400}
#Sample output: NewDict = {'A': 400, 'B': 700, 'C': 300, 'D': 400}
Dict1 = {'A': 100, 'B': 200, 'C':300}
Dict2 = {'A': 300, 'B': 500, 'C':400}
newd = {}
for i in Dict1.keys():
    if i in Dict2.keys():
        newd[i]=Dict1[i]+Dict2[i]
print(newd)
