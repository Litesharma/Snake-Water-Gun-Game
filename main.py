import random
'''
snake Water Gun Game

Rules to play::::

Snake beats Water (as a snake would drink water).
Water beats Gun (as water would put out a gun's fire).
Gun beats Snake (as a gun can shoot a snake).

snake =  1
water =  0
gun   = -1  

'''

c_n=random.choice([1,-1,0])

a=input("You can choose between Snake, Water, or Gun : ")
user=a.lower()
dict={
    'snake':1,
    'water':0,
    'gun':-1,
}
c_dict={
    1:'snake',
    0:'water',
    -1:'gun',
}

u_n=None
if(user in dict):
    print(f'you choose {a.title()}\ncoumpter choose {c_dict[c_n].title()}')
    u_n=dict[user]
    if(u_n==c_n):
        print("Match draw!!")
    else:
        if(u_n==1 and c_n==0):
            print("You won!")
        elif(u_n==1 and c_n==-1):
            print("You lose!")
        elif(u_n==0 and c_n==1):
            print("You lose!")
        elif(u_n==0 and c_n==-1):
            print("You won!")
        elif(u_n==-1 and c_n==0):
            print("You lose!")
        elif(u_n==-1 and c_n==1):
            print("You won!")
        else:
            print("something went wrong please try again:(")
else:
    print("Please enter valid input from snake , water or gun")

