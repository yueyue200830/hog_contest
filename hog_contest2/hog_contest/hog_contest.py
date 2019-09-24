"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""

PLAYER_NAME = 'Love chips and coke' # Change this line!

def final_strategy(score, opponent_score):
    a = [
[4, 4, 5, 3, 0, 0, 1, 1, 0, 0, 0, 1, 0, 3, 1, 3, 2, 4, 2, 6, 4, 2, 0, 2, 0, 0, 0, 0, 5, 1, 2, 2, 10, 3, 10, 10, 7, 6, 4, 0, 0, 10, 4, 5, 2, 0, 0, 9, 9, 10, 0, 10, 10, 0, 10, 3, 10, 9, 2, 0, 0, 0, 1, 0, 0, 10, 0, 3, 10, 1, 1, 9, 8, 7, 0, 10, 10, 1, 10, 1, 0, 0, 0, 2, 2, 0, 0, 2, 10, 10, 2, 10, 1, 1, 1, 1, 1, 2, 2, 2, 1],
[4, 1, 2, 2, 7, 1, 1, 1, 3, 1, 1, 0, 10, 3, 0, 0, 1, 0, 2, 0, 3, 0, 10, 2, 0, 5, 1, 3, 5, 1, 2, 0, 1, 2, 0, 0, 3, 0, 4, 0, 0, 9, 0, 5, 0, 5, 0, 4, 3, 1, 1, 9, 0, 1, 1, 3, 0, 0, 0, 9, 3, 10, 0, 0, 2, 2, 10, 0, 0, 10, 1, 9, 1, 7, 10, 2, 10, 10, 0, 9, 0, 2, 1, 2, 2, 1, 0, 1, 4, 10, 0, 2, 10, 1, 0, 1, 1, 0, 2, 2, 1],
[0, 1, 0, 2, 4, 0, 1, 0, 3, 1, 0, 10, 10, 3, 0, 2, 1, 3, 2, 6, 3, 3, 5, 1, 0, 5, 0, 8, 4, 0, 2, 1, 0, 2, 0, 0, 3, 6, 3, 1, 3, 3, 0, 5, 0, 5, 0, 1, 0, 0, 1, 0, 1, 10, 1, 2, 0, 9, 9, 9, 3, 0, 0, 10, 1, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 0, 0, 0, 1, 0, 0, 0, 0, 1, 10, 0, 1, 4, 2, 10, 1, 1, 1, 1, 1, 2, 1],
[4, 0, 0, 0, 4, 0, 2, 0, 3, 1, 7, 1, 3, 2, 8, 2, 0, 0, 1, 0, 1, 0, 2, 1, 10, 2, 1, 0, 1, 0, 1, 0, 1, 2, 2, 8, 2, 0, 3, 7, 3, 3, 0, 4, 0, 5, 1, 9, 2, 10, 0, 9, 0, 10, 10, 2, 2, 8, 3, 0, 0, 10, 0, 10, 0, 0, 0, 0, 10, 0, 4, 8, 0, 0, 1, 4, 10, 10, 9, 9, 0, 2, 0, 0, 0, 0, 0, 1, 4, 10, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
[3, 5, 2, 1, 1, 0, 0, 0, 3, 1, 7, 0, 0, 2, 7, 2, 0, 8, 1, 6, 0, 9, 5, 0, 10, 2, 10, 2, 4, 6, 1, 10, 4, 2, 2, 10, 2, 5, 3, 7, 2, 0, 3, 2, 1, 5, 1, 3, 2, 2, 0, 1, 0, 3, 10, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 2, 0, 0, 0, 0, 2, 1, 3, 0, 1, 1, 1, 0, 0, 10, 1, 1, 1, 1, 1],
[3, 5, 1, 10, 3, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 2, 10, 0, 1, 0, 3, 0, 1, 0, 2, 1, 0, 2, 4, 5, 0, 0, 0, 0, 0, 7, 0, 5, 2, 0, 2, 2, 3, 0, 10, 4, 10, 3, 2, 1, 0, 1, 10, 3, 3, 0, 1, 0, 1, 8, 2, 10, 10, 3, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 2, 0, 0, 0, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 10, 5, 10, 1, 1, 1, 1],
[3, 1, 1, 1, 3, 10, 1, 0, 2, 0, 0, 10, 2, 2, 6, 1, 10, 2, 0, 10, 1, 2, 0, 10, 10, 0, 1, 2, 0, 5, 1, 0, 4, 1, 1, 2, 0, 10, 2, 0, 2, 2, 3, 0, 10, 4, 10, 1, 0, 10, 0, 0, 10, 3, 9, 0, 0, 8, 7, 1, 2, 2, 10, 3, 1, 0, 0, 1, 1, 0, 3, 8, 6, 6, 10, 1, 0, 1, 8, 0, 2, 1, 0, 9, 9, 6, 0, 10, 3, 0, 1, 0, 1, 3, 2, 4, 0, 10, 1, 1, 1],
[3, 1, 1, 10, 3, 2, 1, 1, 2, 3, 2, 0, 2, 1, 0, 0, 0, 2, 0, 5, 1, 0, 0, 10, 2, 1, 1, 0, 3, 5, 0, 10, 4, 0, 0, 0, 0, 4, 2, 6, 2, 2, 0, 1, 10, 4, 9, 0, 0, 0, 0, 8, 0, 2, 0, 0, 8, 4, 2, 1, 2, 1, 3, 9, 0, 0, 0, 0, 10, 0, 2, 2, 6, 10, 10, 10, 1, 1, 1, 3, 0, 0, 9, 9, 10, 10, 0, 10, 3, 0, 0, 0, 0, 3, 8, 4, 2, 1, 10, 1, 1],
[2, 4, 1, 1, 3, 2, 1, 0, 0, 3, 0, 10, 2, 1, 2, 10, 10, 2, 10, 1, 0, 9, 10, 0, 2, 0, 7, 1, 3, 2, 0, 3, 3, 0, 0, 1, 5, 4, 2, 10, 1, 1, 0, 0, 6, 4, 9, 1, 0, 1, 1, 0, 2, 2, 0, 1, 0, 4, 2, 10, 1, 0, 3, 2, 10, 10, 10, 0, 10, 8, 2, 1, 0, 10, 10, 3, 10, 1, 0, 0, 1, 10, 10, 9, 8, 10, 10, 10, 2, 2, 0, 5, 0, 3, 1, 4, 2, 10, 10, 10, 1],
[2, 4, 1, 0, 0, 0, 1, 9, 1, 0, 6, 1, 1, 0, 2, 0, 2, 1, 3, 0, 1, 2, 0, 3, 1, 1, 0, 0, 3, 1, 0, 2, 2, 1, 0, 1, 5, 4, 0, 5, 1, 1, 2, 10, 3, 0, 9, 0, 1, 0, 0, 0, 10, 2, 0, 10, 9, 0, 10, 10, 1, 10, 5, 2, 2, 4, 0, 10, 0, 8, 2, 0, 0, 2, 10, 9, 1, 10, 0, 0, 1, 0, 8, 8, 2, 0, 4, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
[2, 3, 0, 1, 2, 1, 0, 3, 0, 2, 2, 1, 1, 0, 1, 0, 2, 1, 2, 0, 0, 1, 10, 2, 0, 10, 6, 0, 2, 1, 3, 2, 1, 10, 10, 0, 10, 3, 0, 0, 1, 0, 10, 2, 3, 3, 2, 2, 0, 9, 1, 7, 0, 2, 1, 10, 6, 0, 0, 2, 1, 1, 2, 0, 1, 0, 0, 10, 10, 1, 1, 0, 0, 0, 0, 9, 10, 0, 7, 0, 0, 10, 0, 2, 0, 0, 4, 10, 2, 0, 2, 10, 10, 2, 1, 3, 1, 10, 2, 5, 1],
[2, 0, 2, 10, 1, 1, 3, 8, 1, 2, 1, 0, 1, 10, 1, 10, 2, 1, 2, 4, 0, 0, 3, 2, 0, 0, 10, 1, 0, 0, 0, 0, 0, 0, 10, 6, 0, 3, 0, 0, 0, 0, 0, 10, 0, 3, 0, 7, 10, 9, 0, 4, 1, 0, 10, 10, 10, 3, 0, 0, 1, 0, 2, 0, 0, 0, 1, 10, 10, 7, 1, 6, 10, 10, 4, 0, 10, 10, 0, 2, 0, 10, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 10, 0, 1, 3, 1, 0, 0, 4, 1],
[6, 0, 0, 3, 2, 1, 3, 2, 1, 1, 0, 0, 0, 10, 0, 10, 1, 0, 2, 4, 1, 7, 3, 2, 0, 2, 3, 10, 0, 0, 2, 10, 1, 0, 10, 6, 0, 0, 0, 0, 1, 10, 1, 2, 2, 0, 0, 0, 9, 1, 2, 0, 0, 0, 0, 10, 3, 3, 1, 0, 0, 0, 2, 0, 0, 10, 10, 0, 10, 7, 1, 0, 10, 0, 0, 0, 0, 10, 6, 0, 0, 3, 0, 0, 0, 1, 0, 9, 1, 8, 1, 10, 2, 10, 1, 1, 1, 1, 1, 4, 1],
[1, 2, 1, 0, 0, 1, 0, 2, 1, 1, 3, 10, 0, 6, 0, 4, 1, 0, 2, 3, 1, 1, 3, 2, 10, 10, 0, 1, 10, 0, 2, 2, 10, 3, 3, 10, 4, 2, 1, 9, 0, 10, 10, 2, 2, 2, 1, 0, 3, 8, 0, 3, 1, 0, 8, 2, 10, 1, 1, 0, 0, 10, 2, 0, 1, 3, 10, 10, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 9, 1, 0, 1, 4, 10, 0, 10, 3, 1, 0, 1, 4, 1],
[5, 2, 1, 9, 4, 1, 2, 1, 0, 1, 1, 9, 10, 3, 4, 3, 0, 10, 1, 3, 1, 0, 2, 1, 10, 2, 2, 0, 9, 10, 1, 1, 2, 10, 0, 0, 10, 2, 0, 4, 3, 3, 1, 1, 0, 0, 1, 0, 9, 0, 0, 3, 0, 0, 1, 0, 2, 10, 1, 0, 2, 10, 4, 1, 1, 3, 0, 10, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 3, 9, 1, 0, 1, 1, 2, 1, 0, 10, 1, 1, 1, 4, 1],
[1, 2, 1, 2, 1, 0, 2, 1, 0, 10, 0, 2, 9, 2, 4, 3, 0, 10, 1, 3, 0, 0, 0, 1, 1, 2, 5, 0, 2, 10, 2, 0, 2, 10, 10, 0, 0, 10, 0, 4, 0, 0, 0, 0, 0, 0, 8, 1, 3, 3, 1, 1, 0, 10, 1, 0, 0, 10, 10, 1, 2, 1, 1, 0, 10, 0, 0, 0, 10, 2, 1, 10, 10, 0, 0, 0, 0, 0, 0, 0, 2, 10, 6, 0, 0, 3, 0, 9, 1, 0, 3, 1, 0, 0, 6, 0, 10, 1, 1, 3, 1],
[0, 1, 0, 2, 0, 7, 2, 7, 1, 10, 4, 1, 4, 2, 3, 3, 10, 5, 0, 2, 1, 10, 2, 0, 1, 1, 2, 10, 0, 0, 1, 0, 0, 2, 2, 2, 3, 1, 5, 4, 3, 10, 0, 0, 1, 0, 7, 10, 0, 3, 1, 2, 10, 10, 10, 0, 0, 2, 10, 5, 0, 0, 0, 0, 10, 10, 10, 0, 0, 2, 0, 5, 10, 3, 3, 1, 1, 1, 0, 10, 0, 2, 10, 0, 0, 3, 0, 0, 1, 0, 3, 3, 1, 1, 6, 2, 0, 10, 1, 3, 1],
[4, 2, 0, 2, 1, 7, 1, 1, 1, 0, 2, 1, 2, 2, 3, 2, 9, 4, 0, 2, 0, 6, 10, 0, 0, 0, 0, 8, 0, 0, 1, 10, 10, 2, 2, 4, 0, 0, 10, 3, 2, 2, 10, 0, 0, 0, 7, 10, 2, 2, 1, 0, 10, 10, 7, 1, 0, 0, 2, 5, 2, 10, 0, 1, 3, 2, 2, 1, 0, 0, 0, 4, 0, 3, 3, 0, 0, 0, 0, 10, 4, 1, 0, 6, 3, 2, 2, 0, 10, 7, 0, 3, 0, 1, 6, 0, 0, 1, 10, 3, 1],
[0, 1, 0, 1, 0, 2, 0, 0, 1, 10, 2, 1, 2, 1, 3, 2, 2, 1, 8, 1, 5, 0, 1, 10, 0, 0, 0, 2, 0, 2, 0, 1, 10, 2, 2, 4, 3, 0, 10, 3, 0, 0, 10, 10, 0, 0, 1, 10, 2, 7, 0, 0, 2, 10, 6, 1, 1, 0, 2, 10, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 4, 2, 3, 8, 7, 9, 1, 0, 0, 1, 0, 0, 6, 10, 0, 2, 8, 5, 7, 2, 0, 0, 0, 0, 0, 0, 10, 2, 3, 1],
[4, 0, 0, 1, 2, 0, 1, 6, 1, 1, 1, 0, 0, 1, 2, 2, 0, 0, 7, 2, 1, 0, 1, 10, 10, 0, 0, 1, 10, 2, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 2, 2, 0, 10, 3, 1, 0, 0, 4, 2, 0, 10, 2, 2, 6, 1, 0, 0, 0, 10, 1, 10, 10, 10, 3, 0, 0, 0, 10, 0, 1, 0, 2, 2, 7, 7, 1, 1, 1, 1, 4, 0, 2, 6, 10, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[3, 1, 0, 1, 0, 2, 1, 1, 0, 9, 1, 9, 10, 0, 0, 2, 10, 0, 7, 2, 0, 5, 0, 10, 10, 10, 0, 0, 10, 2, 1, 0, 0, 0, 0, 0, 10, 10, 1, 3, 2, 2, 0, 10, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 6, 10, 1, 0, 0, 0, 0, 10, 10, 3, 3, 0, 0, 1, 0, 0, 1, 4, 2, 2, 2, 7, 9, 1, 1, 1, 1, 10, 10, 0, 10, 0, 1, 7, 0, 1, 2, 10, 10, 5, 5, 1, 1, 10, 2, 2, 1],
[3, 0, 1, 1, 0, 2, 1, 1, 0, 9, 0, 8, 1, 5, 2, 2, 8, 10, 0, 0, 4, 5, 0, 3, 3, 10, 0, 0, 10, 1, 0, 0, 0, 0, 1, 1, 2, 10, 4, 2, 2, 2, 10, 0, 10, 0, 6, 1, 0, 0, 0, 0, 0, 0, 6, 9, 9, 1, 0, 0, 0, 0, 2, 10, 0, 1, 10, 9, 1, 1, 1, 4, 2, 0, 0, 1, 9, 9, 4, 10, 0, 8, 2, 5, 2, 1, 1, 0, 4, 6, 1, 0, 10, 5, 5, 1, 1, 1, 0, 2, 1],
[3, 1, 1, 1, 1, 1, 0, 0, 1, 9, 3, 6, 1, 0, 1, 1, 1, 0, 8, 0, 1, 0, 0, 2, 0, 10, 3, 0, 7, 1, 0, 0, 0, 0, 0, 1, 0, 0, 10, 2, 1, 1, 10, 1, 2, 10, 3, 0, 3, 0, 1, 10, 1, 2, 5, 3, 8, 8, 1, 0, 0, 10, 2, 2, 10, 0, 0, 8, 9, 1, 0, 3, 0, 0, 2, 6, 0, 9, 4, 10, 0, 8, 2, 0, 0, 0, 1, 7, 4, 6, 1, 2, 0, 10, 7, 1, 0, 0, 1, 2, 1],
[3, 1, 1, 0, 1, 1, 0, 5, 10, 1, 1, 3, 2, 0, 1, 0, 1, 2, 2, 10, 0, 0, 10, 2, 0, 5, 3, 3, 5, 0, 4, 10, 10, 9, 0, 0, 0, 2, 0, 2, 1, 1, 0, 1, 2, 1, 10, 0, 1, 1, 1, 1, 10, 0, 0, 2, 3, 8, 3, 3, 1, 4, 2, 2, 2, 10, 1, 0, 9, 4, 0, 3, 1, 0, 0, 0, 8, 3, 4, 10, 3, 2, 0, 0, 0, 0, 1, 6, 4, 0, 1, 1, 0, 0, 4, 10, 0, 0, 1, 1, 1],
[2, 0, 0, 3, 1, 6, 1, 5, 1, 1, 0, 0, 0, 10, 1, 10, 0, 0, 2, 1, 4, 4, 10, 2, 2, 2, 3, 3, 4, 0, 1, 2, 10, 10, 3, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 10, 5, 10, 10, 0, 1, 0, 1, 10, 0, 2, 8, 3, 9, 3, 1, 4, 2, 2, 2, 10, 10, 8, 0, 10, 0, 3, 0, 0, 0, 6, 0, 8, 0, 10, 2, 0, 0, 0, 0, 10, 1, 6, 3, 5, 1, 1, 1, 1, 0, 10, 10, 1, 1, 1, 1],
[2, 1, 1, 3, 0, 1, 0, 1, 0, 8, 0, 10, 0, 1, 10, 10, 0, 3, 0, 1, 0, 4, 10, 2, 2, 2, 2, 3, 4, 0, 1, 2, 3, 10, 10, 2, 0, 0, 3, 0, 1, 10, 9, 0, 8, 10, 2, 3, 10, 5, 0, 0, 0, 1, 5, 2, 2, 8, 9, 3, 0, 0, 1, 0, 0, 10, 10, 10, 8, 0, 2, 3, 0, 0, 10, 5, 0, 0, 3, 10, 0, 0, 0, 0, 0, 10, 10, 6, 3, 3, 1, 1, 0, 0, 0, 2, 10, 1, 1, 1, 1],
[2, 1, 0, 6, 1, 5, 7, 1, 1, 1, 2, 2, 10, 0, 0, 0, 10, 1, 0, 0, 3, 4, 7, 1, 2, 2, 2, 2, 3, 10, 1, 2, 0, 2, 10, 10, 10, 0, 2, 0, 1, 0, 10, 1, 0, 0, 0, 10, 0, 5, 0, 0, 0, 0, 1, 2, 2, 2, 2, 10, 0, 0, 0, 0, 0, 1, 10, 2, 8, 0, 2, 0, 0, 1, 0, 5, 1, 2, 0, 3, 2, 0, 0, 0, 0, 0, 9, 6, 0, 0, 0, 0, 1, 4, 2, 0, 1, 10, 1, 1, 1],
[2, 0, 0, 3, 0, 0, 1, 0, 0, 0, 2, 2, 2, 10, 0, 0, 0, 1, 5, 0, 0, 3, 0, 0, 1, 1, 2, 2, 2, 10, 1, 2, 2, 2, 2, 10, 10, 0, 2, 0, 0, 0, 2, 10, 0, 0, 2, 10, 0, 5, 0, 10, 10, 0, 0, 0, 0, 0, 2, 2, 5, 9, 0, 0, 0, 0, 0, 0, 5, 3, 1, 0, 0, 10, 10, 0, 0, 0, 0, 0, 1, 7, 10, 10, 10, 0, 0, 0, 7, 0, 0, 10, 0, 1, 3, 2, 1, 3, 10, 1, 1],
[2, 1, 3, 2, 0, 0, 0, 0, 9, 8, 1, 0, 1, 0, 10, 10, 6, 1, 5, 10, 3, 3, 0, 0, 1, 1, 2, 2, 2, 10, 0, 1, 2, 2, 2, 2, 10, 10, 2, 0, 0, 10, 9, 0, 7, 0, 0, 2, 2, 5, 2, 2, 10, 0, 4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 10, 0, 2, 2, 1, 9, 10, 10, 10, 5, 1, 0, 0, 0, 0, 0, 10, 10, 10, 10, 1, 5, 2, 0, 0, 10, 8, 0, 3, 2, 10, 2, 2, 10, 1],
[1, 1, 2, 2, 1, 4, 2, 1, 2, 2, 1, 1, 0, 1, 2, 10, 6, 0, 1, 9, 2, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 1, 2, 0, 2, 0, 3, 4, 0, 10, 2, 2, 2, 2, 1, 1, 0, 0, 2, 4, 2, 2, 0, 10, 4, 1, 0, 0, 0, 0, 4, 2, 9, 9, 9, 1, 0, 10, 0, 0, 1, 2, 10, 10, 10, 4, 3, 0, 0, 0, 1, 10, 3, 10, 10, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
[1, 0, 2, 2, 0, 2, 3, 0, 9, 7, 1, 1, 10, 0, 1, 0, 2, 0, 0, 5, 2, 2, 6, 10, 0, 0, 1, 1, 1, 2, 3, 0, 2, 0, 0, 0, 3, 3, 0, 10, 2, 2, 1, 2, 10, 1, 4, 0, 0, 4, 2, 2, 6, 10, 3, 1, 0, 0, 0, 0, 1, 2, 0, 9, 9, 9, 0, 0, 7, 0, 0, 0, 0, 10, 10, 4, 0, 1, 0, 0, 0, 0, 10, 0, 9, 9, 1, 0, 2, 0, 2, 10, 2, 3, 1, 1, 1, 10, 2, 5, 1],
[0, 10, 0, 2, 0, 4, 0, 0, 9, 1, 1, 1, 1, 10, 0, 0, 0, 10, 10, 0, 2, 2, 10, 10, 9, 0, 0, 1, 1, 0, 2, 0, 1, 0, 0, 0, 3, 3, 0, 10, 1, 1, 1, 10, 10, 10, 1, 1, 0, 4, 2, 2, 10, 10, 10, 1, 0, 0, 0, 1, 1, 2, 9, 9, 8, 3, 1, 0, 0, 10, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 4, 2, 10, 1, 0, 10, 0, 2, 1, 10, 1, 0, 4, 1],
[1, 3, 2, 2, 1, 3, 1, 2, 2, 1, 0, 0, 0, 0, 10, 0, 5, 1, 4, 10, 1, 2, 5, 10, 8, 10, 0, 0, 1, 1, 1, 8, 0, 0, 0, 0, 3, 3, 0, 10, 1, 1, 1, 0, 6, 10, 3, 0, 1, 4, 2, 1, 2, 3, 3, 10, 1, 0, 1, 1, 0, 0, 8, 2, 8, 8, 1, 1, 0, 0, 8, 8, 0, 4, 4, 0, 0, 10, 0, 10, 0, 10, 2, 2, 2, 0, 0, 4, 1, 1, 1, 2, 1, 10, 2, 1, 1, 0, 1, 4, 1],
[0, 1, 1, 1, 1, 1, 1, 2, 1, 6, 0, 10, 10, 0, 1, 10, 5, 0, 0, 2, 1, 2, 1, 5, 7, 10, 10, 0, 0, 0, 1, 7, 0, 6, 0, 10, 2, 2, 10, 4, 1, 0, 0, 0, 2, 2, 10, 0, 0, 0, 1, 1, 2, 2, 3, 10, 10, 10, 10, 0, 3, 8, 2, 2, 2, 2, 8, 1, 1, 0, 8, 0, 9, 4, 4, 0, 0, 0, 1, 1, 0, 0, 10, 2, 0, 0, 8, 4, 1, 0, 1, 0, 0, 0, 10, 1, 0, 0, 1, 4, 1],
[0, 10, 1, 0, 0, 3, 5, 3, 1, 6, 3, 10, 10, 10, 0, 1, 5, 1, 3, 0, 1, 1, 1, 0, 3, 2, 10, 10, 0, 0, 1, 3, 0, 6, 10, 10, 2, 2, 10, 3, 1, 0, 0, 0, 0, 2, 0, 10, 10, 3, 1, 1, 2, 0, 2, 2, 10, 10, 10, 0, 3, 0, 2, 0, 2, 2, 1, 10, 1, 0, 1, 0, 0, 9, 3, 3, 1, 10, 1, 1, 1, 5, 0, 10, 0, 0, 7, 4, 1, 0, 1, 0, 0, 2, 2, 10, 1, 1, 1, 4, 1],
[0, 10, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 1, 2, 10, 0, 1, 0, 3, 4, 0, 0, 0, 1, 3, 0, 0, 10, 10, 0, 1, 2, 10, 6, 10, 10, 2, 2, 10, 1, 0, 0, 10, 1, 0, 0, 3, 0, 10, 3, 1, 0, 0, 2, 2, 2, 0, 10, 10, 10, 3, 1, 1, 0, 0, 0, 8, 1, 10, 0, 1, 1, 8, 4, 3, 1, 0, 0, 10, 9, 0, 4, 0, 0, 8, 0, 7, 3, 1, 10, 0, 0, 0, 0, 0, 0, 10, 1, 1, 3, 1],
[0, 2, 0, 1, 0, 0, 0, 2, 0, 0, 3, 9, 1, 1, 6, 10, 0, 0, 1, 4, 0, 10, 0, 0, 0, 1, 1, 10, 10, 10, 0, 2, 10, 6, 10, 10, 1, 0, 10, 0, 0, 10, 10, 10, 0, 0, 2, 0, 1, 3, 0, 0, 0, 1, 2, 2, 10, 0, 10, 9, 3, 1, 0, 0, 0, 0, 8, 10, 1, 10, 1, 0, 8, 0, 2, 2, 0, 0, 10, 9, 5, 2, 1, 0, 0, 0, 3, 10, 1, 10, 10, 10, 0, 1, 0, 1, 1, 10, 1, 3, 1],
[4, 0, 1, 3, 1, 2, 2, 2, 2, 1, 2, 1, 1, 0, 0, 0, 10, 10, 0, 0, 1, 10, 10, 4, 0, 1, 10, 3, 1, 9, 4, 2, 10, 5, 10, 2, 0, 0, 2, 0, 1, 4, 4, 10, 1, 1, 2, 10, 10, 2, 0, 10, 10, 0, 0, 0, 2, 10, 5, 9, 0, 0, 0, 0, 0, 0, 0, 10, 10, 1, 1, 0, 0, 3, 2, 0, 0, 0, 10, 9, 0, 0, 1, 1, 0, 7, 0, 3, 10, 10, 0, 0, 0, 1, 0, 1, 1, 3, 10, 3, 1],
[3, 2, 1, 0, 0, 2, 1, 0, 0, 1, 2, 2, 1, 10, 6, 10, 10, 4, 2, 10, 0, 1, 4, 10, 2, 0, 2, 3, 0, 0, 1, 2, 2, 2, 5, 0, 0, 0, 1, 1, 0, 0, 0, 0, 10, 1, 0, 1, 10, 2, 0, 0, 9, 0, 0, 0, 0, 0, 2, 9, 2, 6, 0, 0, 0, 0, 0, 0, 10, 9, 0, 0, 5, 3, 2, 0, 10, 10, 10, 9, 5, 9, 0, 1, 0, 7, 0, 0, 4, 0, 6, 1, 6, 1, 0, 10, 2, 2, 2, 3, 1],
[3, 2, 0, 2, 2, 2, 1, 2, 2, 1, 3, 2, 0, 0, 6, 2, 0, 3, 2, 3, 0, 0, 2, 4, 2, 0, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 0, 0, 1, 2, 3, 6, 0, 0, 4, 4, 0, 10, 2, 2, 3, 10, 4, 0, 0, 0, 0, 0, 0, 9, 2, 0, 7, 7, 6, 1, 7, 0, 0, 9, 6, 10, 5, 3, 0, 0, 9, 1, 9, 8, 0, 4, 0, 0, 7, 0, 2, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 1],
[0, 9, 5, 2, 1, 1, 1, 1, 1, 1, 1, 2, 10, 0, 6, 2, 10, 0, 0, 3, 5, 0, 1, 0, 2, 10, 1, 0, 10, 6, 1, 1, 1, 0, 2, 1, 10, 10, 0, 8, 2, 3, 0, 3, 4, 4, 0, 10, 2, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 6, 6, 6, 0, 1, 0, 0, 0, 5, 3, 2, 0, 0, 1, 9, 1, 4, 4, 3, 0, 10, 10, 0, 2, 0, 0, 1, 2, 10, 2, 1, 10, 10, 1, 10, 2, 2, 1],
[3, 1, 4, 2, 1, 1, 3, 1, 1, 1, 0, 0, 2, 10, 5, 1, 1, 10, 0, 0, 1, 10, 1, 0, 2, 0, 10, 2, 10, 8, 1, 0, 0, 0, 0, 10, 10, 10, 1, 0, 2, 3, 3, 3, 3, 4, 0, 10, 2, 0, 2, 2, 4, 0, 10, 1, 0, 10, 0, 0, 1, 6, 6, 6, 6, 6, 6, 0, 0, 0, 6, 5, 5, 0, 0, 0, 0, 0, 9, 4, 3, 0, 10, 9, 10, 0, 0, 2, 2, 10, 2, 0, 10, 0, 10, 10, 10, 1, 0, 2, 1],
[2, 0, 0, 1, 1, 1, 3, 1, 1, 0, 2, 8, 0, 3, 5, 1, 2, 2, 10, 9, 0, 0, 0, 4, 0, 1, 4, 10, 2, 7, 0, 0, 0, 0, 1, 0, 10, 10, 1, 1, 2, 2, 3, 3, 3, 3, 0, 3, 0, 0, 2, 1, 3, 10, 10, 10, 1, 1, 4, 0, 1, 5, 6, 6, 6, 6, 0, 1, 0, 0, 5, 2, 0, 0, 0, 1, 0, 9, 3, 7, 3, 8, 9, 10, 10, 1, 0, 1, 1, 10, 0, 0, 0, 10, 2, 10, 1, 0, 1, 2, 1],
[2, 1, 3, 1, 1, 0, 0, 0, 0, 3, 10, 1, 10, 3, 1, 0, 2, 2, 1, 8, 9, 10, 0, 0, 0, 10, 0, 2, 10, 5, 0, 0, 10, 4, 0, 1, 1, 10, 9, 0, 1, 2, 3, 3, 3, 3, 10, 2, 0, 0, 1, 1, 3, 10, 10, 10, 10, 0, 1, 0, 0, 0, 2, 5, 5, 6, 6, 1, 1, 0, 5, 0, 2, 1, 8, 1, 8, 8, 8, 0, 3, 0, 2, 8, 6, 0, 0, 1, 1, 10, 1, 10, 4, 2, 0, 2, 0, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 1, 10, 7, 10, 3, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 2, 0, 10, 3, 0, 0, 0, 1, 2, 5, 2, 10, 10, 3, 0, 0, 3, 0, 0, 6, 1, 2, 2, 2, 3, 3, 10, 2, 0, 0, 1, 1, 3, 10, 10, 10, 10, 10, 4, 0, 0, 5, 1, 5, 0, 5, 6, 10, 1, 1, 0, 0, 2, 2, 8, 10, 8, 8, 8, 7, 0, 8, 0, 0, 0, 10, 5, 1, 3, 9, 9, 0, 0, 0, 0, 10, 1, 1, 1, 1, 1],
[1, 1, 3, 1, 0, 0, 2, 0, 0, 0, 1, 0, 1, 2, 4, 10, 0, 10, 0, 2, 4, 10, 10, 10, 0, 0, 10, 1, 0, 0, 0, 2, 10, 10, 0, 0, 0, 1, 0, 0, 1, 2, 2, 2, 2, 3, 10, 2, 1, 10, 1, 0, 0, 3, 9, 10, 10, 10, 3, 1, 0, 4, 0, 0, 0, 0, 1, 10, 9, 1, 4, 10, 2, 0, 7, 10, 1, 1, 0, 0, 2, 0, 0, 0, 0, 5, 0, 9, 1, 9, 9, 1, 0, 0, 0, 0, 10, 1, 1, 1, 1],
[0, 0, 3, 0, 0, 4, 1, 7, 4, 2, 1, 0, 0, 0, 0, 0, 10, 2, 0, 0, 2, 2, 2, 0, 10, 0, 10, 0, 0, 0, 1, 2, 0, 3, 10, 1, 3, 1, 1, 8, 1, 1, 2, 2, 2, 2, 10, 0, 0, 10, 0, 0, 0, 2, 2, 3, 10, 2, 10, 1, 0, 4, 0, 0, 4, 0, 0, 0, 8, 7, 4, 1, 3, 0, 7, 10, 1, 1, 0, 0, 0, 0, 8, 0, 0, 5, 1, 10, 9, 9, 1, 0, 0, 1, 1, 0, 1, 10, 1, 1, 1],
[0, 7, 1, 1, 10, 3, 1, 1, 9, 2, 1, 0, 10, 0, 10, 0, 0, 1, 10, 8, 2, 2, 2, 1, 10, 10, 1, 1, 10, 4, 1, 0, 0, 2, 10, 10, 3, 0, 8, 0, 0, 0, 0, 2, 2, 2, 10, 0, 10, 9, 0, 10, 10, 2, 2, 2, 0, 0, 3, 7, 0, 4, 1, 1, 1, 0, 0, 0, 8, 7, 4, 1, 1, 0, 0, 10, 7, 0, 1, 0, 2, 7, 7, 8, 1, 4, 4, 9, 9, 9, 0, 0, 0, 1, 0, 0, 1, 3, 10, 1, 1],
[0, 7, 1, 0, 0, 1, 0, 6, 4, 2, 0, 10, 10, 10, 0, 10, 1, 1, 10, 1, 1, 2, 0, 2, 2, 10, 10, 0, 10, 6, 0, 10, 10, 0, 2, 10, 10, 0, 0, 6, 10, 1, 1, 1, 0, 2, 2, 1, 10, 9, 0, 10, 2, 2, 0, 0, 0, 0, 2, 7, 3, 4, 0, 10, 0, 4, 0, 0, 8, 7, 4, 0, 0, 1, 0, 10, 7, 7, 0, 0, 2, 0, 6, 8, 9, 4, 4, 9, 2, 8, 9, 8, 3, 0, 1, 1, 1, 2, 3, 10, 1],
[1, 6, 2, 1, 10, 1, 1, 6, 4, 1, 1, 5, 10, 0, 10, 2, 1, 1, 1, 0, 1, 1, 1, 0, 2, 2, 2, 0, 0, 4, 1, 1, 1, 2, 2, 2, 2, 2, 7, 5, 3, 0, 1, 0, 0, 0, 0, 1, 9, 9, 3, 2, 1, 0, 0, 0, 0, 0, 2, 6, 3, 3, 0, 4, 4, 4, 1, 0, 0, 7, 3, 0, 0, 0, 6, 0, 6, 7, 0, 0, 2, 0, 1, 0, 4, 4, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
[0, 6, 2, 0, 10, 3, 2, 0, 4, 1, 0, 1, 10, 1, 3, 5, 0, 0, 1, 7, 1, 1, 10, 1, 0, 2, 2, 10, 5, 0, 1, 0, 0, 2, 2, 2, 0, 10, 7, 7, 0, 10, 0, 0, 0, 0, 0, 10, 10, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 0, 3, 3, 0, 0, 1, 0, 0, 3, 10, 10, 0, 6, 0, 0, 6, 6, 0, 2, 7, 0, 0, 8, 0, 3, 8, 8, 1, 2, 10, 0, 1, 3, 10, 1, 10, 2, 5, 1],
[0, 2, 2, 1, 1, 0, 0, 1, 3, 0, 1, 1, 1, 0, 2, 0, 0, 0, 0, 3, 3, 1, 0, 10, 1, 0, 2, 10, 10, 0, 0, 0, 0, 0, 2, 2, 2, 10, 10, 5, 10, 10, 0, 0, 0, 0, 0, 10, 9, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 10, 3, 3, 3, 1, 1, 0, 2, 0, 10, 10, 10, 6, 1, 1, 0, 0, 1, 1, 6, 0, 0, 0, 3, 3, 8, 8, 8, 2, 0, 10, 0, 10, 10, 10, 1, 0, 4, 1],
[1, 6, 0, 1, 10, 2, 8, 5, 3, 1, 10, 0, 1, 10, 2, 10, 0, 10, 10, 0, 2, 0, 1, 1, 10, 1, 0, 2, 5, 8, 0, 0, 0, 0, 0, 1, 1, 0, 2, 3, 2, 0, 0, 0, 0, 0, 1, 0, 9, 2, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 10, 10, 3, 3, 3, 4, 1, 0, 0, 2, 10, 10, 10, 5, 10, 0, 0, 6, 5, 1, 6, 0, 10, 0, 3, 0, 7, 1, 7, 1, 0, 2, 10, 10, 10, 2, 0, 1, 4, 1],
[0, 6, 1, 0, 10, 2, 0, 1, 3, 1, 1, 0, 0, 10, 2, 5, 10, 10, 10, 6, 0, 0, 0, 1, 0, 10, 1, 4, 5, 5, 10, 10, 10, 0, 0, 0, 1, 0, 2, 3, 2, 10, 10, 10, 10, 10, 0, 0, 2, 0, 2, 0, 10, 10, 10, 1, 10, 10, 0, 0, 2, 2, 3, 3, 3, 3, 3, 10, 1, 0, 2, 2, 2, 10, 4, 1, 5, 1, 1, 5, 1, 5, 6, 6, 3, 0, 0, 0, 1, 7, 0, 0, 2, 0, 10, 2, 0, 0, 1, 4, 1],
[5, 5, 1, 1, 2, 2, 1, 1, 3, 0, 0, 0, 10, 0, 0, 1, 1, 10, 1, 2, 0, 0, 0, 0, 1, 0, 1, 1, 4, 2, 2, 2, 10, 0, 0, 0, 0, 0, 0, 2, 2, 2, 10, 10, 10, 10, 8, 0, 0, 2, 1, 10, 10, 10, 10, 10, 10, 10, 0, 0, 2, 2, 2, 2, 3, 3, 0, 10, 6, 0, 2, 1, 0, 0, 0, 10, 5, 5, 1, 4, 10, 5, 5, 6, 0, 3, 0, 0, 1, 7, 1, 7, 2, 2, 2, 10, 0, 1, 1, 4, 1],
[0, 1, 1, 1, 2, 1, 1, 0, 2, 0, 10, 10, 10, 10, 0, 0, 1, 1, 1, 2, 2, 10, 10, 1, 0, 0, 1, 1, 0, 2, 2, 2, 2, 10, 10, 0, 0, 0, 0, 2, 2, 0, 0, 10, 10, 10, 10, 1, 0, 0, 1, 10, 10, 10, 10, 10, 10, 10, 1, 0, 1, 2, 2, 2, 0, 0, 0, 10, 6, 5, 1, 0, 0, 1, 0, 10, 5, 5, 5, 4, 10, 5, 4, 5, 7, 2, 0, 0, 7, 0, 7, 0, 2, 0, 0, 0, 10, 1, 1, 3, 1],
[0, 5, 0, 0, 2, 1, 0, 10, 7, 1, 10, 4, 10, 2, 10, 0, 0, 0, 0, 2, 1, 3, 10, 10, 2, 10, 0, 0, 4, 2, 2, 1, 2, 10, 10, 10, 0, 10, 1, 2, 2, 10, 2, 2, 10, 10, 0, 10, 0, 0, 1, 4, 4, 10, 10, 10, 10, 10, 10, 0, 1, 2, 2, 0, 0, 0, 0, 4, 6, 5, 1, 0, 0, 0, 0, 0, 4, 5, 5, 4, 10, 4, 0, 0, 2, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 1, 10, 1, 3, 1],
[4, 4, 0, 5, 1, 1, 0, 4, 2, 0, 1, 3, 2, 2, 1, 10, 10, 0, 0, 1, 1, 2, 2, 10, 10, 10, 10, 0, 4, 0, 1, 1, 2, 10, 10, 10, 10, 10, 10, 2, 1, 1, 10, 2, 5, 10, 10, 10, 1, 7, 1, 1, 1, 2, 10, 10, 10, 10, 10, 1, 0, 0, 0, 0, 0, 0, 0, 1, 10, 4, 0, 0, 10, 10, 1, 1, 4, 4, 4, 4, 10, 10, 4, 1, 0, 0, 2, 0, 10, 6, 0, 10, 1, 0, 0, 0, 1, 3, 10, 3, 1],
[3, 0, 0, 5, 1, 0, 1, 4, 0, 1, 10, 3, 2, 1, 1, 3, 10, 10, 10, 1, 1, 2, 0, 0, 2, 10, 10, 0, 0, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 0, 1, 1, 0, 2, 0, 3, 3, 10, 0, 0, 0, 1, 0, 0, 5, 10, 10, 10, 10, 4, 10, 10, 0, 0, 0, 0, 0, 4, 10, 4, 1, 10, 10, 3, 10, 2, 4, 4, 4, 0, 10, 10, 10, 0, 0, 2, 2, 0, 6, 6, 10, 10, 1, 1, 0, 1, 1, 2, 2, 3, 1],
[3, 10, 10, 10, 10, 1, 10, 3, 1, 1, 10, 3, 2, 0, 0, 3, 1, 0, 4, 0, 10, 0, 1, 1, 1, 2, 2, 10, 3, 0, 1, 0, 1, 0, 10, 10, 10, 2, 5, 0, 10, 0, 0, 0, 0, 2, 0, 2, 7, 0, 10, 0, 1, 0, 0, 5, 2, 3, 10, 10, 10, 10, 10, 1, 1, 0, 0, 4, 5, 4, 10, 0, 10, 10, 3, 10, 4, 4, 4, 3, 2, 10, 3, 4, 0, 0, 0, 1, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[2, 4, 1, 0, 10, 0, 3, 3, 1, 0, 10, 2, 2, 10, 10, 3, 1, 10, 4, 0, 10, 10, 10, 10, 1, 2, 10, 10, 3, 0, 1, 0, 1, 10, 0, 2, 2, 2, 10, 0, 10, 10, 0, 0, 10, 10, 10, 10, 10, 0, 10, 0, 10, 0, 4, 5, 0, 2, 10, 10, 10, 10, 10, 10, 10, 1, 1, 3, 4, 4, 10, 10, 10, 2, 3, 2, 3, 3, 3, 3, 1, 3, 10, 1, 0, 1, 1, 10, 0, 5, 1, 10, 10, 10, 10, 10, 10, 10, 2, 2, 1],
[3, 1, 10, 2, 10, 0, 10, 3, 1, 0, 10, 2, 2, 10, 10, 3, 1, 0, 3, 0, 10, 0, 0, 10, 0, 1, 1, 2, 3, 0, 1, 10, 0, 1, 10, 0, 2, 2, 2, 10, 1, 10, 10, 0, 0, 2, 2, 2, 2, 1, 3, 10, 3, 10, 4, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 3, 4, 3, 1, 10, 2, 2, 0, 0, 0, 0, 0, 0, 10, 0, 0, 10, 1, 1, 10, 10, 10, 5, 10, 0, 10, 10, 10, 10, 10, 1, 0, 2, 1],
[1, 3, 10, 4, 10, 10, 10, 10, 1, 1, 1, 2, 1, 1, 0, 0, 0, 0, 3, 10, 10, 10, 1, 0, 0, 0, 1, 1, 3, 10, 10, 10, 0, 10, 1, 0, 0, 2, 2, 10, 10, 10, 10, 10, 0, 0, 2, 0, 10, 10, 10, 10, 3, 10, 0, 0, 0, 0, 2, 0, 10, 10, 10, 10, 10, 10, 10, 3, 4, 3, 10, 1, 2, 2, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 0, 1, 10, 1],
[2, 3, 10, 3, 10, 10, 2, 2, 10, 1, 1, 1, 0, 0, 10, 10, 10, 10, 3, 10, 10, 1, 10, 1, 0, 0, 0, 1, 0, 10, 10, 10, 10, 10, 0, 1, 0, 0, 4, 10, 10, 10, 10, 10, 3, 0, 0, 0, 0, 10, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 2, 3, 0, 10, 1, 1, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 0, 0, 1, 1, 1],
[10, 3, 3, 3, 10, 10, 2, 2, 10, 10, 1, 2, 10, 0, 10, 2, 10, 10, 3, 1, 4, 0, 0, 10, 10, 0, 1, 0, 2, 0, 10, 10, 10, 10, 10, 0, 1, 0, 0, 1, 10, 10, 10, 10, 3, 1, 0, 0, 0, 10, 2, 2, 2, 10, 3, 4, 1, 1, 2, 0, 10, 10, 10, 10, 10, 10, 10, 0, 3, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 10, 10, 10, 10, 10, 10, 10, 4, 10, 10, 10, 2, 2, 10, 0, 1, 1, 10, 1],
[1, 10, 1, 1, 10, 9, 2, 2, 10, 10, 1, 0, 10, 10, 0, 1, 9, 9, 2, 0, 1, 10, 0, 0, 10, 10, 10, 0, 10, 2, 2, 9, 2, 10, 2, 10, 0, 1, 0, 0, 1, 10, 4, 10, 10, 1, 0, 0, 0, 0, 1, 2, 2, 9, 0, 1, 10, 1, 0, 1, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 10, 0, 0, 0, 1, 0, 0, 0, 0, 10, 0, 10, 10, 10, 10, 10, 10, 10, 10, 1, 10, 2, 2, 0, 0, 10, 1, 1, 10, 1],
[1, 2, 10, 1, 3, 1, 2, 10, 2, 10, 10, 10, 0, 10, 10, 0, 2, 9, 2, 0, 1, 10, 10, 0, 0, 10, 9, 10, 2, 10, 2, 1, 1, 0, 10, 1, 10, 10, 1, 0, 9, 1, 4, 0, 10, 10, 1, 10, 1, 10, 1, 2, 2, 10, 10, 10, 10, 10, 0, 0, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 10, 10, 10, 0, 0, 10, 0, 0, 0, 0, 10, 10, 0, 10, 10, 10, 10, 4, 10, 10, 10, 0, 0, 0, 0, 0, 1, 10, 1, 10, 1],
[10, 2, 2, 10, 3, 9, 1, 10, 10, 2, 10, 10, 10, 2, 9, 10, 0, 1, 2, 10, 3, 3, 10, 10, 0, 10, 10, 10, 1, 2, 10, 0, 0, 1, 2, 10, 1, 10, 10, 0, 1, 1, 0, 2, 2, 10, 10, 10, 10, 2, 1, 1, 1, 2, 10, 10, 10, 10, 0, 0, 10, 9, 10, 10, 10, 10, 10, 0, 0, 0, 1, 10, 10, 10, 10, 10, 10, 0, 0, 1, 10, 10, 10, 0, 10, 10, 10, 0, 10, 10, 10, 10, 0, 0, 0, 0, 9, 10, 10, 10, 1],
[1, 10, 9, 2, 10, 9, 1, 1, 10, 10, 2, 10, 10, 2, 0, 1, 9, 1, 2, 2, 9, 2, 0, 9, 10, 0, 2, 9, 0, 1, 1, 10, 0, 0, 1, 0, 10, 0, 10, 10, 1, 0, 3, 2, 2, 1, 10, 10, 10, 10, 1, 1, 0, 1, 2, 9, 9, 9, 0, 10, 9, 5, 10, 10, 10, 10, 10, 0, 0, 0, 1, 0, 10, 10, 10, 10, 10, 10, 1, 10, 9, 10, 9, 10, 3, 9, 9, 9, 9, 0, 10, 10, 10, 0, 1, 1, 9, 9, 9, 10, 1],
[1, 2, 9, 9, 3, 9, 1, 1, 4, 10, 8, 0, 8, 6, 9, 0, 0, 0, 0, 1, 9, 8, 2, 2, 9, 9, 9, 9, 0, 0, 1, 0, 9, 9, 0, 0, 9, 9, 2, 10, 9, 9, 9, 0, 0, 0, 0, 9, 9, 0, 9, 0, 0, 0, 0, 0, 2, 2, 1, 10, 9, 0, 9, 10, 10, 10, 10, 0, 0, 0, 9, 8, 9, 9, 9, 9, 10, 10, 10, 10, 2, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 9, 1],
[9, 1, 2, 9, 2, 8, 9, 1, 1, 1, 2, 0, 0, 1, 8, 9, 0, 9, 9, 1, 8, 2, 2, 8, 8, 9, 0, 0, 0, 0, 1, 8, 9, 0, 0, 0, 2, 2, 2, 10, 9, 9, 3, 0, 0, 9, 0, 0, 0, 1, 9, 0, 9, 0, 0, 0, 0, 0, 10, 1, 9, 9, 4, 4, 4, 9, 9, 9, 0, 0, 9, 3, 9, 9, 9, 9, 9, 9, 9, 10, 1, 9, 9, 9, 9, 9, 0, 0, 0, 0, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1],
[9, 1, 8, 1, 2, 1, 9, 9, 1, 1, 2, 9, 8, 0, 8, 9, 9, 0, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 9, 10, 1, 4, 9, 9, 1, 9, 9, 8, 9, 9, 8, 8, 2, 1, 0, 8, 8, 0, 0, 0, 9, 9, 9, 8, 0, 0, 0, 9, 9, 10, 9, 8, 4, 3, 3, 3, 9, 9, 9, 0, 8, 3, 9, 9, 9, 3, 9, 9, 9, 10, 8, 9, 9, 9, 9, 8, 9, 0, 0, 0, 9, 0, 10, 9, 9, 9, 9, 8, 8, 8, 1],
[9, 9, 1, 1, 2, 8, 8, 9, 9, 1, 1, 9, 0, 8, 0, 0, 8, 8, 0, 0, 2, 1, 0, 1, 0, 4, 0, 9, 9, 10, 9, 0, 8, 8, 9, 8, 4, 8, 0, 0, 2, 2, 2, 0, 0, 1, 1, 3, 0, 0, 1, 9, 9, 8, 0, 0, 0, 9, 8, 9, 7, 7, 4, 3, 3, 3, 3, 9, 9, 9, 7, 3, 8, 8, 8, 2, 9, 9, 9, 9, 8, 8, 8, 9, 8, 8, 0, 0, 0, 0, 8, 9, 9, 9, 8, 8, 8, 0, 8, 8, 1],
[1, 9, 8, 1, 8, 1, 9, 8, 9, 9, 1, 8, 8, 7, 8, 0, 8, 8, 9, 9, 2, 1, 1, 0, 1, 9, 8, 9, 9, 9, 8, 8, 8, 8, 0, 8, 4, 0, 0, 1, 2, 2, 2, 8, 0, 8, 8, 3, 3, 9, 8, 8, 8, 8, 8, 1, 0, 0, 9, 0, 7, 4, 3, 3, 3, 3, 0, 8, 9, 9, 2, 2, 2, 7, 8, 0, 8, 8, 8, 9, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0, 8, 8, 8, 2, 9, 8, 0, 8, 8, 8, 1],
[8, 8, 7, 1, 7, 8, 3, 8, 3, 9, 8, 0, 1, 0, 3, 8, 0, 2, 0, 9, 8, 0, 0, 1, 0, 1, 8, 2, 8, 8, 7, 7, 0, 2, 7, 0, 0, 0, 0, 0, 1, 2, 0, 0, 8, 8, 8, 8, 8, 1, 7, 7, 8, 7, 8, 0, 0, 0, 0, 9, 7, 3, 3, 2, 3, 0, 8, 8, 8, 9, 2, 2, 2, 2, 8, 0, 8, 8, 8, 9, 8, 8, 8, 8, 0, 8, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 0, 8, 8, 8, 1],
[8, 8, 1, 8, 1, 7, 2, 2, 8, 2, 8, 8, 0, 7, 3, 7, 7, 3, 8, 8, 8, 8, 1, 8, 1, 0, 7, 2, 2, 8, 2, 3, 1, 7, 1, 0, 0, 0, 8, 9, 1, 2, 1, 8, 8, 7, 7, 8, 8, 8, 1, 6, 0, 7, 0, 8, 8, 0, 0, 0, 7, 3, 3, 2, 2, 2, 2, 8, 8, 9, 2, 2, 2, 0, 7, 0, 8, 8, 8, 8, 7, 8, 8, 8, 8, 8, 8, 0, 8, 0, 8, 8, 8, 2, 0, 0, 8, 7, 7, 7, 1],
[7, 8, 8, 8, 7, 8, 2, 2, 2, 8, 6, 8, 8, 7, 2, 7, 7, 1, 0, 8, 1, 8, 8, 0, 8, 0, 0, 2, 2, 2, 6, 6, 8, 1, 8, 1, 0, 7, 8, 8, 8, 0, 8, 8, 8, 7, 3, 0, 8, 8, 7, 3, 0, 1, 7, 7, 7, 7, 0, 8, 7, 3, 3, 0, 0, 0, 0, 2, 8, 8, 2, 2, 0, 0, 7, 0, 7, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 8, 0, 1, 1, 7, 2, 0, 0, 0, 7, 8, 7, 7, 1],
[8, 1, 7, 8, 7, 6, 7, 2, 2, 1, 7, 0, 7, 6, 2, 1, 0, 0, 7, 0, 1, 0, 7, 7, 0, 7, 0, 1, 2, 1, 2, 0, 1, 6, 0, 7, 7, 7, 0, 8, 1, 7, 1, 7, 7, 7, 0, 0, 0, 7, 7, 3, 7, 0, 0, 7, 7, 7, 1, 8, 6, 3, 0, 0, 0, 0, 0, 0, 1, 8, 1, 0, 0, 0, 7, 0, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 7, 0, 0, 0, 0, 0, 7, 7, 8, 7, 1],
[6, 7, 6, 7, 7, 6, 2, 6, 1, 7, 1, 6, 6, 6, 2, 0, 7, 7, 7, 7, 1, 7, 7, 7, 7, 7, 7, 0, 1, 0, 1, 6, 7, 0, 6, 7, 7, 7, 7, 7, 6, 1, 7, 1, 7, 6, 2, 0, 0, 2, 1, 5, 6, 7, 0, 0, 7, 7, 1, 7, 6, 0, 0, 0, 0, 0, 0, 0, 7, 7, 1, 0, 0, 0, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 1, 7, 7, 7, 7, 7, 1],
[2, 6, 6, 6, 6, 6, 6, 1, 1, 7, 6, 0, 0, 6, 6, 0, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 0, 0, 1, 1, 0, 0, 6, 0, 6, 6, 6, 7, 7, 6, 1, 1, 6, 0, 6, 2, 1, 0, 0, 6, 5, 0, 6, 7, 7, 7, 7, 7, 7, 6, 7, 7, 7, 1, 7, 7, 7, 7, 7, 1, 6, 6, 6, 7, 6, 7, 7, 7, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1],
[2, 6, 6, 6, 6, 6, 1, 1, 7, 1, 7, 6, 6, 5, 6, 7, 0, 6, 2, 0, 7, 0, 7, 6, 2, 2, 6, 0, 0, 7, 1, 6, 7, 6, 6, 0, 6, 2, 7, 0, 6, 0, 0, 0, 0, 6, 0, 6, 1, 0, 6, 5, 0, 6, 6, 6, 6, 7, 7, 7, 6, 2, 6, 7, 7, 0, 7, 7, 7, 6, 6, 0, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 1],
[2, 6, 6, 2, 6, 5, 1, 6, 6, 7, 5, 6, 5, 0, 1, 6, 6, 0, 0, 0, 6, 0, 6, 5, 0, 1, 5, 6, 6, 0, 6, 5, 6, 6, 1, 5, 2, 0, 0, 6, 5, 6, 0, 6, 0, 6, 6, 6, 6, 0, 5, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 6, 1],
[5, 6, 5, 6, 5, 5, 6, 6, 6, 7, 5, 5, 2, 5, 0, 5, 5, 6, 0, 0, 5, 6, 5, 5, 0, 1, 5, 6, 6, 7, 5, 5, 5, 0, 6, 0, 2, 5, 5, 0, 6, 6, 6, 6, 1, 0, 0, 6, 6, 0, 1, 4, 6, 5, 6, 6, 0, 0, 2, 6, 3, 6, 0, 0, 6, 6, 6, 0, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 6, 6, 1],
[5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 5, 5, 5, 5, 0, 5, 5, 5, 6, 6, 6, 5, 5, 5, 5, 0, 5, 6, 6, 6, 6, 0, 5, 0, 5, 6, 0, 1, 5, 6, 6, 6, 6, 6, 5, 5, 0, 0, 6, 6, 5, 1, 5, 5, 5, 6, 5, 0, 0, 0, 3, 1, 6, 6, 0, 6, 6, 6, 0, 6, 5, 5, 5, 5, 5, 6, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 5, 0, 0, 5, 5, 1],
[5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 4, 5, 5, 2, 6, 5, 5, 5, 1, 5, 5, 5, 0, 0, 6, 0, 0, 5, 6, 6, 5, 5, 0, 4, 5, 1, 5, 0, 5, 5, 4, 5, 5, 5, 6, 0, 0, 0, 0, 6, 4, 5, 0, 4, 0, 0, 5, 5, 0, 0, 2, 0, 5, 6, 5, 5, 5, 5, 5, 0, 5, 5, 5, 4, 5, 0, 5, 5, 5, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 1],
[1, 5, 4, 5, 5, 4, 5, 4, 5, 5, 5, 4, 0, 0, 0, 0, 4, 4, 0, 5, 4, 4, 0, 0, 5, 5, 5, 0, 5, 5, 4, 4, 4, 5, 5, 0, 0, 0, 5, 5, 4, 4, 4, 0, 0, 0, 5, 5, 0, 5, 4, 0, 1, 0, 4, 4, 5, 0, 0, 5, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 5, 4, 4, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 1],
[4, 1, 4, 4, 4, 4, 5, 4, 5, 6, 5, 4, 5, 5, 5, 5, 4, 0, 5, 5, 5, 0, 5, 5, 5, 5, 5, 4, 5, 0, 4, 4, 4, 4, 5, 4, 5, 4, 0, 5, 4, 4, 0, 4, 4, 5, 5, 4, 5, 5, 5, 5, 5, 4, 0, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 2, 2, 4, 0, 0, 0, 5, 4, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5, 1],
[5, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 5, 0, 0, 1, 4, 4, 4, 4, 4, 4, 5, 1, 4, 4, 0, 4, 4, 4, 4, 0, 5, 4, 4, 2, 0, 4, 0, 4, 4, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 1, 5, 5, 5, 5, 5, 5, 5, 1, 4, 2, 2, 0, 0, 0, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 0, 4, 4, 4, 4, 4, 5, 4, 1],
[5, 5, 4, 5, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0, 4, 1, 0, 0, 0, 0, 3, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 1],
[4, 4, 4, 4, 4, 4, 3, 3, 3, 4, 3, 4, 0, 4, 4, 4, 4, 3, 4, 4, 1, 3, 4, 4, 4, 4, 3, 4, 0, 4, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 4, 4, 4, 4, 3, 0, 4, 5, 1, 4, 4, 4, 4, 3, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1],
[4, 3, 4, 3, 3, 3, 3, 3, 4, 3, 4, 0, 4, 0, 3, 3, 3, 3, 3, 3, 4, 0, 0, 3, 3, 3, 3, 4, 4, 3, 4, 0, 0, 0, 3, 3, 4, 3, 3, 0, 4, 0, 0, 4, 0, 3, 3, 0, 4, 3, 4, 0, 0, 0, 4, 0, 3, 4, 4, 3, 4, 0, 4, 4, 4, 4, 0, 4, 4, 4, 3, 0, 4, 3, 3, 4, 4, 0, 4, 4, 4, 3, 4, 4, 3, 3, 3, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 1],
[3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 4, 3, 3, 3, 3, 3, 3, 4, 4, 0, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 3, 4, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 4, 3, 3, 3, 0, 4, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3, 0, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 2, 3, 0, 3, 0, 3, 3, 3, 3, 3, 0, 3, 0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 3, 2, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 1],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 0, 3, 2, 2, 3, 3, 2, 3, 0, 3, 3, 3, 3, 3, 3, 0, 2, 3, 3, 0, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 0, 3, 3, 3, 3, 3, 2, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 2, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 1],
[2, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 0, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 0, 2, 2, 2, 2, 0, 2, 2, 3, 2, 2, 0, 3, 2, 3, 3, 3, 3, 3, 0, 2, 2, 3, 2, 3, 2, 3, 2, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 2, 3, 2, 2, 2, 0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0, 1],
[2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 3, 3, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
[2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
    return a[score][opponent_score]

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    player_=[]
    opponent_=[]
    flag=False
    if(player_score==0| opponent_score==0):
        return False
    while(player_score!=0):
        player_.append(player_score%10)
        player_score=player_score//10
    while(opponent_score!=0):
        opponent_.append(opponent_score%10)
        opponent_score=opponent_score//10
    min_len=min(len(player_),len(opponent_))
    for i in range(0,min_len):
        if(player_[i]==opponent_[i]):
           flag=True
           return True

    return flag
def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    ones=score%10
    tens=score//10
    if(ones<=tens):
        return ones+1
    else:
        return tens+1

def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and does not trigger a
    non-beneficial swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    rolls = num_rolls
    incresement = free_bacon(opponent_score)
    new_score = incresement + score
    will_swap = is_swap(new_score, opponent_score)
    if will_swap and new_score < opponent_score:
        rolls = 0
    if incresement >= margin and not(will_swap and new_score > opponent_score):
        rolls = 0
    return rolls  # Replace this statement
