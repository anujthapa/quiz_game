print(f'Welcome to my quiz')
correct_count = 0
playing =  input("Do you want to paly quiz? ")
print(playing)
if playing != "yes":
    quit()

print("! lets Play :)")

answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print("Correct")
    correct_count = correct_count+ 1
else:
    print("Opps! Not correct")
answer = input("What does CPU stands for? ")
if answer == "Graphics processing unit":
    print("Correct")
    correct_count = correct_count+ 1
else:
    print("Opps! Not correct")
answer = input("What does RAM stands for? ")
if answer == "random excess memory":
    print("Correct")
    correct_count = correct_count+ 1
else:
    print("Opps! Not correct")
answer = input("What does PSU stands for? ")
if answer == "power supply":
    print("Correct")
    correct_count = correct_count+ 1
else:
    print("Opps! Not correct")

print(f"You have scroed {correct_count}")
