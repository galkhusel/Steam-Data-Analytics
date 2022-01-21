"""            <th>Date</th>
            <th>Price</th>
            <th>Gain</th>
            <th>Discount</th>




<tr>
            <td>January 5, 2021</td>
            <td>$9.99</td>

                        <td class="gain-minuse">+$8.00</td>
            
                        <td>-</td>
                    </tr>
"""
import csv
import json
import time

START = 0
END = 0


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def __innit__(self):
		self.start
		self.end
		self.data

	def clean(self):
		self.start = None
		self.end = None
		self.data = None

	def handle_starttag(self, tag, attrs):
		print("Encountered a start tag:", tag)
		self.start = tag

	def handle_endtag(self, tag):
		print("Encountered an end tag :", tag)
		self.end = tag

	def handle_data(self, data):
		print("Encountered some data  :", data)
		self.data = data

	def get_start(self):
		return self.start

	def get_end(self):
		return self.end

	def get_data(self):
		return self.data




HTMLparser = MyHTMLParser()

def parse_sp(data):
	#HTMLparser = MyHTMLParser()
	HTMLparser.feed(data)
	print(HTMLparser.get_data())
	#HTMLparser.clean()


def parse_sc(data):
	HTMLparser.feed(data)

def parser(line_list):

	list_return = []
	list_aux = []

	for line in line_list:
		#print(line)
		parse_sp(line)

	return list_return

def open_file(id_):
	print("tyes")
	try:
		print("tyes2")

		with open ("F:/BACKUP/TP Final coder/SCRAPPER/sprice/sp"+ str(id_) + ".txt", "r") as sp_txt:
			with open ("F:/BACKUP/TP Final coder/SCRAPPER/scharts/sc"+ str(id_) + ".txt", "r") as sc_txt:
				
				text_sp = sp_txt.readlines()
				#print(text_sp)
				lista = parser(text_sp)
				
	except:
		return 0

	return 1

def file_loop (idlist,start,end):

	for id_pos in range(start, end+1):

		id_ = idlist[id_pos]
		print(id_)
		open_file(id_)
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
	file_loop(idlist,START,END)



main()