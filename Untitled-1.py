#Hàm in bảng
def printBoard(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")

#Hàm nước đi của máy
def ai_Move():
    bestScore = -1000 
    bestMove = [] 
    for key in board.keys(): 
        if (board[key] == " "): 
            board[key] = ai_Player 
            score = minimax_DSA(board, 1, False) 
            board[key] = " "
            if (score > bestScore):
                bestScore = score
                bestMove = key
    print("Lượt đi của máy: " + str(bestMove))
    insert_Letter(ai_Player, bestMove)
    return

#Hàm nước đi của người
def human_Move():
    bestScore = 1000
    position = int(input("Lượt đi của bạn: "))
    while (position > 9):
        print("Lượt đi sai, thử lại")
        position = int(input("Lượt đi của bạn: "))
    insert_Letter(human_Player, position)
    return

#Minimax
def minimax_DSA(board, depth, isMaximizing): 
    if (mark_scoreplayerWin(ai_Player)): 
        return 10
    elif (mark_scoreplayerWin(human_Player)):
        return -10
    elif (check_Tie()):
        return 0
                                                                    
    if (isMaximizing):
        bestScore = -1000
        for key in board.keys():
            if (board[key] == " "):
                board[key] = ai_Player
                score = minimax_DSA(board, depth + 1, False)
                board[key] = " "
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for key in board.keys():
            if (board[key] == " "):
                board[key] = human_Player
                score = minimax_DSA(board, depth + 1, True)
                board[key] = " "
                if (score < bestScore):
                    bestScore = score
        return bestScore

#Hàm đánh dấu điểm (mark = kí hiệu đối tượng đang kiểm tra)
def mark_scoreplayerWin(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

#Hàm kiểm tra vị trí trống
def check_FreeSpace(thisPosition): 
    if board[thisPosition] == " ": 
        return True 
    else: 
        return False

#Hàm kiểm tra kết quả hoà
def check_Tie(): 
    for key in board.keys(): 
        if board[key] == " ": 
            return False 
    return True 

#Hàm kiểm tra kết quả thắng (Điều kiện có 3 vị trí thẳng - xéo - ngang giống nhau)
def check_Winner(): 
    if (board[1] == board[2] and board[1] == board[3] and board[1] != " "):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != " "): 
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != " "): 
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != " "):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != " "):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != " "):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != " "):
        return True
    elif (board[3] == board[5] and board[3] == board[7] and board[3] != " "):
        return True
    else:
        return False

def insert_Letter(letter, position):
    if check_FreeSpace(position) == True: 
        board[position] = letter 
        printBoard(board) 

        if check_Tie(): 
            print("Hoà!") 
            exit()

        
        if check_Winner(): 
            if letter == "X": 
                print("Người máy thắng. Chúc bạn may mắn lần sau !") 
                exit() 
            else: 
                print("Xin chúc mừng người chơi đã chiến thắng !") 
                exit() 
        return 

    else: 
        position = int(input("Vị trí đã được chọn. Vui lòng chọn vị trí khác: "))
        insert_Letter(letter, position)
    return

#Cài đặt giới thiệu
print("\n")
print("*************************************************************************")
print("*                                                                       *")
print("*                     - ĐỒ ÁN: TRÍ TUỆ NHÂN TẠO -                       *")
print("*                                                                       *")
print("*        XÂY DỰNG TRÒ CHƠI TIC TAC TOE AI BẰNG THUẬT TOÁN MINIMAX       *")
print("*                                                                       *")
print("*************************************************************************")
print("\n")

print("Theo dõi hướng dẫn sau:")
print("> Lượt đi đầu tiên 'X' : Người máy")
print("> Lượt đi tiếp theo 'O': Người chơi")
print("> Nhập vị trí muốn đi thuộc các ô:")
print("  1 | 2 | 3 ")
print("  --+---+-- ")
print("  4 | 5 | 6 ")
print("  --+---+-- ")
print("  7 | 8 | 9 ")
print("\n")
print("Tic Tac Toe bắt đầu. Chúc người chơi may mắn !")


board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " "} 
printBoard(board) 

#Kí hiệu người tham gia chơi
human_Player = "O"
ai_Player = "X"

while not check_Winner(): 
    ai_Move() 
    human_Move() 