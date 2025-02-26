loop = True
while loop:
    n = int(input("guess the number, enter 0 to exit:" ))
    if n == 0:
        loop = False
        break
    elif n == 2128:
        print (f"{n} is correct... You Win!!!")
        loop = False
        break
    elif n in range (0,1501):
        print (f"{n} is too little, try a bigger number")
    elif n > 2700:
        print (f"{n} is too much, try a smaller number")
    elif n in range (1501,2001) :           
        print(f"{n} is close, try a bigger number!")
    elif n in range (2200,2701):
        print (f"{n} is close, try a bit smaller!")
    elif n in range (2001,2121):
        print ("you're very close, within 100")
    elif n in range(2140,2201):
        print ("You're very close, within 100")
    elif n in range (2120,2141):
        print("extremely close, within 10")
