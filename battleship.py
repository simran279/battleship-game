import copy, random

def print_board(s,board):

	player = "Computer"
	if s == "u":
		player = "User"
	
	print("The " + player + "'s board look like this: \n")
	for i in range(10):
		#print the board values, and cell dividers
		for j in range(10):
			#if board[i][j] == -1:
			#	print (' ')	
			if s == "u":
				if(board[i][j] == -1):
					print (board[i][j], end='   ')
				else:
					print (board[i][j], end='    ')
			elif s == "c":
				if board[i][j] == "*" or board[i][j] == "$":
					print (board[i][j], end='   ')
				else:
					print (0, end='   ')
		print("\n")
def user_place_ships(board,ships):

	for ship in ships.keys():

		#get coordinates from user and vlidate the postion
		valid = False
		while(not valid):

			print_board("u",board)
			print ("Placing a/an " + ship)
			x,y = get_coor()
			ori = v_or_h()
			valid = validate(board,ships[ship],x,y,ori)
			if not valid:
				print ("Cannot place a ship there.\nPlease take a look at the board and try again.")
				input("Hit ENTER to continue")

		#place the ship
		board = place_ship(board,ships[ship],ship[0],ori,x,y)
		print_board("u",board)
		
	input("Done placing user ships. Hit ENTER to continue")
	return board
def computer_place_ships(board,ships):

	for ship in ships.keys():
	
		#genreate random coordinates and vlidate the postion
		valid = False
		while(not valid):

			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			o = random.randint(0,1)
			if o == 0: 
				ori = "v"
			else:
				ori = "h"
			valid = validate(board,ships[ship],x,y,ori)

		#place the ship
		print ("Computer placing a/an " + ship)
		board = place_ship(board,ships[ship],ship[0],ori,x,y)
	#print_board("c",board)
	
	
	return board
def place_ship(board,ship,s,ori,x,y):

	#place ship based on orientation
	if ori == "v":
		for i in range(ship):
			board[x+i][y] = s
	elif ori == "h":
		for i in range(ship):
			board[x][y+i] = s

	return board
	
def validate(board,ship,x,y,ori):

	#validate the ship can be placed at given coordinates
	if ori == "v" and x+ship > 10:
		return False
	elif ori == "h" and y+ship > 10:
		return False
	else:
		if ori == "v":
			for i in range(ship):
				if board[x+i][y] != -1:
					return False
		elif ori == "h":
			for i in range(ship):
				if board[x][y+i] != -1:
					return False
		
	return True

def v_or_h():

	#get ship orientation from user
	while(True):
		user_input = input("vertical or horizontal (v,h) ? ")
		if user_input == "v" or user_input == "h":
			return user_input
		else:
			print ("Invalid input. Please only enter v or h")

def get_coor():
	
	while (True):
		user_input = input("Please enter coordinates (row,col) ? ")
		try:
			#see that user entered 2 values seprated by comma
			coor = user_input.split(",")
			if len(coor) != 2:
				raise Exception("Invalid entry, too few/many coordinates.");

			#check that 2 values are integers
			coor[0] = int(coor[0])-1
			coor[1] = int(coor[1])-1

			#check that values of integers are between 1 and 10 for both coordinates
			if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
				raise Exception("Invalid entry. Please use values between 1 to 10 only.")

			#if everything is ok, return coordinates
			return coor
		
		except ValueError:
			print ("Invalid entry. Please enter only numeric values for coordinates")
		except Exception as e:
			print (e)

def make_move(board,x,y):
	
	#make a move on the board and return the result, hit, miss or try again for repeat hit
	if board[x][y] == -1:
		return "miss"
	elif board[x][y] == '*' or board[x][y] == '$':
		return "try again"
	else:
		return "hit"

def user_move(board):
	
	#get coordinates from the user and try to make move
	#if move is a hit, check ship sunk and win condition
	while(True):
		x,y = get_coor()
		res = make_move(board,x,y)
		if res == "hit":
			print ("Hit at " + str(x+1) + "," + str(y+1))
			check_sink(board,x,y)
			board[x][y] = '$'
			if check_win(board):
				return "WIN"
		elif res == "miss":
			print ("Sorry, " + str(x+1) + "," + str(y+1) + " is a miss.")
			board[x][y] = "*"
		elif res == "try again":
			print ("Sorry, that coordinate was already hit. Please try again")	

		if res != "try again":
			return board

def left(board,a,b):
	x=0
	y=0
	if (b-1 >= 0):
	
		if (board[a][b-1] != -1 and board[a][b-1] != '*' and board[a][b-1] != '$'):
			#print("if loop left")
				x=a
				y=b-1
		elif(board[a][b-1] == '*' or board[a][b-1] == -1):
			#print("elif loop left")
				x,y = right(board,a,b)
		else:
			#print("else loop left")
				if(b-2 >=0):
					if (board[a][b-2] != -1 and board[a][b-2] != '*' and board[a][b-2] != '$'):
			#	print("else if loop left")
						x=a
						y=b-2
					elif(board[a][b-2] == -1 or board[a][b-2] == '*'):
			#	print("else elif loop left")
						x,y = right(board,a,b)
					else:
			#	print("else else loop left")
						if(board[a][b-2] == '$'):
							x,y = left(board,a,b-2)
	else:
		x,y = right(board,a,b)
	return(x,y)
