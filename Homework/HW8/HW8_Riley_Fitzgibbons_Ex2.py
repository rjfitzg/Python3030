'''
Homework8 Exercixe 2
Riley Fitzgibbons

Decrypt a PDF using a dictionary attack
'''

def decryptPDF(pdfRead):
	import time
	# Load dictionary 
	dic = open(dictName, 'r')
	# Start timer
	start = time.time()

	# Begin attack
	for line in dic:
		for word in line.split():
			print(word)
			if (pdfRead.decrypt(word) > 0):
				end = time.time()
				# Took about 3:03 minutes
				print('%s decrpyts the file. It took %s long' % (word, start-end))
				return
	print('No words in the dictionary worked.')

# Import packages
import PyPDF2 as pdf

# Set variables
pdfName = 'Util/encrypted.pdf'
dictName = 'Util/dictionary.txt'

# Read in pdf
pdfRead = pdf.PdfFileReader(open(pdfName, 'rb'))

# If encrpyted, start decrypt
if (pdfRead.isEncrypted):
	decryptPDF(pdfRead)

