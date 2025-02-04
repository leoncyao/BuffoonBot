import chess.pgn
import io
import json

def pgn_to_fens(pgn_text):
    # Read the PGN from the input text
    pgn = io.StringIO(pgn_text)
    games_fens = []
    
    while True:
        game = chess.pgn.read_game(pgn)
        if game is None:
            break
        
        # Initialize the board
        board = game.board()
        
        # List to store FENs for the current game
        fens = []
        
        # Add the initial position FEN
        fens.append(board.fen())
        
        # Iterate through all moves and add FENs
        for move in game.mainline_moves():
            board.push(move)
            fens.append(board.fen())
        
        games_fens.append(fens)
    
    return games_fens

def convert_pgn_file_to_json(pgn_path, json_path):
    try:
        with open(pgn_path, 'r') as pgn_file:
            pgn_text = pgn_file.read()
            
        # Convert PGN to FENs for each game
        games_fens = pgn_to_fens(pgn_text)
        
        if not games_fens:
            print(f"Error: No games found in {pgn_path}")
            return
            
        # Write FENs to JSON file
        with open(json_path, 'w') as json_file:
            json.dump({"games": [{"moves": fens} for fens in games_fens]}, json_file, indent=2)
            
        print(f"Successfully converted {pgn_path} to {json_path}")
            
    except Exception as e:
        print(f"Error processing files: {str(e)}")

if __name__ == "__main__":
    pgn_path = "data/pgn/lichess_neonleon.pgn"
    json_path = "data/fen/leon.json"
    convert_pgn_file_to_json(pgn_path, json_path)