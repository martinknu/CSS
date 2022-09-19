#Created: 2022-09-04
#Author: Martin Knudsen
#Purpose: To create examples of all HTML colors


#------------ Dependencies ---------------
import os
import sys



#------------ File path ---------------

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


colorsFilePath = get_script_path() + "/"
colorsFileName = "htmlcol.txt"

colorsOutputFile = "javascriptarray.html"

#------------ open file and read colors---------------
file = open(colorsFilePath + colorsFileName, "r")
content = file.read()

file.close()
#print("File closed")

data_into_list = content.split("\n")
#print(data_into_list)


#------------ create and append to files---------------
file = open(colorsOutputFile, "a")

# Using for loop
for color in data_into_list:
    #print(color)
    file.write("<div style=\"background-color:%s \" " % color)
    file.write("> %s </div>\r\n" % color)


file.write("---------------Javascript array------------------")
file.write("[")
for color in data_into_list:
    file.write("\"%s\", " % color)

file.write("]")    
file.close()