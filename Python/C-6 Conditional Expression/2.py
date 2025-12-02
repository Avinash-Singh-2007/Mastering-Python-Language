s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
total = (s1 + s2 + s3) / 3
if total >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33:
    print("Pass")
else:
    print("Fail")
