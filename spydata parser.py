from bs4 import BeautifulSoup
import csv
import json
import time
import pandas as pd 

PARSED_CSV_PATH = "PARSER/"

"""(0,2,6,5,7), usecalls=[0.2]"""

ar = pd.read_csv("steamspy_data.csv")


developer = ar.iloc[:,[0,2]]
score = ar.iloc[:,[0,5,6]]
genre = ar.iloc[:,[0,17]]
"""
with open (PARSED_CSV_PATH + "developer.csv", "w") as dev_csv, open (PARSED_CSV_PATH + "score.csv", "w") as s_csv, open (PARSED_CSV_PATH + "genre.csv", "w") as gen_csv:

	developer.to_csv(dev_csv)
	score.to_csv(s_csv)
	genre.to_csv(gen_csv)

"""

developer.to_csv("developer.csv")
score.to_csv("score.csv")
genre.to_csv("genre.csv")

