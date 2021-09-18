# Chess-Engine

# Citations

Model and methodology derived from this paper:
O. David, N. Netanyahu, L. Wolf. "DeepChess: End-to-End Deep Neural Network for Automatic Learning in Chess". International Conference on Artificial Neural Networks (ICANN), 2016. https://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf

Dataset:
Computer Chess Rating Lists, CCRL-4040.[1239176].pgn, Computer Chess Rating Lists, http://www.computerchess.org.uk/ccrl/

# Instructions

1) Download code
2) Start Docker
3) Open cmd prompt and navigate to project directory
4) run this command: 'docker build -t chess:0.0.1 .'

# Accessing Cloud Service

Example:
https://chess-dlfdt73fwq-uc.a.run.app/nextmove?fen=2r2rk1_pp1n1pp1_1q3b1p_2pp2PP_2P5_Q4N2_PP1B1P2_1K1R3R%20b%20-%20-%200%2020&depth=0

The fen argument is based on the format given in the python chess document. https://python-chess.readthedocs.io/en/latest/
The '/' is replaced with _ in the url. This represents the current board position

The depth determines the depth of the decision tree. One move means one move by the current player and the opponent combined.
eg, A depth of 0 means that the algorithm considers all next positions two levels deep (ie, after white moves and then black moves).
A depth of 1 means that the algorithm considers all positions 4 levels deep (ie, after white moves, then black moves, then white moves, then black moves).
... and so on.

# Results
The model is able to distinguish a "white wins" positions from a "black wins" position with ~84.5% accuracy. However, there are inefficiencies in the algorithm that prevent the tree from going deeper without consuming too much time. This can be improved by hashing the feature extraction for positions that will be evaluated more than once and compressing the network.
