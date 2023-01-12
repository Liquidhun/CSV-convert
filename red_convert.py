import sys, getopt
import os
from os.path import exists

# def main(argv):
def main(inputfile, outputfile):
	# inputfile = ''
	# outputfile = ''
	
	
	if (inputfile== "" or outputfile == ""):
		print('Error: No input file detected. Check input directory.')
		sys.exit(2)
	else:
		targetEncoding = "utf-8"
		source = open(inputfile, "r", encoding=targetEncoding)
		content = source.read()
		source.close()
		content = content.replace(",,,,,,,,,", ";;;;;;;;;")
		content = content.replace(",,,,,,,,", ";;;;;;;;")
		content = content.replace(",,,,,,,", ";;;;;;;")
		content = content.replace(",,,,,,", ";;;;;;")
		content = content.replace(",,,,,", ";;;;;")
		content = content.replace(",,,,", ";;;;")
		content = content.replace(",,,", ";;;")
		content = content.replace(",,", ";;")
		content = content.replace('","', '";"')
		content = content.replace('ID,Work Item Type,Title,Test Step,Step Action,Step Expected,Area Path,Assigned To,State', 'ID;Work Item Type;Title;Test Step;Step Action;Step Expected;Area Path;Assigned To;State')

		# content = content.replace('1.1', '1_1')
		# content = content.replace('1.2', '1_2')
		# content = content.replace('1.3', '1_3')
		# content = content.replace('1.4', '1_4')
		# content = content.replace('1.5', '1_5')
		# content = content.replace('1.6', '1_6')
		# content = content.replace('1.7', '1_7')
		# content = content.replace('1.8', '1_8')
		# content = content.replace('1.9', '1_9')
		# content = content.replace('1.10', '1_10')

		for i in range (1,10):
			for x in range (1,10):
				# print(str(i) +'.' + str(x));
				# print(str(i) + '_' + str(x))
				content = content.replace(str(str(i) +'.' + str(x)), str(str(i) + '_' + str(x)))

		target = open(outputfile, "w", encoding=targetEncoding)
		target.write(content)
		target.close()
		print('Input file is "', inputfile)
		print('Output file is "', outputfile)

if __name__ == "__main__":
	print("\nStart converting...\n")
	inputPath = "input"
	outputPath = "output"
	dir_list = os.listdir(inputPath)
	
	# print("Files and directories in '", path, "' :")
	
	# prints all files
	
	for file in dir_list:
		if os.path.exists(os.path.join(inputPath, file)):
			print(file)
			main(os.path.join(inputPath, file), os.path.join(outputPath, file))
			print("\n")
		else:
			print(file + " is missing!")
	#main(sys.argv[1:])