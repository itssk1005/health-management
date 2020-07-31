import datetime

def getdate():
    return datetime.datetime.now()
def take(k):

    while(True):
        if (k == 1):
            c = int(input("1 for food, 2 for exercise : "))

            if (c == 1):

                value = input("Enter data here\n")

                with open("saurabh-food.txt","a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")

                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d=="YES"):
                    continue
                else:
                    break



            if (c==2):

                value = input("Enter data here\n")

                with open("saurabh-ex.txt","a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")
                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d == "YES"):
                    continue
                else:
                    break

        elif (k == 2):
            c = int(input("1 for food, 2 for exercise : "))

            if (c == 1):

                value = input("Enter data here\n")

                with open("ranjay-food.txt","a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")

                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d == "YES"):
                    continue
                else:
                    break
            if (c == 2):

                value = input("Enter data here\n")

                with open("ranjay-ex.txt","a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")

                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d == "YES"):
                    continue
                else:
                    break

        elif (k == 3):

            c = int(input("1 for food, 2 for exercise : \n"))

            if (c == 1):

                value = input("Enter data here\n")

                with open("rushikesh-food.txt","a") as f:
                    f.write(str([str(getdate())])+": "+value+"\n")
                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d == "YES"):
                    continue
                else:
                    break

            if (c == 2):
                value = input("Enter data here\n")

                with open("rushikesh-ex.txt", "a") as f:
                    f.write(str([str(getdate())]) + ": " + value + "\n")
                print("Data successfully added")
                d = input("Do you want enter data again YES/NO")
                if (d == "YES"):
                    continue

        elif (k == 4):
                c = int(input("1 for food, 2 for exercise : "))

                if (c == 1):

                    value = input("Enter data here\n")

                    with open("yash-food.txt", "a") as f:
                        f.write(str([str(getdate())]) + ": " + value + "\n")

                        print("Data successfully added")
                        d = input("Do you want enter data again YES/NO")
                        if (d == "YES"):
                            continue
                        else:
                            break

                    if (c == 2):

                        value = input("Enter data here\n")

                        with open("yash-ex.txt", "a") as f:
                            f.write(str([str(getdate())]) + ": " + value + "\n")
                        print("Data successfully added")
                        d = input("Do you want enter data again YES/NO")
                        if (d == "YES"):
                            continue
                        else:
                            break


        else:
            print("Please enter the correct client number!!")
            break

def retrieve(k):

        if (k == 1):

            c = int(input("1 for food, 2 for exercise"))

            if (c == 1):

                with open("saurabh-food.txt") as f:

                    for i in f:
                        print(i,end="")

            elif (c == 2):

                with open("saurabh-ex.txt") as f:

                    for i in f:
                        print(i)

        elif (k == 2):

            c = int(input("1 for food, 2 for exercise"))

            if (c == 1):
                with open("ranjay-food.txt") as f:
                    for i in f:
                        print(i,end="")

            elif (c == 2):
                with open("ranjay-ex.txt") as f:
                    for i in f:
                        print(i,end="")

        elif (k == 3):

            c = int(input("1 for food, 2 for exercise"))

            if (c == 1):
                with open("rushikesh-food.txt") as f:
                    for i in f:
                        print(i,end="")

            elif (c == 2):
                with open("rushikesh-ex.txt") as f:
                    for i in f:
                        print(i,end="")
        elif (k == 4):

            c = int(input("1 for food, 2 for exercise"))

            if (c == 1):
                with open("yash-food.txt") as f:
                    for i in f:
                        print(i,end="")

            elif (c == 2):
                with open("yash-ex.txt") as f:
                    for i in f:
                        print(i,end="")



print("HEALTH MANAGEMENT SYSTEM : ")




data= int(input("1 for ADD, 2 for RETRIVE :  "))

if data == 1 :
    cli_name = int(input("1 for SAURABH,2 for RANJAY, 3 for RUSHIKESH,4 for YASH :  "))
    take(cli_name)
elif data == 2:
    cli_name = int(input("1 for SAURABH,2 for RANJAY, 3 for RUSHIKESH"))
    retrieve(cli_name)










