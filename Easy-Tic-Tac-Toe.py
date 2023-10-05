from IPython.display import clear_output         # Not necessary
import time

board = [[1,2,3],[4,5,6],[7,8,9]]
current_player_char = 'X'
next_player_char = 'O'
totalInputs = 9
winner = None

def checkHorizontal():
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
      return True
  else:
    return False

def checkVertical():
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i]:
      return True
  else:
    return False

def checkDiagonal():
  if board[0][0] == board[1][1] == board[2][2]:
    return True
  elif board[2][0] == board[1][1] == board[0][2]:
    return True
  else:
    return False

def checkBoard():
  if checkHorizontal() or checkVertical() or checkDiagonal():
    return True
  else:
    return False

def placeCharacterOnBoard(pos):
  position = board[(pos-1)//3][(pos-1)%3]
  if position == current_player_char or position == next_player_char:
    print("Invalid Position. Please enter a valid position again: ")
    return 0
  else:
    board[(pos-1)//3][(pos-1)%3] = current_player_char
    printCurrentBoard()
    return 1

def printCurrentBoard():
  print("-------------")
  for eachRow in board:
    print("|",end="")
    for eachCol in eachRow:
      print(f" {eachCol} ",end="|")
    print() #To move to the next row
    print("-------------")

def runGame():
  global current_player_char
  global next_player_char
  global winner
  welcome_msg = "Hi"
  print(welcome_msg)
  inputCount= 0
  while inputCount < totalInputs:
    printCurrentBoard()
    position = int(input(f"Player {(inputCount%2)+1}: "))
    validityofInput = placeCharacterOnBoard(position)
    inputCount+= validityofInput
    if inputCount>=5:
      if checkBoard():
        winner = "Player 1" if current_player_char == 'X' else "Player 2"
        clear_output()      # Not necessary
        break
    if validityofInput:
      current_player_char,next_player_char = next_player_char,current_player_char
    clear_output()      # Not necessary
  printCurrentBoard()

  if winner != None:
    print(f"Well done, {winner}. You have won the game.")
  else:
    print(f"The game ended in a draw")
runGame()
