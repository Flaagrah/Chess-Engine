from flask import Flask, request
import Utils.NextMoves
import chess
app = Flask(__name__)

@app.route("/nextmove", methods=["Get"])
def hello():
    fen = request.args.get("fen")
    fen = fen.replace('_','/')
    board = chess.Board()
    board.set_fen(fen)
    board = Utils.NextMoves.getNextMove(board, 2)
    return str(board)