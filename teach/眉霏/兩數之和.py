user_list = input("").split()
user = input("")

for i in user_list:
    
    for x in user_list:
        print(i,",",x)
        i = int(i)
        x = int(x)
        user = int(user)
        if i+x == user:
            print(i,"+",x,"=",user)
            exit()
