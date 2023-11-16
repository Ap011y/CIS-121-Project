"""
Hunter Simmons and Mohamad Chamseddine Final Project
15NOV23

This program and attached files takes data from a statistics research project, performs calculations, and 
displays the information in an easily read format
"""

# Opens the .txt file and extracts the data from it
with open("final_project_data.txt", "r") as myFile:
    rawDataLst = myFile.readlines()

    #splits the data into lists by line
neatDataLst = []
for line in rawDataLst:
    if line == rawDataLst[0]:
            pass
    else:
        line = line[0:len(line)-1]
        neatDataLst.append([line])
print(neatDataLst)