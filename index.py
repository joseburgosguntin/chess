from termcolor import colored, cprint

class ChessBoard:
    def __init__(self):
        self.matrix = [
        ["R", "H", "B", "Q", "K", "B", "H", "R"], 
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "H", "B", "Q", "K", "B", "H", "R"],
        ]
        self.selected_location = []
        self.black_pieces_locations = {"r_1": [7,0], "h_1": [7,1], "b_1": [7,2], "q": [7,3], "k": [7,4], "b_1": [7,5], "h_1": [7,6], "r_1": [7,7],
        "p_1": [6,0], "p_2": [6,1], "p_3": [6,2], "p_4": [6,3], "p_5": [6,4], "p_6": [6,5], "p_7": [6,6], "p_8": [6,7]} 
        self.white_pieces_locations = {"r_1": [0,0], "h_1": [0,1], "b_1": [0,2], "q": [0,3], "k": [0,4], "b_1": [0,5], "h_1": [0,6], "r_1": [0,7],
        "p_1": [1,0], "p_2": [1,1], "p_3": [1,2], "p_4": [1,3], "p_5": [1,4], "p_6": [1,5], "p_7": [1,6], "p_8": [1,7]}
    
    def print_board(self):
        for black_piece in self.black_pieces_locations:
            self.matrix[self.black_pieces_locations[black_piece][0]][self.black_pieces_locations[black_piece][1]] = colored(self.matrix[self.black_pieces_locations[black_piece][0]][self.black_pieces_locations[black_piece][1]], 'green', attrs=[])
        print(colored("+ a b c d e f g h +", 'blue', attrs=[]))
        for i in range(8):
                print(colored(i + 1, 'blue', attrs=[]), self.matrix[i][0], self.matrix[i][1], self.matrix[i][2], self.matrix[i][3], self.matrix[i][4], self.matrix[i][5], self.matrix[i][6], self.matrix[i][7], colored(i + 1, 'blue', attrs=[]))
        print(colored("+ a b c d e f g h +", 'blue', attrs=[]))
        for black_piece in self.black_pieces_locations:
            self.matrix[self.black_pieces_locations[black_piece][0]][self.black_pieces_locations[black_piece][1]] = colored(self.matrix[self.black_pieces_locations[black_piece][0]][self.black_pieces_locations[black_piece][1]], 'white', attrs=[])
    
    def read_board_location(self, location):
        l0 = int(location[1]) - 1
        match location[0]:
            case "a":
                l1 = 0
            case "b":
                l1 = 1
            case "c":
                l1 = 2
            case "d":
                l1 = 3
            case "e":
                l1 = 4
            case "f":
                l1 = 5
            case "g":
                l1 = 6
            case "h":
                l1 = 7
        return [l0, l1]

    def select_location(self, location):
        l = self.read_board_location(location)
        if self.matrix[l[0]][l[1]] != " ":
            self.matrix[l[0]][l[1]] = colored(self.matrix[l[0]][l[1]], 'red', attrs=[])
            self.selected_location = l

    def validate_move(self, destination):
        s_v = self.matrix[self.selected_location[0]][self.selected_location[1]]
        s_l = self.selected_location
        d_l = self.read_board_location(destination)
        match s_v:
            case "K":
                if d_l == ([s_l[0] + 1, s_l[1] + 1] | [s_l[0] + 1, s_l[1]] | [s_l[0], s_l[1] + 1] |
                [s_l[0], s_l[1] - 1] | [s_l[0] - 1, s_l[1]] | [s_l[0], s_l[1] - 1]):
                    return True

    def move_piece(self, destination):
        s_v = self.matrix[self.selected_location[0]][self.selected_location[1]]
        d = self.read_board_location(destination)
        match s_v:
            case "K":
                if self.validate_move(destination):
                    (self.matrix[self.selected_location[0]][self.selected_location[1]],
                    self.matrix[d[0]][d[1]]) = (
                    self.matrix[d[0]][d[1]],
                    self.matrix[self.selected_location[0]][self.selected_location[1]])


chess = ChessBoard()
chess.select_location("d2")
chess.print_board()
print(chess.read_board_location("a8"), chess.read_board_location("b8"), chess.read_board_location("c8"))
