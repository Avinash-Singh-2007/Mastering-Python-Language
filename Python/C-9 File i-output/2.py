def game(score):
    with open("./h-score.txt","r+") as f:
        hscore = f.read().strip()
        if hscore :
            if str(score) > hscore:
                f.seek(0)
                f.write(str(score))
        else:
            f.seek(0)
            f.write(str(score))        


def Showscore():
    with open("./h-score.txt","r+") as f:
        hscore = f.read().strip()
        if hscore:
            print(f"High score: {hscore}")
        else:
            print("No score available")

game(15)
Showscore()
game(20)
game(12)
Showscore()

        
