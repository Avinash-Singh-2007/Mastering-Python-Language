i = 0
found = False
with open("./poems.txt","r")as f:
    text = f.readline()
    while len(text) != 0:
        i += 1
        find = text.lower().find("python")
        if  find != -1:
            print(f"Talking about pythonin line no {i}")
            found = True   
        text = f.readline()
        
if not found:
    print("Not talking about python")           