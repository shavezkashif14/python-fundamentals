games = ["Minecraft", "Fortnite", "Roblox"]

while True:
    print("1. View games")
    print("2. Add a game")
    print("3. Remove a game")
    print("4. Search for a game")
    print("5. Exit")

    task = int(input("Choose an option: "))

    if task == 1:
        print("Your games:")
        for game in games:
            print(game)
        input("Press any key to continue: ")
    elif task == 2:
        games.append(input("Enter new game name: "))
        print("Game added!")
        input("Press any key to continue: ")
    elif task == 3:
        for game in games:
            print(game)
        games.remove(input("Enter the game you wish to delete: "))
        print("Game deleted!")
        input("Press any key to continue: ")
    elif task == 4:
        game = input("Enter game: ")
        if game in games:
            print(game, "is in your library!")   
        else:
            print(game, "in not in your library!")
        input("Press any key to continue: ") 
    elif task == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid selection!")
        input("Press any key to continue: ")