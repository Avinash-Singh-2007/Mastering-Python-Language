with open("./poems.txt","r+")as f:
    text = f.read()
    text = text.replace("Donkey","######")
    f.seek(0)
    f.write(text)