class XorOgame:
    def __init__(self) -> None:
        self.game_board = [ [' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' '], ]

    def print_board(self):
        for row in self.game_board:
            for idx, value in enumerate(row):
                print(value, end=" ")
                if idx != 2:
                    print("", end="| ")
            print("\n---------")

    def check_for_win(self, character):
        win = False
        # horizontal
        for row in self.game_board:
            if row[0] == row[1] == row[2] == character:
                print(f"{row[0]} won 24")
                win = True
        # vertical
        for i in range(3):
            if self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] == character:
                print(f"{self.game_board[0][i]} won 28")
                win = True
        # diagonal
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == character:
            print(f"{self.game_board[0][0]} won 31")
            win = True
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == character:
            print(f"{self.game_board[0][0]} won 34")
            win = True
        return win

    def get_location_to_place(self, player_character: str):
        while True:
            x = int(input(f"Enter x coordinate to place({player_character}):"))
            y = int(input(f"Enter y coordinate to place({player_character}):"))
            if 0 <= x <= 2 and 0 <= y <= 2:
                if self.game_board[x][y] != ' ':
                    print("no free to place")
                    self.print_board()
                    continue
                self.game_board[x][y] = player_character
                break

    def play(self):
        while True:
            self.print_board()

            # x 
            self.get_location_to_place('x')
            self.print_board()
            if self.check_for_win('x'):
                break

            # o
            self.get_location_to_place('o')
            self.print_board()
            if self.check_for_win('o'):
                break

        print('game ended')

game = XorOgame()
game.play()