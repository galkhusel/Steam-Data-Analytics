from bs4 import BeautifulSoup
import csv
import json
import time

START = 0
END = 29237

SCRAPPER_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics/SCRAPPER"
APP_LIST_PATH = "F:/BACKUP/Estudios/Coding/CoderHouse Data Analytics/Steam Data Analytics"
PARSED_CSV_PATH = ""

def parse(soup):

	line_list = []
	line =soup.find_all(['th', 'td'])

	for col in line:
		line_list.append(col.get_text())
		

	return line_list

def parser(soup):

	list_csv = []
	tr = soup.find_all('tr')

	for line in tr:
		list_csv.append(parse(line))

	return list_csv

def open_file(id_):
	
	try:
		with open (SCRAPPER_PATH + "/sprice/sp"+ str(id_) + ".txt", "r") as sp_txt:
			with open (SCRAPPER_PATH + "/scharts/sc"+ str(id_) + ".txt", "r") as sc_txt:
				
				soup_sp = BeautifulSoup(sp_txt, 'html.parser')
				table_separator_sp = soup_sp.find_all('table')

				x = 0
				for table in table_separator_sp:
					list_csv = parser(table)
					print(list_csv)
					print("------------")
					print("------------")
					print("------------")
					print("------------")
					print("------------")
					"""
					with open("output.csv", "wb") as f:
					    writer = csv.writer(f)
					    writer.writerows(a)
					print(x)
					x+=1"""

				soup_sc = BeautifulSoup(sc_txt, 'html.parser')
				table_separator_sc = soup_sc.find_all('table')

				for table in table_separator_sc:
					list_csv = parser(table)
					print(list_csv)
					print("------------")
					print("------------")
					print("------------")
					print("------------")
					print("------------")
				
	except:
		return 0

	return 1

def file_loop (idlist,start,end):

	for id_pos in range(start, end+1):

		id_ = idlist[id_pos]
		print(id_)
		open_file(id_)


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
	file_loop(idlist,START,END)
	return 1

main()