'''

'''
from CONNSIX import connsix
import random 
import utils

def main():
	ip = input("input ip: ")
	port = int(input("input port number: "))
	ai_home = input("input BLACK or WHITE: ")
	
	red_stones = connsix.lets_connect(ip, port, ai_home)
	if len(red_stones):	
		print("Received red stones from server: " + red_stones)

	if ai_home == 'BLACK':
		away_move = connsix.draw_and_read("K10")
		print("Received first away move from server: " + away_move)
	else:
		away_move = connsix.draw_and_read("")
		print("Received first away move from server: " + away_move)
	while 1:
		away_move = connsix.draw_and_read(utils.make_move())
		print("Received away move from server: " + away_move)

if __name__ == "__main__":
	main()