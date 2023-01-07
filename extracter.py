import re
from openpyxl.workbook import Workbook 

file = "outpt.txt"    #name of the file containing 10 digit numbers from trash txt data

mobile_list=[]
with open(file) as f:
	for line in f:
		text=line
		phoneNumRegex = re.compile(r'[789]\d{9}',re.VERBOSE)
		for groups in phoneNumRegex.findall(text):
			#print(groups)
			mobile_list.append(groups)
			file1=open

print(mobile_list)
file = open('final.txt','w')   #name of the file where you want to store the numbers
for item in mobile_list:
	file.write(item+"\n")
file.close()

