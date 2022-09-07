#HEalth Management System
# 3 clients-Harry, Sandy, Himanshu
#Total 6 files




def getdate():
    import datetime
    return datetime.datetime.now()

print("[---Welcome to Health Management System---]")
n1=int(input("[---Select 1 for Harry---]\n[---Select 2 for Sandy---]\n[---Select 3 for Himanshu---]\n"))
n2=int(input("[---Select 1 to retrieve---]\n[---Select 2 for input---]"))
n3=int(input("[---Select 1 for Diet---]\n[---select 2 for Workout---]"))

def HealthManagement(n1,n2):
    n4=int(input("[---Select 1 to Continue]---]\n[---Select 2 to exit---]"))
    if n4==1:
        if(n1==1 and n2==1):
            if n3==1:
                # Python code to illustrate read() mode character wise
                file = open("HarryDiet.txt", "r")
                print(file.readlines())
            elif n3==2:
                file = open("HarryWorkout.txt", "r")
                print(file.readlines())
                file.close()



        elif(n1==1 and n2==2):
            if n3 == 1:
                # Python code to illustrate read() mode character wise
                file = open("HarryDiet.txt", "a")
                file.write("{}".format(getdate()))
                file.write(input("Enter Diet"))
                file.close()
            elif n3 == 2:
                file = open("HarryDiet.txt", "a")
                file.write("{}".format(getdate()))
                file.write(input("Enter Workout"))
                file.close()

        elif(n1==2 and n2==1):
            if n3 == 1:
                # Python code to illustrate read() mode character wise
                file = open("SandyDiet.txt", "r")
                print(file.readlines())
                file.close()
            elif n3 == 2:
                file = open("SandyWorkout.txt", "r")
                print(file.readlines())
                file.close()



        elif(n1==2 and n2==2):
            if n3 == 1:
                # Python code to illustrate read() mode character wise
                file = open("SandyDiet.txt", "a")
                file.write("{}".format(getdate()))
                file.write(input("Enter Diet"))
                file.close()
            elif n3 == 2:
                file = open("SandyWorkout.txt", "a")
                file.write("{".format(getdate()))
                file.write(input("Enter Workout"))
                file.close()

        elif(n1==3 and n2==1):
            if n3 == 1:
                # Python code to illustrate read() mode character wise
                file = open("HarryDiet.txt", "r")
                print(file.readlines())
                file.close()
            elif n3 == 2:
                file = open("HarryWorkout.txt", "r")
                print(file.readlines())
                file.close()

        elif(n1==3 and n2==2):
            if n3 == 1:
                # Python code to illustrate read() mode character wise
                file = open("HimanshuDiet.txt", "a")
                file.write("{}".format(getdate()))
                file.write(input("Enter Diet"))
                file.close()
            elif n3 == 2:
                file = open("HimanshuWorkout.txt", "a")
                file.write("{}".format(getdate()))
                file.write(input("Enter Workout"))
                file.close()
        else:
            print("Please enter a valid input")

    elif n4==2:
        exit()
    else:
        print("Please enter a valid input")

HealthManagement(n1,n2)