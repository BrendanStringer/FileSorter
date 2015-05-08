# Brendan L. Stringer 
# File Sorter 2.0 
# Python 3
# This program will sort files based on their file extension. Most commonly it is run directoy after data running photorec in UVM's Computer Carry-In Clinic

# Import funcions
import os 

# Main function 
def main(): 

	# Initialize variables
	filePaths = []
	extensionList = []
	fileCount = 0
	SORTED_FILES = '../sorted_files/'
	copiedFiles = 0

	# Get current working directory
	# cwd = os.getcwd()

	cwd = '/users/bstringe/Documents/'

	# Verify working directory and make sure you want to run the program
	print('<-- File Sorter 2.0 -->')
	print('Is ', cwd, 'the directory you would like to sort?')
	answer = str(input('Y/N? : '))

	# Validate answer
	if answer in ('Yes', 'yes', 'Y', 'y'):

		print('\n\nOkay, lets get started...')

		# Get as list of all the files and paths. 
		for root, dirs, files in os.walk(cwd):

			# Get all the file paths
			for file in files:
				filePaths.append(os.path.join(root, file))
				fileCount +=1 

				# Get a list of file extensions
				filename, extension = os.path.splitext(file)

				# Make directories for all the extiosions
				# Make sure we don't make blank named directories
				# Make sure the drectories don't exists already
				if extension != '' and not os.path.exists(SORTED_FILES + extension):
					os.mkdir(SORTED_FILES + extension)
				

		# Print the file count
		print('File Sorter has found ', fileCount, ' files.')

		# # Create the sorted_files folder
		# if not os.path.exists(SORTED_FILES): 
		# 	os.mkdir(SORTED_FILES)

	else: 

		print('Please cd to the correct directory and run again.')
		sys.exit()


main()