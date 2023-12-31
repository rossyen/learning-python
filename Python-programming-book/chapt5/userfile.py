# userfile.py
#   Program to create a file of usernames in batch mode

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print('This program creates a file of usernames from a')
    print('file of names')

    # get the file name

    infileName = askopenfilename()
    outfileName = asksaveasfilename()

    # open the files

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create the username
        uname = (first[0]+last[:7].lower)
        # write it to the output file
        print(uname, file=outfile)
        
    #close both files
    infile.close()
    outfile.close()

    print('Username have been written to', outfileName)

main()