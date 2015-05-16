#filesorter - sort files by extension

import os
import sys
import fnmatch
import shutil
from time import sleep

def main():

	pwd = os.getcwd() #the current working directory

	#version info, verify current directory is correct.
	print("<-- filesorter 1.0 --> \n")
	print("Is", pwd, "the directory you wish to run filesorter on?")
	answer = str(input("Y/N? : "))

	#check if input from user was valid
	if answer in ('y', 'Y', 'yes', 'Yes'):
		print("\nOK! lets get started...")
		sleep (1)
		get_file_paths(pwd)

	elif answer in ('n', 'N', 'No', 'no'):
		sys.exit("You need to cd to the directory you wish to run filesorter from. cd to the correct directory, then run filesorter agian. \n\n")


	else:
		sys.exit("You did not answer yes or no (Y/N). Filesorter will exit now...\n\n")


def get_file_paths(dir):

	#variable
	filesfound = 0
	extension_array = []
	paths_array = []

	#display message
	print("Building a list of files within this directory...")
	sleep(3)

	#for everything in the directory, get the file path
	#save all file paths to array
	for root, dirs, files in os.walk(dir):

		for file in files:
			if fnmatch.fnmatch(file,"*.*"):
				filepaths = (os.path.join(root, file))
				paths_array.append(filepaths)

				#take the filepath and split the extension
				fileName, fileExtension = os.path.splitext(filepaths)
				fileExtension = fileExtension.lstrip('.')

				if fileExtension not in extension_array:
					extension_array.append(fileExtension)

			filesfound = filesfound + 1
			set(extension_array)

	print("\n-------------------------------------------------------------")
	print("Filesorter has found:", filesfound, "files.")
	print("Filesort has found", len(extension_array), "different file extensions.")
	sleep(4)

	sort(extension_array, paths_array, filesfound)

def sort(extensions, filepaths, filesfound):
	
	sorted_files = "../sorted_files"
	copiedFiles = 0
	remainingFiles = filesfound
	percent = 0
	
	sleep(1)

	print("\nCreating necesary directories...")

	if not os.path.exists(sorted_files):
		os.mkdir(sorted_files)
		print("created directory to sort files to", sorted_files)
	
	else:
		print("../sorted_files directory already exists...\n")

	for item in extensions:
		
		item = sorted_files+"/"+item
		if not os.path.exists(item):
		
			os.mkdir(item)
			print("created directory for", item)

		else:
			print("directory for", item, "already exists.")
	
	sleep(3)

	print("\n---------------------Copying files---------------------------\n")
	
	sleep(1)
	for extension in extensions:

		for path in filepaths:
			#take the filepath and split the extension
			fileName, fileExtension = os.path.splitext(path)
			folder = fileExtension.lstrip('.')
			
			try:
				if extension == folder:
					destination = sorted_files+"/"+extension
					shutil.move(path,destination)
					print("copying:", path, "to", destination, "\n[Files remaining:", remainingFiles, "]", "\n[Percent Complete:", format(percent, '.2f'), "]")
					remainingFiles = (remainingFiles - 1)
					copiedFiles += 1
					percent = (copiedFiles/filesfound)*100
			
			except shutil.Error:
				print("there was an error with", path, "and", destination)

			except FileNotFoundError:
				print("file", path, "was not found, skipping...")

			except OSError:
				print("file", path, ":No such service or address, skipping...")

	sleep(2)
	os.chdir("../") #change directory up one level
	pwd = os.getcwd() #the current working directory
	
	print("\nDONE! the sorted files can be found here:", pwd+"/sorted_files")

main()
