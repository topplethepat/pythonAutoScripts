#simple program that adds two new lines whenever there is a
# Speaker d: and then saves the new fixed file with the Speaker Turns retained.


import re
import os



path = "/Users/lenorealford/Documents/pythonScripts/test_new_line"
for filename in os.listdir(path):
	if filename.endswith(".txt"):
		
		with open (filename, 'r') as myText:
			data = myText.read()
	
			
			done = re.sub(r'Speaker 1: ',r'\n\nSpeaker 1: ', data)
			next_done = re.sub(r'Speaker 2: ',r'\n\nSpeaker 2: ', done)

			with open (filename, 'w') as myText:
				myText.write(next_done)

			




	else:
		pass