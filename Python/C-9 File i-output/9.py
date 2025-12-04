first_file = ""
second_file = ""
with open("./this.txt","r")as f:
    first_file = f.read()
with open("./this-copy.txt","r")as f:
    second_file = f.read()

if(first_file.strip() == second_file.strip()):
    print("Content is same in both file")
else:
    print("Content is not same in both file")