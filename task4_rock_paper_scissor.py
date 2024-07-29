import random
options=("rock","paper","scissor")

while True:
    computer= random.choice(options)
    user=input("Enter Your Choice (rock,paper,scissor): ").lower()
     
    if (user not in options):
        print("\t  !! INVALID CHOICE !!\n Please choose (rock, paper, or scissor)")
        continue
    
    print(f"USER CHOICE= {user}")
    print(f"COMPUTER CHOICE= {computer}")
                

    if (computer == user):
        print("It's A Tie")
    elif(user=="paper"and computer== "rock"):
        print("You Won")
    elif(user=="scissor"and computer== "paper"):
        print("You Won")
    elif(user=="rock"and computer== "scissor"):
        print("You Won")
    else:
        print("You Loose,Better Luck Next Time ")
    
    playagain = input("Do you want to play again? (yes/no): ").lower()
    if playagain == "no":
        break

print("Thanks for playing!")
    
    
            
        
    
    
    
        
    
