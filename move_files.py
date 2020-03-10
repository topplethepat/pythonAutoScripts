# script to move multiple files from one directory to another
# need to create csv file with filename in first column,
# destination path in second column,
# current path of file in third column

import csv
import os
import shutil
import sys

def move_files(listfile):

  with open('audio2check.csv', 'rb') as f:
      reader = csv.reader(f)
      for row in reader:
        filename = row[0]
        filepath = row[2]
        new_filepath = row[1]      
        orig_filename = os.path.join(filepath,filename)     
        new_filename = os.path.join(new_filepath,filename)

        try:
          shutil.copy(orig_filename, new_filename)   #Changed
        except:
          IOError
          print "file not there"
  print 'All done!'

move_files('myfile.csv')  