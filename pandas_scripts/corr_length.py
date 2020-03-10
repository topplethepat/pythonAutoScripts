# finds the rows containing middle range of length, writes to other csv file.
import pandas
import csv

data = pandas.read_csv('list.csv')

df = pandas.DataFrame(data)

df = df[(df["size"] >= 22226) & (df["size"] <= 1560000)]

df.to_csv('bucket_corr_length.csv')