def right(board,a,b):
	x=0
	y=0
	if (b+1 <= 10):
		if (board[a][b+1] != -1 and board[a][b+1] != '*' and board[a][b+1] != '$'):
			#print("if loop right")
				x=a
				y=b+1
			#print(x,y)
		elif(board[a][b+1] == '*' or board[a][b+1] == -1 ):
			#print("elif loop right")
				x,y = up(board,a,b)
		else:
		#	print("else loop right")
				if (b+2 <= 10):
					if (board[a][b+2] != -1 and board[a][b+2] != '*' and board[a][b+2] != '$'):
			#	print("else if loop right")
						x=a
						y=b+2
			#	print(x,y)
					else:
			#	print("else else loop right")
						if(board[a][b+2] == '$'):
								x,y = right(board,a,b+2)
	else:
		x,y = up(board,a,b)
	return(x,y)
def up(board,a,b):
	x=0
	y=0
	if (a-1 >= 0):
		if(board[a-1][b] != -1 and board[a-1][b] != '*' and board[a-1][b] != '$'):
			#print("if loop up")
				x=a-1
				y=b
		elif(board[a-1][b] == '*' or board[a][b] == -1):
			#print("elif loop up")
				x,y = down(board,a,b)
		else:
			if (a-2 >= 0):
			#print("else loop up")
				if (board[a-2][b] != -1 and board[a-2][b] != '*' and board[a-2][b] != '$'):
			#	print("else if loop up")
					x=a-2
					y=b
				elif(board[a-2][b] == '*' or board[a-2][b] == -1 ):
			#	print("else elif loop up")
					x,y = down(board,a,b)
				else:
			#	print("else else loop up")
					if(board[a-2][b] == '$'):
						x,y = up(board,a-2,b)
	else:
		x,y = down(board,a,b)
	return(x,y)
def down(board,a,b):
	x=0
	y=0
	if (a+1 <= 10):
		if (board[a+1][b] != -1 and board[a+1][b] != '*' and board[a+1][b] != '$'):
			#print("if loop down")
				x=a+1
				y=b
		elif(board[a+1][b] == '*' or board[a+1][b] == -1):
			#print("elif loop down")
				x = random.randint(1,10)-1
				y = random.randint(1,10)-1
		else:
			#print("else loop down")
			if (a+2 <= 10):
				if (board[a+2][b] != -1 and board[a+2][b] != '*' and board[a+2][b] != '$'):
			#		print("else if loop down")
						x=a+2
						y=b
				else:
			#		print("else else loop down")
						if(board[a+2][b] == '$'):
							x,y = down(board,a+2,b)
		return(x,y)			
def generate_coords(board,a,b):
	if (a==0 and b==0):
			#print("random")
			x = random.randint(1,10)-1
			y = random.randint(1,10)-1
			if(board[x][y]=='*' or board[x][y]=='$'):
				x,y = generate_coords(board,a,b)
	else:
			x,y = left(board,a,b)
	return (x,y)
def computer_move(board,a,b):
	#generate user coordinates from the user and try to make move
	#if move is a hit, check ship sunk and win condition
	
			#else:
			#		x = random.randint(1,10)-1
			#		y = random.randint(1,10)-1
		x,y = generate_coords(board,a,b)
		#print(x,y)
		res = make_move(board,x,y)
		#print(res)
		if res == "hit":
			a=x
			b=y
			print ("Hit at " + str(x+1) + "," + str(y+1))
			if(check_sink(board,x,y) == True):
				a=0
				b=0
				board[x][y] = '$'
				#return board,a,b
			board[x][y] = '$'
			if check_win(board):
				return "WIN",a,b
			else:
				return board,a,b
		elif res == "miss":
			print ("Sorry, " + str(x+1) + "," + str(y+1) + " is a miss.")
			board[x][y] = "*"
			a=0
			b=0
			return board,a,b

def check_sink(board,x,y):
	#figure out what ship was hit
	if board[x][y] == "A":
		ship = "Aircraft Carrier"
	elif board[x][y] == "B":
		ship = "Battleship"
	elif board[x][y] == "S":
		ship = "Submarine" 
	elif board[x][y] == "D":
		ship = "Destroyer"
	elif board[x][y] == "P": 
		ship = "Patrol Boat"
	
	#mark cell as hit and check if sunk
	board[-1][ship] -= 1
	if board[-1][ship] == 0:
		print (ship + " Sunk")
		return True
def check_win(board):
	
	#simple for loop to check all cells in 2d board
	#if any cell contains a char that is not a hit or a miss return false
	for i in range(10):
		for j in range(10):
			if board[i][j] != -1 and board[i][j] != '*' and board[i][j] != '$':
				return False
	return True

def main():

	#types of ships
	ships = {"Aircraft Carrier":5,
		     "Battleship":4,
 		     "Submarine":3,
		     "Destroyer":3,
		     "Patrol Boat":2}

	#setup blank 10x10 board
	board = []
	for i in range(10):
		board_row = []
		for j in range(10):
			board_row.append(-1)
		board.append(board_row)

	
	#setup user and computer boards
	user_board = copy.deepcopy(board)
	comp_board = copy.deepcopy(board)

	#add ships as last element in the array
	user_board.append(copy.deepcopy(ships))
	comp_board.append(copy.deepcopy(ships))

	#ship placement
	user_board = user_place_ships(user_board,ships)
	comp_board = computer_place_ships(comp_board,ships)
	a=0
	b=0
	#game main loop
	while(1):

		#user move
		print_board("c",comp_board)

		comp_board = user_move(comp_board)

		#check if user won
		if comp_board == "WIN":
			print ("User WON! :)")
			quit()
			
		#display current computer board
		print_board("c",comp_board)
		input("To end user turn hit ENTER")

		#computer move
		
		user_board,a,b = computer_move(user_board,a,b)
		#check if computer move
		if user_board == "WIN":
			print ("Computer WON! :(")
                    
			quit()
			
		#display user board
		print_board("u",user_board)
		input("To end computer turn hit ENTER")
	
if __name__=="__main__":
	
	main()