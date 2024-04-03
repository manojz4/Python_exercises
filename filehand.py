# file1 = open(r'/home/dhpcsa/handle.txt','rt')
# print(file1.read())
# print("Before closing explicitly" , file1.closed)  
# file1.close()
# print("After closing explicitly" , file1.closed)  
# ###################

# Read from a file and modify its content

# Input file name
file1 = (r'/home/dhpcsa/handle.txt')

# Output file name
outh= "output.txt"


with open(file1, "r") as h:
    with open(outh, "w") as g:
        for line in h:
            line = "HPCSA" + " " + line
            g.write(line)

print("File changed and save " + outh)