with open("Athletes.txt", "a", encoding="UTF-8") as file:
    while True:
        atl = input("Enter an athlete's name: ")

        if atl.lower() != "stop":
            file.write(atl + "\n")

        else:
            file2 = open("Athletes.txt", "r", encoding="UTF-8").read()
            print("\nThe athletes are \n" + file2)
            print("There are " + str(file2.count("\n")) + " athletes on the list")
            break
