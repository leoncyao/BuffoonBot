
import chess.pgn as chesspidgeons
import sys
import argparse

def get_moves(file: str) -> list[str]:
    ret = []
    try:
        with open(file, "r") as f:
            game = chesspidgeons.read_game(f)
            if game is None:
                print("Oh nosies game not found saduwu", file=sys.stderr)
                sys.exit(1)
         
            board = game.board()
            for move in game.mainline_moves():
                ret.append(board.fen())
                board.push(move)
    except OSError:
        print("I'm sowwee I couldn't open your file T_T", file=sys.stderr)
    
    return ret

def write_fen_to_file(file: str, boards: list[str]):
    try:
        with open(file, "w") as f:
            for boardstate in boards:
                f.write(boardstate + "\n")
    except OSError:
        print("I'm sowwee I couldn't open your file T_T", file=sys.stderr)
        sys.exit(1)


def get_arguments():
    ap = argparse.ArgumentParser(description="Hewo I'm here to convert PGN to FEN desu~~")
    ap.add_argument("--pgnfile", type=str, help="Path to senpai's chess game in PGN format")
    ap.add_argument("--fenfile", type=str, help="Where senpai wants me to write the FEN uwu")
    
    args = vars(ap.parse_args())
    
    if (args['pgnfile'] is None or args['fenfile'] is None):
        print("Um I'm sowwee but you're missing an argument uwu", file=sys.stderr)
        sys.exit(1)
    return (args['pgnfile'], args['fenfile'])

if __name__ == "__main__":
    pgnFile, fenFile = get_arguments()
    boards = get_moves(pgnFile)
    write_fen_to_file(fenFile, boards)