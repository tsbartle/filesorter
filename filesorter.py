#!/usr/bin/env python3

# This script will sort files based on their file extension.

# Import functions
import os 
import sys

# Main 
def main(): 

	# Variables
	extensionList = []
	fileCount = 0
	SORTED_FILES = '../sorted_files/'
	copiedFiles = 0
	noExtension = 'missing_extension'

	# Check if user is root
	if os.geteuid() != 0:
		exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

	# Get current working directory
	cwd = os.getcwd()

	# Verify working directory and make sure you want to run the program
	print('\n')
	print('<-- File Sorter -->')
	print('Is ', cwd, 'the directory you would like to sort?\nNOTE: Sorting the wrong directory will cause problems.')
	answer = str(input('Y/N? : '))

	# Validate answer
	if answer in ('Yes', 'yes', 'Y', 'y'):

		print('\n\nOkay, lets get started...')

		# Make sure a sorted_files folder does not exist on this drive and quit if it does
		if not os.path.exists(SORTED_FILES):
			os.mkdir(SORTED_FILES)
			# This creates a "missing_extension" folder that will be used for files that 
			# do not have extensions
			os.mkdir(SORTED_FILES + noExtension)
		else:
			# Quit if the SORTED_FILES folder already exists. This is to protect files from being overwritten.
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
				# Check that directories don't already exist
				# Move the file into it's extension correct folder
				if extension != '' and not os.path.exists(SORTED_FILES + extension):
					os.mkdir(SORTED_FILES + extension)
					os.rename(filePaths, SORTED_FILES + extension + '/' + file)
				
				# Move the file if the folder already exists
				elif extension != '': 
					os.rename(filePaths, SORTED_FILES + extension + '/' + file)

				# For files that do not have extensions use the "noExtension" folder
				else:
					extension = noExtension
					os.rename(filePaths, SORTED_FILES + extension + '/' + file)

				# Print status to the user
				print("Moving file:", filePaths, "to", SORTED_FILES + extension)
				print('File Sorter has moved ', fileCount, ' files')

		# Print the file count
		print('\n\nFile Sorter moved ', fileCount, ' files.')

	else: 

		# Message to display if user was not in the correct directory
		print('Please change to the correct directory and run the script again.')
		sys.exit()

main()