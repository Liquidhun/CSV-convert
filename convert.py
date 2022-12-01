import sys, getopt
import os

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print('convert.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print('convert.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if (inputfile== "" or outputfile == ""):
		print('convert.py -i <inputfile> -o <outputfile>')
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

		content = content.replace('1.1', '1_1')
		content = content.replace('1.2', '1_2')
		content = content.replace('1.3', '1_3')
		content = content.replace('1.4', '1_4')
		content = content.replace('1.5', '1_5')
		content = content.replace('1.6', '1_6')
		content = content.replace('1.7', '1_7')
		content = content.replace('1.8', '1_8')
		content = content.replace('1.9', '1_9')
		content = content.replace('1.10', '1_10')

		target = open(outputfile, "w", encoding=targetEncoding)
		target.write(content)
		target.close()
		print('Input file is "', inputfile)
		print('Output file is "', outputfile)

if __name__ == "__main__":
	main(sys.argv[1:])