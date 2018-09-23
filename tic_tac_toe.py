import random


class TicTacToe:
    X = 'X'
    O = 'O'

    def __init__(self):
        self.cells = [' '] * 9

    def display_board(self):
        print(self.cells[6] + '|' + self.cells[7] + '|' + self.cells[8])
        print('-----')
        print(self.cells[3] + '|' + self.cells[4] + '|' + self.cells[5])
        print('-----')
        print(self.cells[0] + '|' + self.cells[1] + '|' + self.cells[2])
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
                print(f'Wrong character.')

    def place_marker(self, position, marker):
        self.cells[position] = marker

    def win_combinations(self, mark):
        return (
                (self.cells[0] == mark and self.cells[1] == mark and self.cells[2] == mark) or
                (self.cells[3] == mark and self.cells[4] == mark and self.cells[5] == mark) or
                (self.cells[6] == mark and self.cells[7] == mark and self.cells[8] == mark) or
                (self.cells[0] == mark and self.cells[3] == mark and self.cells[6] == mark) or
                (self.cells[1] == mark and self.cells[4] == mark and self.cells[7] == mark) or
                (self.cells[2] == mark and self.cells[5] == mark and self.cells[8] == mark) or
                (self.cells[0] == mark and self.cells[4] == mark and self.cells[8] == mark) or
                (self.cells[2] == mark and self.cells[4] == mark and self.cells[6] == mark)
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
                print('Wrong character.')


print('Welcome to Tic Tac Toe!')
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
            board.display_board()
            position = board.position_choice()
            marker = board.place_marker(position, Player1_marker)
            if board.win_combinations(Player1_marker):
                board.display_board()
                print('Player 1 is the winner!')
                game_on = False
            else:
                if board.full_board_check():
                    board.display_board()
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            board.display_board()
            position = board.position_choice()
            marker = board.place_marker(position, Player2_marker)
            if board.win_combinations(Player2_marker):
                board.display_board()
                print('Player 2 is the winner!')
                break
            else:
                if board.full_board_check():
                    board.display_board()
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 1'
    if not board.play_again():
        break
