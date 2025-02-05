import json

from collections import defaultdict

def generate_model_data(file_path, output_file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    

    # ASIC CHEN What should I call this data
    # Initialize sets to store unique positions
    white_history_moves = defaultdict(set)
    black_history_moves = defaultdict(set)


    
    # Iterate over each game
    for game in data.get("games", []):
        moves = game.get("moves", [])
        
        # Extract positions for white (even indices) and black (odd indices)

        for i in range(len(moves)):
            if i % 2 == 0 and i < len(moves)-2:
                white_history_moves[moves[i]].add(moves[i+2])
            elif i % 2 == 1 and i < len(moves)-2:
                black_history_moves[moves[i]].add(moves[i+2])
    # Save the unique positions to a JSON file

    def serializer(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError(f"Type {type(obj)} not serializable")

    with open(output_file_path, 'w') as outfile:
        json.dump({
            "white_history_moves": white_history_moves,
            "black_history_moves": black_history_moves
        }, outfile, indent=4, default=serializer)

if __name__ == "__main__":
    generate_model_data('data/fen/leon.json', 'data/model_data/leon_mode.json')
    print("model_data have been exported to 'data/model_data/leon_model.json'")