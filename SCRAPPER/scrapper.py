import requests
import csv
import json
import time

INICIO = 0
FIN = 29237
#
STEAM_PRICE = "https://steampricehistory.com/app/"
STEAM_CHARTS = "https://steamcharts.com/app/"

PATH_SP = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/SCRAPPER/sprice"
PATH_SC = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/SCRAPPER/scharts"
PATH_ERROR = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/SCRAPPER/ERROR"

APP_LIST_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics"

def scrapper_(id_):


	steam_price_url = STEAM_PRICE + str(id_)
	steam_charts_url = STEAM_CHARTS + str(id_)

	steam_price = requests.get(steam_price_url)
	steam_charts = requests.get(steam_charts_url)

	try:
		with open (PATH_SP+ "/sp"+ str(id_) + ".txt", "w") as sp_txt:
			with open (PATH_SC + "/sc"+ str(id_) + ".txt", "w") as sc_txt:
				sp_txt.write(steam_price.text)
				sc_txt.write(steam_charts.text)
	except:
		with open (PATH_ERROR + str(id_) +"---ERROR---.txt", "w") as ERROR:
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

	idlist = get_id(APP_LIST_PATH + "/app_list.csv")
	idlist.pop(0)
	scrapper(idlist,INICIO,FIN)

main()
