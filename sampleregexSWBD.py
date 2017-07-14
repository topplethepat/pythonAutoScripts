#simple program that removes a pattern, and then saves the new fixed file as is.


import re
import os





path = "/Users/lenorealford/Documents/Folder/new_folder/swbd"
for filename in os.listdir(path):
	if filename.endswith(".txt"):
		with open (filename, 'r') as myText:
			data = myText.read()
			#formula for swbd
			done = re.sub(r'\w{1,7}\s\d\s\w\s\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\s\<\w\,\w{1,2}\,\w{1,4}\>','', data)

			with open (filename, 'w') as myText:
				myText.write(done)
	else:
		pass


				

		 	
