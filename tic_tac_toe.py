import random


class TicTacToe:
    X = 'X'
    O = 'O'

    def __init__(self):
        self.cells = [' '] * 9

    def display_board(self):
        print("|".join(self.cells[6:9]))
        print('-----')
        print("|".join(self.cells[3:6]))
        print('-----')
        print("|".join(self.cells[0:3]))
        print()

    def player_input(self):
        marker = ''
        while not (marker == self.X or marker == self.O):
            marker = input(f'Player 1, please choose {self.X} or {self.O}: ').upper()
            if marker == self.X:
                return (self.X, self.O)
            elif marker == self.O:
                return (self.O, self.X)
            else:
                print(f'Wrong character!')

    def place_marker(self, position, marker):
        self.cells[position] = marker

    def win_combinations(self, mark):
        return (
                all(cell == mark for cell in self.cells[0:3]) or
                all(cell == mark for cell in self.cells[3:7]) or
                all(cell == mark for cell in self.cells[7:9]) or
                all(cell == mark for cell in self.cells[0:7:3]) or
                all(cell == mark for cell in self.cells[1:8:3]) or
                all(cell == mark for cell in self.cells[2:9:3]) or
                all(cell == mark for cell in self.cells[0:9:4]) or
                all(cell == mark for cell in self.cells[2:7:2])
        )

    @staticmethod
    def who_starts():
        return 'Player 1' if random.randint(0, 1) else 'Player 2'

    def cells_availability(self, position):
        return self.cells[position] == ' '

    def full_board_check(self):
        for i in range(0, 9):
            if self.cells_availability(i):
                return False
        return True

    @staticmethod
    def position_choice():
        position = 0


        while position not in range(1, 9) or not board.cells_availability(position):
            position = int(input('Choose a position [number from 1 to 9]: '))
            position -= 1
            return position
        else:
            print(f'That position is already taken')

    def possible_moves(self, moves_list):
        moves = []
        for i in moves_list:
            if self.position_choice(i):
                moves.append(i)
            else:
                print(f'That position is already taken. Choose another.')

    @staticmethod
    def play_again():
        while True:
            replay = input('Do you want to play again? [Y/N]: ').upper()
            if replay == 'Y':
                return replay
            elif replay == 'N':
                print('The end of the game')
                break
            else:
                print('Wrong character!')


    print('Welcome to Tic Tac Toe!')

def players_turn(player_name):
    markers = {"Player 1": Player1_marker,
                "Player 2": Player2_marker}
    marker = markers[player_name]
    board.display_board()
    position = board.position_choice()
    board.possible_moves(moves_list=[])
    board.place_marker(position, marker)

    if board.win_combinations(marker):
        board.display_board()
        print(f'{player_name} is the winner!')
        return False
    else:
        if board.full_board_check():
            board.display_board()
            print('Tie game!')
            return False
        return True



while True:
    board = TicTacToe()
    Player1_marker, Player2_marker = board.player_input()
    turn = board.who_starts()
    print(f'{turn} will start')

    begin = input('Are you ready to start? [Y/N]: ').upper()
    if begin == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            game_on = players_turn(turn)
            turn = 'Player 2'
        else:
            game_on = players_turn(turn)
            turn = 'Player 1'
    if not board.play_again():
        break
