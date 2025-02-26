# prime = ["1","2","3","5","7","9","11","13","17","19"]


# print ("Is it a prime number:" ,end="")
# n = input()

# for x in prime:
#     if x == nombre: break
#     print (x)
# else:
#     print ("false")

# print ("Is it a prime number:" ,end="")
# n = input()
n = int(input("Is it a prime number:" ))
ip = True

for i in range(1, n):
    if n % i == 0 and i != 1 and i != n:
        print (f"{n} is not a prime")
        ip=False
        break
if ip == True:
    print (f"{n} is a prime")
else:
    if ip == False:
        print(f"{n} is not a prime number")


          
          

   