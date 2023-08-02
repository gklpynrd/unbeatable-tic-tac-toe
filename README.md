# Unbeatable TicTacToe Ai
Implementation of code is little bit verbose. Will fix that

Program sometimes decides to mock with the user. Still won't loses though. Probably because program has only 3 utility states.

# Unbeatable Tic Tac Toe

![Tic Tac Toe](https://raw.githubusercontent.com/gklpynrd/Projects/main/AI/unbeatable_tictactoe(verbose)/tictactoe.png)

## Introduction

The "Unbeatable Tic Tac Toe" project is an implementation of the classic Tic Tac Toe game with an AI-based unbeatable opponent. The game is written in Python and aims to provide an interactive and challenging experience for players.

## Features

- Play against an unbeatable AI: The game incorporates a smart AI algorithm that ensures the AI will never lose, and if played optimally, the game will always end in a draw.
- Interactive Command-Line Interface: The game is played through the command-line interface (CLI), providing a user-friendly experience for players to interact with the game.

## How to Run

1. Clone the repository: `git clone https://github.com/gklpynrd/Projects.git`
2. Navigate to the "Unbeatable Tic Tac Toe" project directory: `cd Projects/AI/unbeatable_tictactoe(verbose)`
4. Run the game: `python tictactoe.py`

## Usage

- Upon starting the game, the player will make the first move.
- To place a move, enter the corresponding row and collumn (x,y) where the player wants to place their mark.
- The AI opponent will respond with its move shortly after the player's move.
- Continue playing until the game reaches a win, lose, or draw state.
- To exit the game, use the appropriate exit command or key combination (e.g., Ctrl + C).

## How the AI Works

The AI algorithm is based on the Minimax algorithm, a recursive search algorithm used for decision-making in two-player turn-based games like Tic Tac Toe. The AI explores all possible moves and their outcomes to find the best move to maximize its chances of winning or to minimize the player's chances of winning.
