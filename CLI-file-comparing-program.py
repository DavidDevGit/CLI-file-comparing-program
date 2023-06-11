#importing difflib
import difflib

print ("place the full path of file or do it from directory of files")

print ("file 1")

f1 = open(input(),"r")

print ("file 2")

f2 = open(input(),"r")

f1_data = f1.readlines()
f2_data = f2.readlines()

for i in range(len(f1_data)):
	if f1_data [i] != f2_data [i]:
		print ("Line "+ str(i+1) + "doesn't match.")
		print ("----------------------")
		print ("File1: " + f1_data[i])
		print ("File2: " + f2_data[i])


# closing files
f1.close()
f2.close()
