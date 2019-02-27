import random
l=['r','p','s']
dict = {'r':'Rock','p':'Paper','s':'scissor'}

while True:

    u=input("enter your choice,press n to discontinue")
    if u=='n':
        print("game over")
        exit()
    #input from the computer
    c=random.choice(l)
    print("computer chooses",c)

    if u==c:
        print("tie")
    elif u=="p" and c=="r":
        print("user wins since",dict['p'],"WINS OVER",dict['r'])
    if u==c:
        print("tie")
    elif u=="r" and c=="s":
        print("user wins since",dict['r'],"WINS OVER",dict['s'])
    if u==c:
        print("tie")
    elif u=="s" and c=="p":
        print("user wins since",dict['s'],"WINS OVER",dict['p'])
    else:
        print("computer wins")