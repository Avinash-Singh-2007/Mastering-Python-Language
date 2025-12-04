with open("./poems.txt","r") as f:
    text = f.read()
    text = text.lower()

if text.find("twinkle") == -1:
    print("Twinkle not there")  
else:
    print("Twinkle there")      