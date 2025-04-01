
print("\nWelcome to the Rock Paper and Scissors Game\n")
print("It is You vs Computer")
print("Who ever wins 5 times first, wins the game\n")
i,j,k = 0,0,1
while (True):
    print("--------------------------------------------------------------")
    print("ROUND",k)
    print("\nEnter 1 for rock")
    print("Enter 2 for paper")
    print("Enter 3 for scissors")
    print("Incase you want to exit, Enter 4 to exit")
    if(k!=1):
        print("Enter 5 to reset the score")
    user_input = int(input("\nEnter your choice:"))
    if(user_input == 1):
        a= "rock"
    elif(user_input == 2):
        a= "paper"
    elif(user_input == 3):
        a= "scissors"
    elif(user_input == 4):
        print("Thanks for playing")
        exit()
    elif(user_input == 5):
        i=0
        j=0
        print("\nThe score has been reset")
        continue
    else:
        print("\nPlease enter a valid Input \n")
        continue
    print("\nYour choice is :", a)
    import random
    num = random.randint(1, 3)
    if(num == 1):
        b= "rock"
    elif(num == 2):
        b= "paper"
    elif(num == 3):
        b= "scissors"
    print("Computer's choice is :", b)
    if(user_input == num):
        print("Draw")
    elif((user_input==1 and num==2) or(user_input==2 and num==3) or (user_input==3 and num==1)):
        print("Computer wins")
        j+=1
    else:
        print("You win")
        i+=1
    print("\nThe score is you:",i ,"  Computer:",j,"\n\n")
    k+=1
    if(i==5):
        print("Congratulations :: You are the winner")
        break
    elif(j==5):
        print("Computer Win's")
        print("Well played")
        break
print("\nThanks for playing")
