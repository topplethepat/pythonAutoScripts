#program that adds two new lines whenever there is a
# [00:00:16] and then saves the new fixed file with timestamps.
#LA June 2017


import re
import os

path = "/Users/lenorealford/Documents/pythonScripts/test_new_line"
for filename in os.listdir(path):
	if filename.endswith(".txt"):
		with open (filename, 'r') as myText:
			data = myText.read()

			
			new = re.sub(r'\[.*?\]', r'\n\g<0>\n\n', data)
			with open (filename, 'w') as myText:
				myText.write(new)
				

	
    			
        		
            	

		
	
	


				

		 	
