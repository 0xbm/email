choice = input("Would you like send 1.EMAIL, 2.SMS or q for quit: ")

while True:
    choice = input("Would you like send 1.EMAIL, 2.SMS? or q for quit: ")
    if choice == "q":
        break
    elif choice == "1":
        exec(open("mailSender.py").read())
    elif choice == "2":
        exec(open("smsSender.py").read())
    else:
        print("Choose between 1 or 2 or q: ")
