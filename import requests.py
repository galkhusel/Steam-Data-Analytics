import requests
import csv
import json
import time

INICIO = 8804
FIN = 14617

def scrapper_(id_):


	steam_price_url = "https://steampricehistory.com/app/" + str(id_)
	steam_charts_url = "https://steamcharts.com/app/" + str(id_)

	steam_price = requests.get(steam_price_url)
	steam_charts = requests.get(steam_charts_url)

	try:
		with open ("F:/BACKUP/TP Final coder/SCRAPPER"+ str(id_) + ".txt", "w") as sp_txt:
			sp_txt.write(steam_price.text)

		with open ("F:/BACKUP/TP Final coder/SCRAPPER/scharts/sc"+ str(id_) + ".txt", "w") as sc_txt:
			sc_txt.write(steam_charts.text)
	except:
		with open ("F:/BACKUP/TP Final coder/SCRAPPER/ERROR/sp"+ str(id_) +"---ERROR---.txt", "w") as ERROR:
			ERROR.write("ERROR")

def scrapper (idlist,start,end):

	for id_pos in range(start, end+1):

		id_ = idlist[id_pos]
		print(id_)
		scrapper_(id_)
		time.sleep(5)


def get_id(PATH):

	list_ = []

	with open (PATH,encoding="utf8") as file:
		fcsv = csv.reader(file,delimiter=",")
		
		for fila in fcsv:
			list_.append(fila[0])

	return list_



def main():

	idlist = get_id("F:/BACKUP/TP Final coder/SCRAPPER/app_list.csv")
	idlist.pop(0)
	scrapper(idlist,INICIO,FIN)

main()


