# this will find the length in seconds of an audio file and write it to a results file
# formula from https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
import os
import pandas

path="/pathtoFile/"

counter = 0

def find_length(resfile):
	data = pandas.DataFrame([])
	for filename in os.listdir(path):
		if filename.endswith(".wav"):
			f = open(filename, 'r')
			#read the ByteRate field from file (see the Microsoft RIFF WAVE file format)
			#https://ccrma.stanford.edu/courses/422/projects/WaveFormat/
			#ByteRate is located at the first 28th byte
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
				
			with open(resfile, 'w') as results:
				results.write(str(newdata))