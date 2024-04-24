# r w >
a = int(input("Value of a"))
b = int(input("Value of b"))
# print(complex(a, b))
##python to convert into decimal number system

# n1 = input("Value of n1: ")
# n2 = input("Value of n2: ")
# n3 = input("Value of n3: ")

# a = int(n1)
# b = int(n2)
# c = int(n3)

# print('Octal:', oct(a))
# print('Binary:', bin(b))
# print('Hexa-decimal:', hex(c))

str_1 = "1c2"
n = int(str_1, 16)
print("string to integer", n)
# In the programmer,we are going to rewrite 2 using int() function to convert numbers from different number systems
# into decimal number system
s1 = "17"
s2 = "1110010"
s3 = "1c2"

n = int(s1, 8)
print("octal", n)
n = int(s2, 2)
print("Binary", n)
n = int(s3, 16)
print("Hexadecimal", n)
c = bin(a)
print("Binary", c)
c = oct(a)
print("Octal", c)
c = hex(a)
print("Hexadecimal", c)

if a < b:
    print("Hello")
elements = [10, 20, 30, 40, 15]
x = bytes(elements)
print(x[0])
##convert the list into bytes type array
x = bytes(elements)
print("Byte type elements", x)
x = bytearray(elements)
print("bytearray", x)

for i in elements:
    print(i)
for i in range(len(elements)):
    print(elements[i])

elements1 = [10, 20, 30, 40, 50]
x = bytearray(elements1)
x[1] = 100
x[2] = 200
for i in x:
    print(i)

t1 = (1, 2, 3, 4, 5)
print(t1[1])

s1 = {1, 2, 3, 4, 6}
print(type(s1))

# range
r = range(10)
print(r)
L = list(range(10))
print(L)

# set
s = {10, 20, 30, 40, 50, 60, 70}
print(s)
s1 = set("Abu Al Shahriar  Rifat")
print(s1)
List_to_set = set(L)
print(List_to_set.update('Bangladesh'));
print(List_to_set.remove(5))
print(List_to_set)
##make frozen set
s2={90,89,65,45};
print(frozenset(s2));
print(s2);

##dictionary
d={2019005005:'Rifat',2019005006:'Kifayat',2019005007:'Rahima',2019005008:'Karima'}
for i in d.keys():print(i);
for J in d.values():print(J);
Values=d.values();
print(Values)
print(d[2019005005]);

'''
importan Escape Character in Strings
9 escape charter in the python
1.\
2.\\
3.\'
4.\"
5.\b
6.\r
7.\t
8.\v
9.\n
'''
ch='A';
print(ch);
str1='Bharat';
print(str1[0]);

for i in range(len(str1)):
    print(str1[i].isupper());
    
print(22/7);


