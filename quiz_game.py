import time
print("Welcome to Qizzers 2022")
qus = input("Do you want to play? yes/no:\n").lower()
score=0
wrong=0
if qus != "yes":
    quit()
time.sleep(1)
print("Okay,Lets Play")
times=int(input("How times You Want to Play:\n"))
for i in range(times):
    time.sleep(1)
    answer = input("What Does IDE Stands for?\n").lower()
    if answer == "integrated development environment":
        time.sleep(1)
        print("Wait Checking Your Answer")
        score+=1
        time.sleep(1)
        print("Correct!")
    else:
        wrong+=1
        print("Incorrect")
    time.sleep(1)
    answer = input("What Does UPS Stands for?\n").lower()
    if answer == "uninterruptible power supply":
        time.sleep(1)
        print("Wait Checking Your Answer")
        score += 1
        time.sleep(1)
        print("Correct!")
    else:
        wrong += 1
        print("Incorrect")
    time.sleep(1)
    answer = input("What Does RAM Stands for?\n").lower()
    if answer == "random access memory":
        time.sleep(1)
        print("Wait Checking Your Answer")
        score += 1
        time.sleep(1)
        print("Correct!")
    else:
        wrong += 1
        print("Incorrect")
    time.sleep(1)
    answer = input("What Does pep 8 Stands for?\n").lower()
    if answer == "python enhancement proposal":
        time.sleep(1)
        print("Wait Checking Your Answer")
        score += 1
        time.sleep(1)
        print("Correct!")
    else:
        wrong += 1
        print("Incorrect")
        time.sleep(1)
    print(f"You have Got {score} out of 4 Questions Correct")
    time.sleep(1)
    print(f"Your Accuracy is {score/4*100} %")
    time.sleep(1)
    print(f"You got {wrong} Questions Wrong")
