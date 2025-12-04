with open("./this.txt","r")as f:
    text = f.read()
    with open("./this-copy.txt","w")as g:
        g.write(text)
