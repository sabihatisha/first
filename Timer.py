#import time
#for seconds in range(0,10,1):
#    print(seconds)
#    time.sleep(1)
#print("Happy New year!: Apna time agagaya")


rows= int(input("how many rows?: "))
colums= int(input("how many columss?: "))
symbol= input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="")
    print()

