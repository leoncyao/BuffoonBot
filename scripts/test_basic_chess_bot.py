import json
import random
import chess
import chess.svg
import cairosvg

def load_move_history(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_random_move(history, current_position):
    if current_position in history:
        return random.choice(history[current_position])
    else:
        return None

def save_position_to_png(fen, file_name):
    board = chess.Board(fen)
    svg_data = chess.svg.board(board=board)
    cairosvg.svg2png(bytestring=svg_data, write_to=file_name)

def update_position(current_position, move):
    board = chess.Board(current_position)
    # Convert the move from UCI notation to a move object
    uci_move = chess.Move.from_uci(move)
    # Push the move to the board
    board.push(uci_move)
    return board.fen()

def play_chess_bot():
    # Load the move history from the JSON file
    move_history = load_move_history('data/model_data/leon_model.json')
    white_history_moves = move_history.get('white_history_moves', {})
    black_history_moves = move_history.get('black_history_moves', {})

    # Initial position in FEN notation
    current_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    while True:
        # Save the current position to a PNG file

        # Bot's move (as white)
        bot_move = get_random_move(white_history_moves, current_position)
        if bot_move:
            print(f"Bot's move: {bot_move}")
            current_position = bot_move
        else:
            # Generate a random legal move if no move is found in history
            board = chess.Board(current_position)
            legal_moves = list(board.legal_moves)
            if legal_moves:
                bot_move = random.choice(legal_moves).uci()
                print(f"Bot's random move: {bot_move}")
                current_position = update_position(current_position, bot_move)
            else:
                print("No legal moves available. Game over.")
                break
        # Update the current position with the bot's move

        save_position_to_png(current_position, 'current_position.png')

        # Player's move (as black)
        player_move = input("Enter your move (or 'exit' to quit): ")
        if player_move.lower() == 'exit':
            break

        # Update the current position with the player's move
        current_position = update_position(current_position, player_move)

if __name__ == "__main__":
    play_chess_bot()