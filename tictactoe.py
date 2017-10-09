userInput = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
gameOver = False
turnFlag = 0

while not gameOver:
    prompt = input("Enter your desired slot: ")

    while prompt not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        prompt = input("ERROR: Please enter a number between 1-9: ").strip()

    index = int(prompt) - 1

    while userInput[index] != '-':
        prompt = input("ERROR: Slot %d already contains an %s. Enter another: " % (index + 1, userInput[index]))
        index = int(prompt) - 1

    if turnFlag == 0:
        if userInput[index] != 'X':
            userInput[index] = 'O'
            turnFlag = 1
    else:
        if userInput[index] != 'O':
            userInput[index] = 'X'
            turnFlag = 0

    print("\n\n\n\n\n\n\n\n\n")
    print("", *userInput[0:3], "\n", *userInput[3:6], "\n", *userInput[6: 9], sep='  ')

    if (userInput[0] != '-' and userInput[0] == userInput[1] == userInput[2]) or (userInput[3] != '-' and userInput[3] == userInput[4] == userInput[5]) or (userInput[6] != '-' and userInput[6] == userInput[7] == userInput[8]):
        gameOver = True
        print("Game Over")
    elif (userInput[0] != '-' and userInput[0] == userInput[3] == userInput[6]) or (userInput[1] != '-' and userInput[1] == userInput[4] == userInput[7]) or (userInput[2] != '-' and userInput[2] == userInput[5] == userInput[8]):
        gameOver = True
        print("Game Over")
    elif (userInput[0] != '-' and userInput[0] == userInput[4] == userInput[8]) or (userInput[2] != '-' and userInput[2] == userInput[4] == userInput[6]):
        gameOver = True
        print("Game Over")
    elif '-' not in userInput:
        gameOver = True