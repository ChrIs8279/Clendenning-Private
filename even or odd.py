loop = True
while loop:
    n = int(input("type 0 to end/ Is it even or odd:" ))
    if n == 0:
        loop = False
        break
    else:
        if n % 2 == 0:
            print(f"{n} is an even number")
        else:
            print (f"{n} is an odd number")





