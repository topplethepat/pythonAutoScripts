#! /usr/bin/env python3

#  python multTxt2Csv.py --directory ./testDirectory --output ./test3.csv
import argparse
import csv
import os

def main():
  parser = argparse.ArgumentParser(
    description = "Batch upload of directory of txt files to csv file"
  )
  parser.add_argument(
    '--directory', 
    help = "path to directory of txt files", 
    required = True
  )
  parser.add_argument(
    '--output', 
    help = "path to csv file", 
    required = True
  )

  args = parser.parse_args()

  convert(args.directory, args.output)

  # ********* def convert  ***********
  
def convert(directory, file):
	
  with open(file, 'w') as output_file:
     	
    fieldnames = ['Agent', 'Transcription']
    output_writer = csv.DictWriter(
        output_file, fieldnames = fieldnames, delimiter = ',', quotechar = '"')
      
    for fileName in os.listdir(directory):
       with open(os.path.join(directory, fileName),'r') as textFile:
            output_writer.writerow({'Agent' : fileName, 'Transcription' : textFile.read()})	 


main()
