"""
Snake water gun game
"""

def game():
    import random
    i = 0
    gdic = {"s":"snake", "w":"water","g":"gun"}

    dic = {("snake", "water"): "snake", ("water", "gun"): "water", ("snake", "gun"): "gun"

        , ("water", "snake"): "snake", ("gun", "water"): "water", ("gun", "snake"): "gun"

        , ("snake", "snake"): "duce", ("water", "water"): "duce", ("gun", "gun"): "duce"
           }

    ucnt = 0
    ccnt = 0

    while( i < 10):
        computer = random.choice(list(gdic.values()))
        uin = input("Snake , Water or Gun ? (press 's' for snake, 'w' for water and 'g' for gun)\n")
        user = gdic.get(uin)
        if(user not in gdic.values()):
            print("Game Over...")
            return
        l = []
        l.append(computer)
        l.append(user)
        input_list = tuple(l)
       # print(input_list)
        res = dic.get(input_list)

        print("Round",i+1,":",end=" ")

        if( res == user):
            ucnt = ucnt + 1
            print("You won")
            #print("User :",ucnt)

        elif(res == computer):
            ccnt = ccnt + 1
            print("Computer won")
            #print("Computer :", ccnt)

        elif(res == "duce"):
            print("Round Tied")

        i = i+1

    print()
    print("Match result:" ,end =" ")
    if(ucnt > ccnt):
        print("Congratulations,You are the Winner!")
    elif(ucnt == ccnt):
        print("Match Tied")
    else:
        print("Oops... hard luck, Computer is the winner")

    print()
    print("Match Summary:")
    print("Computer's Score :",ccnt)
    print("Your Score :",ucnt)


game()