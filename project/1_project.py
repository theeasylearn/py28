while True:
    print("Press 1 for Product management")
    print("Press 2 for Bill management")
    print("Press 3 to Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print("provide options for product management")
    elif choice == 2:
        print("provide options for Bill management")
    elif choice == 3:
        print("Thank your for your software application")
        break #stop loop
    else:
        print("invalid choice")
