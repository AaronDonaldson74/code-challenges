'''
Football Points
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far. A win receives 3 points, a draw 1 point and a loss 0 points.

Examples
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0
Notes
Inputs will be numbers greater than or equal to 0.
'''

def score(wins, draws, losses):
    return (3*wins)+(draws)+0

print(score(3, 4, 2))