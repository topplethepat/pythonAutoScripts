#!/usr/bin/env python
# regexBrackets finds [0:00:00] pattern and removes it in a .txt file
# it also removes speaker mentions, e.g. SPEAKER: F2

#command line example
#  python regexBrackets.py --list madLibs.txt --results ./res.txt

import argparse
import re

def main():
	parser = argparse.ArgumentParser(
		description = "script to clean files for testing"
	)
	parser.add_argument(
		'--list', 
		help = "path to txt file", 
		required = True
	)

	parser.add_argument(
		'--results',
		help = "path to output txt file of cleaned up text",
		required = True
		)

	args = parser.parse_args()

	cleanTxt(args.list, args.results)

def cleanTxt (list_path, results_path):

	with open (list_path,'r') as myText:
		data = myText.read()
		with open (results_path, 'w') as results_file:
			new = re.sub(r'\[.*?\]','', data)
			improved = re.sub(r'SPEAKER\:\s\w{1,3}','', new)
			#new = re.sub(r'SPEAKER\:\s\w\d', '', data)
		
			results_file.write(improved)
			#results_file.write(new)
			results_file.close()
				
	


if __name__ == "__main__":
	main()


