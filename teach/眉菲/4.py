
satiety = 0

while True:
        x = input()
        if satiety == 3:
             print("I am not hungry")
        if x == "1" and satiety<3:
            print("I am eating")
            satiety += 1
        
            