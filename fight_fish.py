import os

import chess.engine
engine = chess.engine.SimpleEngine.popen_uci(os.environ["STOCKFISH_PATH"])

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
print(board.result())
engine.quit()