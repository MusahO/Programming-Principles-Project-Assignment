import time
import os


num_of_ppl = 0
cost = 0
vip = 0
vip = 0
economy = 0
twin_seats = 0
movie_dates = 0

seats = [[[' \t', '*\t', '*\t', '*\t','*\t', '*\t', '*\t', '*\t', '*\t', '*\t','*\t', '*\t', '*\t', '*\t', '*\t', '*\t','*\t', '*\t', '*\t', '*\t', '*'] for i in range(19)
    ] for i in range(19)]


def choosing_seats():

	global cost 
	global vip 
	global vvip 
	global economy
	global twin_seats
	global num_of_ppl
	decision = 'y'

	while decision == 'y':
		num_of_seats = 0
		print('\n Seat\t\t\t\tSeat Price\t\tSelection\nTwin Seats(1)\t\t\t25,000\t\t\t1\nVVIP(2)\t\t\t\t100,000\t\t\t2\nVIP(3)\t\t\t\t50,000\t\t\t3\nEconomy(4)\t\t\t20,000\t\t\t4')
		seat_choice = int(input('Please make your selection: '))
		num_of_seats = int(input("Please enter number of seats you want to book: "))
		num_of_ppl += num_of_seats

		if seat_choice == 1:
			cost += 25000*num_of_seats
			twin_seats += 1*num_of_seats
		elif seat_choice == 2:
			cost += 100000*num_of_seats
			vvip += 1*num_of_seats
		elif seat_choice == 3:
			cost += 50000*num_of_seats
			vip += 1*num_of_seats
		elif seat_choice == 4:
			cost += 20000*num_of_seats
			economy += 1*num_of_seats

		decision = input('Would you like to book more Seats ? (y/n): ')
		if type(decision) != str(decision):
			decision = input('Would you like to book more Seats ? (y/n): ')
		
	print("you have reserved ", num_of_seats, " seats")

	total_available_seats = 320
	os.system('cls')
	value = 0
	print("availabe seats are marked with *")
	for j in range(19):
		for column in range(1, 21):
			value += 1
			seats[j][0][column] = str(value) + ('\t')
		value = 0

	for k in range(15):
		for row in range(1, 17):
			value += 1
			seats[k][row][0] = str(value) + ('\t')
		value = 0
	
	for row in range (17):
		for column in range(21):
			print(seats[0][row][column], end='')
		print('')

	for n in range(num_of_ppl):
		row = int(input('Please Enter the row of desired seat : '))
		while row < 1 or row > 16:
			row = int(input("Please enter number for the column of desired seat: "))
		column = int(input('Please enter number for the column of desired seat: '))
		while column <1 or column>20:
			column=int(input("Please Enter column number that exists: "))
		while seats[0][row][column] == '#\t':
			row = int(input('Seat Has already been taken\n Please enter number of row for available Desired seat: '))
			while row<1 or row>16:
				row = int(input('Please Choose another seat: '))
			column = int(input("Please enter column of desired seat: "))
			while column <1 or column > 20:
				column = int(input("Enter different column that exists: "))
		os.system('cls')

		seats[0][row][column] = '#\t'
		for row in range(17):
			for column in range(21):
				print(seats[0][row][column], end='')
			print('')
	print("Your seat has been booked!")

	total_available_seats -= num_of_ppl

	if total_available_seats != 0:
		print ("Number of seats available: ", total_available_seats)
	else:
		print ("Available seats: None")
		print ("Please Try Again ")
	print("Total sales: shs. ", cost)
	
def exit():
	pass

def main():
	print("\n Cinemax Movie Night")
	print("SpiderMan Far From Home")
	print("Date: November 5, 2018, Time: 8:00 PM")
	print(time.strftime("%H:%M:%S"))
	choosing_seats()

if __name__ == '__main__':
	main()