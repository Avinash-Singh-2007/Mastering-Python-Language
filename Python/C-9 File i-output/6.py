with open("./poems.txt","r")as f:
    text = f.read()
    if text.lower().find("python") != -1:
        print("Talking about python")
    else:
        print("Not talking about python")    