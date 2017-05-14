import os
import shutil
import sys

class Pyorg:
	def organize(self, destination):
		curr_dir = os.getcwd()
		files = os.listdir(curr_dir)
		if len(files) == 0:
			print "Current directory is empty"
		for file in files:
			ext = file.split('.')[-1]
			dest = destination + '/' + ext
			if not os.path.exists(dest):
				os.makedirs(dest)
			if not os.path.isdir(file):
				shutil.move(curr_dir + '/' + file, dest)
				print "Moved " + curr_dir + '/' + file + ' to ' + dest

def main():
	destination = sys.argv[1]

	if destination == '--curr':
		destination = os.getcwd()

	elif not os.path.exists(destination):
		print "Destination directory does not exist"
		sys.exit(0)
	pyorg = Pyorg()
	pyorg.organize(destination)

main()