myfavfruitsnum = int(input("Enter number of your fave fruits : "))

AkofavFruits = []

for i in range(myfavfruitsnum):
    fruit = input("Enter fruits : ")
    AkofavFruits.append(fruit)

print(AkofavFruits)    

for x in AkofavFruits:
    if x == "Banana":
        break
    elif x == "Apple":
        print("HAPPY EATING")
    


    
