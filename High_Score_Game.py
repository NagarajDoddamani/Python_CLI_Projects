for i in range(10):
    score = int(input("Enter Score : "))
    with open("high_Score.txt") as file:
        high_score = file.read()
        if(high_score == ""):
            high_score = 0
        else:
            high_score = int(high_score)

    if(score >= high_score):
        print("The High Score is Reccorded")
        with open("high_Score.txt","w") as file:
            file.write(str(score))
    else:
        print("This is Not the High Score")

with open("high_Score.txt") as file:
    high_score = file.read()
    print(f"The High score is {high_score}")