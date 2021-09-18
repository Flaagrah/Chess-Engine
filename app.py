from flask import Flask, request
import Utils.NextMoves
import chess
app = Flask(__name__)

@app.route("/nextmove", methods=["Get"])
def hello():
    fen = request.args.get("fen")
    depth = int(request.args.get("depth"))
    depth = depth*2+1
    fen = fen.replace('_','/')
    board = chess.Board()
    board.set_fen(fen)
    board = Utils.NextMoves.getNextMove(board, depth)
    return str(board)