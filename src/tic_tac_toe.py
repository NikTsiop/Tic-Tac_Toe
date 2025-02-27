from dataclasses import dataclass, field
import random as rand
import math


@dataclass
class Player:
    name: str
    symbol_key: str
    symbol_value: int
    moves: list[tuple[int, int]] = field(default_factory=list)
    ai: bool = False


class TicTacToe:
    def __init__(self, players, n=3):
        self.players: list[Player] = players
        self.game_over = False
        self.board = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        self.print_board()

    def get_len(self):
        return len(self.board[0])

    def check_horizontal(self, current_state):
        for row in current_state:
            if row.count(row[0]) == len(row) and row[0] != 0:
                return row[0]
        return None

    def check_vertical(self, current_state):
        for col in range(len(current_state)):
            check = []

            for row in current_state:
                check.append(row[col])

            if check.count(check[0]) == len(check) and check[0] != 0:
                return check[0]
        return None

    def check_diagonal(self, current_state):
        diags1 = []

        for col, row in enumerate(reversed(range(len(current_state)))):
            diags1.append(current_state[row][col])

        diags2 = []
        for ix in range(len(current_state)):
            diags2.append(current_state[ix][ix])

        if (diags1.count(diags1[0]) == len(diags1) and diags1[0] != 0):
            return diags1[0]

        if (diags2.count(diags2[0]) == len(diags2) and diags2[0] != 0):
            return diags2[0]

        return None

    def check_winning(self, current_state, available_moves, eval=False):
        vertical = self.check_vertical(current_state)
        horizontal = self.check_horizontal(current_state)
        diagonal = self.check_diagonal(current_state)

        if (
            (not vertical and not horizontal and not diagonal) and
            available_moves == 0
        ):
            if not eval:
                print("Draw")
                self.game_over = True
            return 0
        else:
            if vertical or horizontal or diagonal:
                if not eval:
                    self.game_over = True
                if vertical:
                    return vertical
                elif horizontal:
                    return horizontal
                elif diagonal:
                    return diagonal
            return None

    def available_move(self, x, y):
        return self.board[x][y] == 0

    def available_move_count(self):
        available_moves = 0
        for row in self.board:
            available_moves += row.count(0)
        return available_moves

    def next_state(self, move, player: Player):
        x, y = move
        self.board[x][y] = player.symbol_value
        player.moves.append(move)

        self.print_board()

        result = self.check_winning(
            self.board,
            self.available_move_count()
        )

        if result != 0:
            print(f"{player.name} is the winner!")

    def print_board(self):
        length = len(self.board)

        for i in range(length):
            row = []
            for j in range(length):
                symbol_key = next((player.symbol_key for player in self.players if (i, j) in player.moves), None)
                row.append(symbol_key if symbol_key else " ")  # Append symbol or empty space

            print(" | ".join(row))  # Print the row with " | " separator

            if i != length - 1:  # Print horizontal separator except for the last row
                print("-" * (length * 4 - 1))

    def minmax(self, symbol_value, depth, maximizing_player=True):
        """
        Minimax algorithm for Tic-Tac-Toe AI.
        """
        result = self.check_winning(
            self.board,
            self.available_move_count(),
            eval=True
        )

        if result == -1:
            return -10 + depth
        elif result == 1:
            return 10 - depth
        elif result == 0:
            return result

        if maximizing_player:
            best_score = -math.inf
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 0:
                        self.board[i][j] = symbol_value
                        score = self.minmax(-1*symbol_value, depth + 1, False)
                        self.board[i][j] = 0
                        best_score = max(score, best_score)

            return best_score

        else:
            best_score = math.inf
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == 0:
                        self.board[i][j] = symbol_value
                        score = self.minmax(-1*symbol_value, depth + 1, True)
                        self.board[i][j] = 0
                        best_score = min(score, best_score)

            return best_score

    def best_move(self, symbol_value):
        best_score = -math.inf
        move = None
        for i in range(len(self.board[0])):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    self.board[i][j] = symbol_value
                    score = self.minmax(-symbol_value, 0, False)
                    self.board[i][j] = 0
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move


def print_title():
    print()
    print(
        """
     ████████╗██╗ ██████╗     ████████╗ █████╗  ██████╗     ████████╗ ██████╗ ███████╗
     ╚══██╔══╝██║██╔════╝     ╚══██╔══╝██╔══██╗██╔════╝     ╚══██╔══╝██╔═══██╗██╔════╝
        ██║   ██║██║             ██║   ███████║██║             ██║   ██║   ██║███████╗
        ██║   ██║██║             ██║   ██╔══██║██║             ██║   ██║   ██║██╔════╝
        ██║   ██║╚██████║        ██║   ██║  ██║╚██████║        ██║   ╚██████╔╝███████║
        ╚═╝   ╚═╝ ╚═════╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝ ╚══════╝
        """
    )
    print(100*"=")   


def create_player(player_num):

    default_symbols = ['X', 'O']
    players = []

    print(f"Player {player_num}:")
    print(20*"=")

    name = input(f"Player's Name (default -> Player {player_num}): ")
    symbol_key = input("Player's Symbol (default -> X or O): ")
    symbol_value = 2*(player_num - 1) + 1

    name = name if name != "" else f"Player {player_num}"
    symbol_key = (
        symbol_key if symbol_key != "" else default_symbols[player_num]
    )

    players.append(
        Player(name, symbol_key=symbol_key, symbol_value=symbol_value)
    )

    return players


def main():
    players = []

    print_title()
    print(20*" " + "(1) Player1 vs Player2")
    print(20*" " + "(2) Player1 vs Computer")

    mode = 0
    while mode == 0:
        try:
            mode = int(input("Choose mode (1 or 2):"))
        except Exception:
            print("Invalid Input")

    if mode == 1:
        for i in range(2):
            players.extend(create_player(i))
    else:
        players = create_player(0)
        players.append(Player("Terminator", "T", 1, ai=True))

    tic_tac_toe = TicTacToe(players, 3)

    index = rand.randint(0, 1)
    playing: Player = players[index]
    print(f"Starting with {playing.name}")
    move = None

    while not tic_tac_toe.game_over:
        row = -1
        col = -1
        available = False
        if not playing.ai:
            while (
                (row < 0 or row >= tic_tac_toe.get_len()) and
                (col < 0 or col >= tic_tac_toe.get_len()) and
                not available
            ):
                try:
                    row = int(input("Choose row: "))
                    col = int(input("Choose col: "))

                    available = tic_tac_toe.available_move(row, col)
                    if not available:
                        raise

                    move = (row, col)

                except Exception:
                    print("No valid move")
                    row = -1
                    col = -1
        else:
            move = tic_tac_toe.best_move(playing.symbol_value)

        tic_tac_toe.next_state(move, playing)

        if not tic_tac_toe.game_over:
            if index == 0:
                index = 1
            else:
                index = 0

            playing = players[index]
            print(f"{playing.name}'s turn!")


if __name__ == '__main__':
    main()
