import random
'''
s = 1
g = -1
w = 0



'''

computer = random.choice([1,-1,0])
yourstr = input("enter ur choose :")
yourdic={"s":1 ,"g":-1 ,"w":0}
reversedic = {1:"snake" ,-1:"gun" ,0 :"water"}
you = yourdic[yourstr]

print(f"you chose:{reversedic[you]}\n computer chose: {reversedic[computer]}")

# we have 2 input variable you and computer

if(computer == you):
    print("so match is draw")
    
else:
    if(computer==-1 and you == 1):
        print("you win")
    elif(computer==-1 and you == 0):
        print("you lose")
    elif(computer==1 and you ==0):
            print("you lose")
    elif(computer==0 and you == 1):
            print("you win")
    elif(computer==-1 and you== 0):
                print("you win")
    elif(computer==0 and you==-1):
                print("you lose")
    elif(computer==1 and you==-1):
                print("you lose")
    else:
           print("something wrong")






