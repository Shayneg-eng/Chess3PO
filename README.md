# Chess3PO

A chess bot you play against in the terminal. The [python-chess](https://python-chess.readthedocs.io/en/latest/) library handles the board and the rules. The part that picks moves is our own: the search, the evaluation, and the piece tables.

Excuse the weird code. I was in 10th grade and this was basically the first larger-scale project I worked on.

## How it picks a move

The bot looks three half-moves ahead: every move it could make, every reply you could make to that, and every move it could make after that. It scores each of those final positions, and for each of its candidate moves it assumes you'll find the reply that's best for you. Then it plays the move where your best reply does the least damage. It's a small hand-built version of minimax.

A position's score comes from two things:

- **Material.** Pawn 100, knight 300, bishop 320, rook 500, queen 900.
- **Piece-square tables.** Every piece type gets a bonus or penalty depending on which square it's on. Knights in the center are worth more than knights on the rim, pawns are pushed to advance, the king is pushed to stay safe, and so on.

After every move it prints both sides' scores, how long it thought for, and how many positions it searched. There's a longer write-up of the search in `explination of how the bot finds the best move.txt`.

## Playing

```bash
pip install chess
python "Chess BOT 1.1.2.py"
```

You're white. Type moves in standard notation (`e4`, `Nf3`, `O-O`). The bot prints your legal moves every turn, and you can type `undo` to take a move back or `stop` to quit.

## Versions

`Chess BOT.py` is the original. 1.1.1 reworked the game loop and evaluation, and 1.1.2 replaced a long chain of if-statements in the piece-square scoring with a lookup table. 1.1.2 is the one to run.
