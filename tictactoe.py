class TicTacToe:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        return ('  |  '.join(self.board[0:3]) + '\n' +
            '---|-----|----' + '\n' +
            '  |  '.join(self.board[3:6]) + '\n'
            '---|-----|----' + '\n' +
            '  |  '.join(self.board[6:9])
        )

    def empty_board(self):
        self.board = [' '] * 9

    def display_board(self):
        print('  |  '.join(self.board[0:3]))
        print('---|-----|----')
        print('  |  '.join(self.board[3:6]))
        print('---|-----|----')
        print('  |  '.join(self.board[6:9]))

    def player_input(self):
        player1 = input("Please pick a marker 'X' or 'O':")
        while player1.upper() not in ('X', 'O'):
            player1 = input("Please pick a marker 'X' or 'O' again:")
        return player1.upper()

    def place_marker(self, marker, position):
        if self.space_check(position):
            self.board[position] = marker

    def win_check(self, mark):
        first_row, second_row, third_row = self.board[:3], self.board[3:6], self.board[6:]
        first_column, second_column, third_column = self.board[::3], self.board[1::3], self.board[2::3]
        first_diagonal, second_diagonal = self.board[::4], self.board[2:7:2]
        return (first_row == [mark, mark, mark] or second_row == [mark, mark, mark] or
                third_row == [mark, mark, mark] or first_column == [mark, mark, mark] or
                second_column == [mark, mark, mark] or third_column == [mark, mark, mark] or
                first_diagonal == [mark, mark, mark] or second_diagonal == [mark, mark, mark])

    def space_check(self, position):
        return -1 < position < 9 and self.board[position] == ' '

    def full_board_check(self):
        return ' ' not in self.board

    def player_choice(self):
        selected_position = int(input('Please enter a number(1-9):'))
        while not self.space_check(selected_position - 1):
            selected_position = int(input('Please enter a number(1-9) again:'))
        return selected_position - 1

    def replay(self):
        play_again = input('Do you want to play again?(Y/N):')
        return play_again.upper() == 'Y'

print('Welcome to Tic Tac Toe!')
init_board = [' '] * 9
game = TicTacToe(init_board)
while True:
    player_mark = game.player_input()
    while not game.full_board_check():
        position = game.player_choice()
        game.place_marker(player_mark, position)
        print(game)
        if game.win_check(player_mark):
            print('Congratulations! You have won the game!')
            break
        player_mark = 'O' if player_mark == 'X' else 'X'
    if not game.replay():
        break
    game.empty_board()