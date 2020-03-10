#this script will count words in a json file
#then transfers filename and number of words to csv file
#LA 2018

import json
import os
import csv


def count_words(resfile):
	path = "/path/2file"
	for filename in os.listdir(path):
		if filename.endswith(".json"):

			data = json.load(open (filename))
			data_list = data["media"]["transcripts"]["latest"]["words"]
			word_count = sum('p' in sub for sub in data_list) - 1
			with open (resfile, 'a') as my_csv:
				fieldnames = ['FileName', 'WordCount']
				output_writer = csv.DictWriter(
				my_csv, fieldnames = fieldnames ,delimiter = ',', quotechar = '"')

				output_writer.writerow({'FileName' : filename, 'WordCount' : str(word_count)})

count_words('res.csv')				