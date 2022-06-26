print("welcome to my computer quiz! ")
play=input("Do you want to take a shot! yes/no ")
if play.lower()!='yes':
    quit()
print("Okay lets play together! ")
score=0

qu= input("what does CPU stands for? ")
if qu.lower()=="central processing unit":
    print("Correct")
    score = score+1
else:
    print("Incorrect")

qu= input("What is stand for BD? ")
if qu.lower()=='bangladesh':
    print("Correct")
    score+=1
else:
    print("Incorrect")

qu= input("What is the full form of PM?  ")
if qu.lower()=="prime minister":
    print("Correct")
    score += 1
else:
    print("Incorrect")

qu= input("What is independent year of Bangladesh? ")
if qu.lower()=="1971":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Your got " + str(score)+ " correct question")
print("Your got " + str((score/4)*100)+ "correct question")


