# Brendan L. Stringer 
# File Sorter 2.0 
# Python 3
# This program will sort files based on their file extension. Most commonly it is run directoy after data running photorec in UVM's Computer Carry-In Clinic

# Import funcions
import os 
import sys

# Main function 
def main(): 

	# Initialize variables
	fileCount = 0
	SORTED_FILES = '../sorted_files/'

	# Get current working directory
	cwd = os.getcwd()

	# Verify working directory and make sure you want to run the program
	print('\n')
	print('<-- File Sorter 2.0 -->')
	print('Is ', cwd, 'the directory you would like to sort?')
	answer = str(input('Y/N? : '))

	# Validate answer
	if answer in ('Yes', 'yes', 'Y', 'y'):

		print('\n\nOkay, lets get started...')

		# Make sure a sorted_files folder does not exist on this drive and quit if it does
		if not os.path.exists(SORTED_FILES):
			os.mkdir(SORTED_FILES)
		else: 
			print('\n\nA sorted_files folder already exists.')
			print('File Sorter has quit.\n')
			sys.exit()

		# Get as list of all the files and paths. 
		for root, dirs, files in os.walk(cwd):

			# Get all the file paths
			for file in files:
				filePaths = os.path.join(root, file)
				fileCount += 1

				# Get a list of file extensions
				filename, extension = os.path.splitext(file)
				
				# Strip the . off the file extension
				extension = extension.lstrip('.')

				# Make directories for all the extiosions
				# Make sure we don't make blank named directories
				# Make sure the drectories don't exists already
				# Move the file into it's correct folder
				if extension != '' and not os.path.exists(SORTED_FILES + extension):
					os.mkdir(SORTED_FILES + extension)
					os.rename(filePaths, SORTED_FILES + extension + '/' + file)

				
				# Move the file if the folder already exists
				elif extension != '': 
					os.rename(filePaths, SORTED_FILES + extension + '/' + file)

				# Print status to the user
				print('File Sorter has moved ', fileCount, ' files')

		# Print the file count
		print('\n\nFile Sorter has moved ', fileCount, ' files.')

	else: 

		print('Please cd to the correct directory and run again.')
		sys.exit()

main()