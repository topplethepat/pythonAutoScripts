# finds matches from two csv files, exports those matches to create new csv.
import pandas as pd

def find_matches(file_one,file_two,resfile):

	a = pd.read_csv(file_one)
	b = pd.read_csv(file_two)
	c = pd.merge(a, b, how='inner', on=['fileURL'])

	c.to_csv(resfile)

find_matches('file.csv','file2.csv','results.csv')	