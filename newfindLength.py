#this will find the length in seconds of an audio file and write it to a results file
import os

import pandas

path="/Users/lenorealford/Documents/pythonScripts/testVoicemailDownload"
res_file = "test4VM.csv"
counter = 0
data = pandas.DataFrame([])
for filename in os.listdir(path):
	if filename.endswith(".wav"):
		f = open(filename, 'r')
		#with open (filename, 'r') as f:
		f.seek(28)
		a = f.read(4)
		byteRate=0
				
		for i in range(1,4):
			byteRate=byteRate + ord(a[i])*pow(256,i)
					
			fileSize=os.path.getsize(filename)
					
			ms=((fileSize-44)*1000)/byteRate
			sec = ms/1000
			counter += 1
		data = data.append(pandas.DataFrame({'Filename':filename, 'Sec': sec},index = [counter]), ignore_index=True)
			
		newdata = data.to_csv(index=False)
				
		with open(res_file, 'w') as results:
			results.write(str(newdata))
				
				
				

