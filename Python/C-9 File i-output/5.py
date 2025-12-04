list = ["Donkey","Lion","Girafe"]

with open("./poems.txt","r+")as f:
    text = f.read()
    for l in list:
        text = text.replace(l,"######")
    f.seek(0)
    f.write(text)