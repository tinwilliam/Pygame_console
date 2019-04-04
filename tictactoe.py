
import pygame
import random

x = "x" 
o = "o"

grid = [[1,2,2],
		[3,4,5],
		[6,7,8]]

def winX():
	if grid[0][0] == x & grid[0][1] == x & grid[0][2] == x :
		return("Player X win")
	elif grid[1][0] == x & grid[1][1] == x & grid[1][2] == x :
		return("Player X win")
	elif grid[2][0] == x & grid[2][1] == x & grid[2][2] == x :
		return("Player X win")
	elif grid[0][0] == x & grid[1][0] == x & grid[2][0] == x :
		return("Player X win")
	elif grid[0][1] == x & grid[1][1] == x & grid[2][1] == x :
		return("Player X win")
	elif grid[0][2] == x & grid[1][2] == x & grid[2][2] == x :
		return("Player X win")
	elif grid[0][0] == x & grid[1][1] == x & grid[2][2] == x :
		return("Player X win")
	elif grid[0][2] == x & grid[1][1] == x & grid[2][0] == x :
		return("Player X win")


def winO():
	if grid[0][0] == o & grid[0][1] == o & grid[0][2] == o :
		return("Player O win")
	elif grid[1][0] == o & grid[1][1] == o & grid[1][2] == o :
		return("Player O win")
	elif grid[2][0] == o & grid[2][1] == o & grid[2][2] == o :
		return("Player O win")
	elif grid[0][0] == o & grid[1][0] == o & grid[2][0] == o :
		return("Player O win")
	elif grid[0][1] == o & grid[1][1] == o & grid[2][1] == o :
		return("Player O win")
	elif grid[0][2] == o & grid[1][2] == o & grid[2][2] == o :
		return("Player O win")
	elif grid[0][0] == o & grid[1][1] == o & grid[2][2] == o :
		return("Player O win")
	elif grid[0][2] == o & grid[1][1] == o & grid[2][0] == o :
		return("Player O win")

	
