import string
import random

s1= string.ascii_lowercase
s2= string.ascii_uppercase
s3= string.digits
s4= string.punctuation
p=int(input("Enter Password Length:"))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
random.shuffle(s)
print("PASSWORD :",end='')
print("".join(s[0:p]))
