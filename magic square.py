def main():
    instructions()
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    loop = "y"

    while loop == "y":
        
        row = int(input("what row? enter a number from 1 to 3: "))
        col = int(input("what column? enter a number from 1 to 3: "))

        row = row - 1
        col = col - 1

        number = int(input("okay, what's the number you want to put in that slot? "))
        
        if number in board[0] or number in board[1] or number in board[2]:
            print("you already input " + str(number))
        else:
            board[row][col] = number
            grid(board)
            loop = str(input("would you like to input another number? y/n: "))
        
    check(board)

def grid(g):
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def instructions():
    print("welcome to the lo shu magic square test. a lo shu magic square is\n"
          "a 3x3 box where the numbers in the box are all exactly 1-9, and\n"
          "each row, column, and diagonal all add up to the same number. i'm\n"
          "going to ask you what slot you'd like to fill, and you input a\n"
          "number into that slot. then, i'll check your answers.")

def check(board):
        
    if " " in board[0] or " " in board[1] or " " in board[2]:
        print("you left some spots blank. try again.")

    elif board[0][0] + board[0][1] + board[0][2] == board[1][0] + board[1][1] + board[1][2] == board[2][0] + board[2][1] + board[2][2] == board[0][0] + board[1][0] + board[2][0] == board[0][1] + board[1][1] + board[2][1] == board[0][2] + board[1][2] + board[2][2] == board[0][0] + board[1][1] + board[2][2] == board[0][2] + board[1][1] + board[2][0]: 
        print("this is a correct lo shu magic square! congratulations!")

    else:
        print("this is not a correct lo shu magic square.")

main()
               
