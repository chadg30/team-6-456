# Author: Chad Green & Diyorbek Juraev
# Date: 03/31/2021
'''
This program:
1. validates an input file and contents in it.
2. Handle file opening in a mode
2.1. Handle file exceptions, etc.
3. Search file contents
'''
import magic

def parse_file(filename):
    #open the file to read, and implement the logic as required by the assignment-4
    # opens the file
    parsefile = open(filename, "r")
    # reads the lines into lineread
    lineread = parsefile.readlines()
    # reads the lines line by line
    for line in lineread:
        # if true is in the line then the line is split and the keyword is printed
        if 'true' in line:
            keywords = line.split(":")
            print(keywords[0])
    # closes the file
    parsefile.close()


def validate_file(filename):
    # validate if the file is a text file, if it is return true, otherwise return false
    validate = False # bool to check if file is text
    file = magic.from_file(filename) # downloaded and imported magic to check get the file type
    # check the magic to see if it is text
    if 'text' in file:
        validate=True
    # return true or false
    return validate

# Main program, do not modify it.
if __name__ == "__main__":
    filename="my_config.txt"
    valid=validate_file(filename)
    # print all the setting values set to ON/true on the configuration file.
    if valid:
        print("File %s is a valid text file. Now printing all the settings set ON" %filename)
        parse_file(filename)
    else:
        print("File %s is NOT a valid text file. Program aborted!" % filename)
