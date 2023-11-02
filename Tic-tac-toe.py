import sys


def game_init():
    print("+" * 73)
    print("+ Weclome to the game!" + " " * 50 + "+")
    print("+ After Choosing your symbol" + " " * 44 + "+")
    print("+ Choose a number according to the table below to insert your symbol in +")
    print("+" * 73)
    print("  1  |  2  |  3  ")
    print("-----------------")
    print("  4  |  5  |  6  ")
    print("-----------------")
    print("  7  |  8  |  9  ")


def choose_symbol():
    global player1,player2
    ans = ''
    while ans != 'X' and ans != 'O':
        temp = input("For player 1: Choose 'X' or 'O' : ")
        ans = temp.upper()
        player1 = ans
        if player1 == "X":
            player2 = "Y"
        else:
            player2 = "X"
    return ans


def choose_num():
    chosen = None
    player = None
    global run
    if run % 2 == 0:
        player = 2
    else:
        player = 1
    while chosen not in range(1, 10):
        temp = input(f"[Player {player} turn] select number to insert symbol in: [1-9]")
        if temp.isdigit() and int(temp) in range(1, 10):
            chosen = int(temp)
        else:
            print("Invalid input! Try again: ")
    run += 1
    return chosen


def play_round(sym, num):
    xolist[num - 1] = sym
    print(f"  {xolist[0]}  |  {xolist[1]}  |  {xolist[2]}  ")
    print("-----------------")
    print(f"  {xolist[3]}  |  {xolist[4]}  |  {xolist[5]}  ")
    print("-----------------")
    print(f"  {xolist[6]}  |  {xolist[7]}  |  {xolist[8]}  ")
    if check_win(sym):
        sys.exit("Exiting Game...")
    else:
        new_sym = None
        if sym == "X":
            new_sym = "O"
        else:
            new_sym = "X"
        n = choose_num()
        play_round(new_sym, n)


def check_win(sym):
    # Checking Who won
    global player1,player2
    player_no = None
    if player1 == sym:
        player_no = "1"
    else:
        player_no = "2"
    #rows test:
    if (all(item == sym for item in xolist[0:3]) or all(item == sym for item in xolist[3:6])
    or all(item == sym for item in xolist[6:9])):
        print(f"Player {player_no} has won by row")
        return True
    #column test:
    if ((xolist[0] == xolist[3] == xolist[6]) or (xolist[1] == xolist[4] == xolist[7])
    or (xolist[2] == xolist[5] == xolist[8])):
        print(f"Player {player_no} has won by column")
        return True
    #diagonal test:
    if (xolist[0] == xolist[4] == xolist[8]) or (xolist[2] == xolist[4] == xolist[6]):
        print(f"Player {player_no} has won by diagonal")
        return True
    else:
        return False


# This is where you can call your functions
if __name__ == "__main__":
    xolist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    run = 1
    player1 = None
    player2 = None
    game_init()
    sym = choose_symbol()
    num = choose_num()
    play_round(sym, num)
