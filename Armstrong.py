n = int(input())
s = str(n) 
a = int(s[0]) ** 3
b = int(s[1]) ** 3
c = int(s[2]) ** 3
if a + b + c == n:
    print("True")
else:
    print("False")