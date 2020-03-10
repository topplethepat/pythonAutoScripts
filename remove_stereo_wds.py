# this removes "Agent" and "Customer" from transcript to prepare for WER comparison
import csv
import os


def clean_data():
	path = "/path/2/files"
	for filename in os.listdir(path):
		if filename.endswith(".txt"):
			with open (os.path.join(path,filename), 'r') as f:
				my_text = f.readlines()
				x = my_text[0].replace('Customer:', '')
				cleaned_text = x.replace('Agent:', '')
				with open (os.path.join(path,filename), 'w') as myText:
					myText.write(cleaned_text)
	
clean_data()

			