#simple program that adds two new lines whenever there is a
# Speaker 1: and then saves the new fixed file with the Speaker Turns retained.


import re
import os



path = "/Users/lenorealford/Documents/pythonScripts/test_new_line"
for filename in os.listdir(path):
	if filename.endswith(".txt"):
		
		with open (filename, 'r') as myText:

			for line in myText:
				speakerRegex = re.compile (r'\w{1,8}\s\d\:\s')
				print speakerRegex.search(line)





					

			# with open (filename, 'w') as myText:
			#  	myText.write(myText)	
									

				# else:
				# 	pass	
				#regex = r"\w{1,8}\s\d\:\s"

				#z = re.match('\w{1,8}\s\d\:\s', lines)
			

				#done = re.sub(r'\w{1,8}\s\d\:\s',r'\n\n', data)


			# data = myText.read()
	
			# done = re.sub(r'\w{1,8}\s\d\:\s',r'\n\n', data)

			# with open (filename, 'w') as myText:
			# 	myText.write(done)
	else:
		pass