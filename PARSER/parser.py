from bs4 import BeautifulSoup
import csv
import json
import time

START = 0
END = 4
"END_END = 29237"

SCRAPPER_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/SCRAPPER"
APP_LIST_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics"
PARSED_CSV_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/PARSER/"

HEADER_PRICE_HISTORY = ['Date', 'Price', 'Gain', 'Discount',"game_id","id"]
HEADER_SALES = ['Sale', 'Date Start', 'Price', 'Discount',"game_id","id"]
HEADER_PLAYER_BASE = ['Month', 'Avg. Players', 'Gain', '% Gain', 'Peak Players',"game_id","id"]


def parse(soup):

	line_list = []
	line =soup.find_all(['th', 'td'])

	for col in line:

		line_list.append(col.get_text())
		

	return line_list

def parse_table(soup,game_id):


	list_csv = []
	tr = soup.find_all('tr')

	for line in tr:
		list_csv.append(parse(line)+[game_id])


	return list_csv[1:]


def parser(game_id):
	
	try:
		with open (SCRAPPER_PATH + "/sprice/sp"+ str(game_id) + ".txt", "r") as sp_txt, open (SCRAPPER_PATH + "/scharts/sc"+ str(game_id) + ".txt", "r") as sc_txt:
		
			soup_sp = BeautifulSoup(sp_txt, 'html.parser')
			table_separator_sp = soup_sp.find_all('table')
			_, player_price_history, sales_table, _ = table_separator_sp

			lph = parse_table(player_price_history,game_id)
			ls = parse_table(sales_table,game_id)

			print(player_price_history)


			soup_sc = BeautifulSoup(sc_txt, 'html.parser')
			table_player_base = soup_sc.find_all('table')[0]

			lpb = parse_table(table_player_base,game_id)

	
	except FileNotFoundError:
		return [],[],[]

	return lph, ls, lpb

def write_csv (idlist,start,end):

	with open (PARSED_CSV_PATH + "player_base"+ ".csv", "w") as pb_csv, open (PARSED_CSV_PATH + "sales"+ ".csv", "w") as s_csv, open (PARSED_CSV_PATH + "price_history"+ ".csv", "w") as ph_csv:

		pb = csv.writer(pb_csv)
		s = csv.writer(s_csv)
		ph = csv.writer(ph_csv)
		pb.writerow(HEADER_PLAYER_BASE)
		s.writerow(HEADER_SALES)
		ph.writerow(HEADER_PRICE_HISTORY)

		for game_id_pos in idlist[start:end+1]:
			list_pb, list_s, list_ph = parser(game_id_pos)
			pb.writerows(list_pb)
			s.writerows(list_s)
			ph.writerows(list_ph)


def get_id(PATH):

	list_ = []

	with open (PATH,encoding="utf8") as file:
		fcsv = csv.reader(file,delimiter=",")
		
		for fila in fcsv:
			list_.append(fila[0])

	return list_



def main():

	idlist = get_id(APP_LIST_PATH + "/app_list.csv")
	idlist.pop(0)
	write_csv(idlist,START,END)
	#add_column_number(csv)
	return 1

main()