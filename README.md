# tictactoe

Run a game by running game.py

Specify human or random players in game.py's main function.

A human player will ask for row/column input from the command line. Rows and columns are entered separately and are indexed from zero.

The first player is chosen at random, regardless of initial input order.


## Designing Players

A player class initialized in game.py requires two functions that will be called by the game automatically during play.

- `set_token(self, token)` allows the game to send the player's token (eg, 'A' or 'B'). This is so the player knows which pieces on the board belong to them. No return necessary.
- `play(self, board)` provides the current board and expects a return or (row, column) for the next move. Players can call any of the board's methods, but should not be used to actually modify the board (this ability should be removed in future versions).

## Board Methods

The game board is initialized as a 3x3 python array of zeros. Its methods can be called from inside `player.play()` when designing a player.

- `reset_board()` returns the board to the initial state of zeros.
- `check_open_space(row, col)` returns false if `row` or `col` fall outside of the board's dimensions. Also returns false if the space has changed from the initial value of `0`.
- `check_win()` returns 0 if no player has won, otherwise returns that player's token. Note: tie endgames will return 0.
- `play(player, row, column)` sets the board at (row, col) to the value of `player` (intended to be the player's token).
- `get_board()` returns the 3x3 board array.
- `printable_board()` returns an f-string that formats the board for nicer printing. Add the returned string as an argument in `print()` as-is.
