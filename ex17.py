#so there is this directory or sorts that is imports
#such as argv that is arguable varible it means its takes another
#value while running ok
from sys import argv
from os.path import exists

#we are going to take 3 other than the input for argv
script, from_file, to_file = argv
#the f thing is telling the python to format things
print(f"Copying from {from_file} to {to_file}.")
# opening and reading the file
in_file = open(from_file)
indata = in_file.read()
#how long the file we are going to put into other file is
print(f"The input file is {len(indata)} bytes long.")
#taking input are u ok if we do it
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit ENTER to continue, CTRL-C to abort.")
input()
#this is open file
out_file = open(to_file, 'w')
#this is writing the output file
out_file.write(indata)
#printing all done.
print("Alright, all done.")
#closing the files we opend
out_file.close()
in_file.close()
#still need to creat input and out file
