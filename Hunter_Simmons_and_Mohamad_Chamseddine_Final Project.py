"""
Hunter Simmons and Mohamad Chamseddine Final Project
15NOV23

This program and attached files takes data from a statistics research project, performs calculations, and 
displays the information in an easily read format with console commands from the user
"""
#finds the mean of a list
def mean(lst):
    total = len(lst)
    sum = 0.0
    for num in lst:
        sum += float(num)
    mean = sum / total
    return mean

#finds the median number in a list
def median(lst):
    length = len(lst)
    middle = length // 2
    if length % 2 == 0:
        median = (float(lst[middle-1]) + float(lst[middle]))/2 
    else:
        median = float(lst[middle])
    return median

#finds the range of a list
def range(lst):
    length = len(lst)
    range = float(lst[length]) - float(lst[0])
    return range

#creats the DataGroup class
class DataGroup:
    
    #Sets the initial class variables to an empty string
    def __init__(self):
        self.name = ""
        self.year =""
        self.data = []
        self.source_data = []
    
    #Creats the Set Name method
    def set_name(self, new_name):
         self.name = new_name
         
    #Creats the Set Year method
    def set_year(self, new_year):
         self.year = new_year
         
    #Creats the Add Source Data method
    def add_source_data(self, source_data):
         self.source_data = source_data
    
    #Creats the set data method
    def set_data(self, data):
        self.data = data
    
    #Creats the get data method
    def get_data(self):
        return self.data
    
    #defines the string asscociated with the class
    def __str__(self):
        msg = f"The name of this data set is '{self.name}' the year of the data is {self.year}\nThe data asscociated with this data group is {self.data}."
        return msg        
    


# Opens the .txt file and extracts the data from it
with open("final_project_data.txt", "r") as myFile:
    #splits the data into lists by line
    rawDataLst = myFile.readlines()

#stores a copy of the source data for later reference
with open("final_project_data.txt", "r") as myFile:
     rawData = myFile.read()

neatDataLst = []
for line in rawDataLst:
    
    #skips the first line of the file which is the title of the data coloums
    if line == rawDataLst[0]:
            pass
    else:
        #removes \n from the end of each line 
        line = line[0:len(line)-1]
        neatDataLst.append(line)

#seperates each line in the neat data list into its own list
finalDataLst = []
for line in neatDataLst:
    finalDataLst.append(line.split(" "))

#makes a dictionary of the source data for easy indexing of the source data
dataDict = {}
for data in finalDataLst:
    dataDict[data[0]] = [data[1],data[2]]

#Seperates the refined raw data into two sets based on original column in .txt file
dataSet_1 = []
dataSet_2 = []
for data in finalDataLst:
    dataSet_1.append(data[1])
    dataSet_2.append(data[2])


#instantiats the data group 1970
data_1970 = DataGroup()

#sets the name and year for the data group also adds the source data
data_1970.set_name("1970 average age of first birth")
data_1970.set_year("1970")
data_1970.add_source_data(rawData)
data_1970.set_data(dataSet_1)
#instantiats the data group 2020
data_2020 = DataGroup()

#sets the name and year for the data group also adds source data
data_2020.set_name("2020 average age of first birth")
data_2020.set_year("2020")
data_2020.add_source_data(rawData)
data_2020.set_data(dataSet_2)



#Prints a list of commands for the program
print("Welcome!\nPlease use a single space between arguments only enter 2 arguments at most and use lowercase.\n")
print("To use data_1970 enter: 'data_1970' to use data_2020 enter: 'data_2020'.")
print("For a dictionary of the source data enter: 'dict'.")
print("To set a new name for a data group enter: 'new_name (new name here)'.")
print("To change the year of a data group enter: 'new_year (new year here)'.")
print("To get the mean of a data group enter: 'mean'.")
print("To get the median of a data group enter: 'medain'.")
print("To get the range of a data group enter: 'range'.")
print("To get the source data of a data group enter: 'source'")
print("To get the data of a data group enter: 'data'.")
print("To print the string of a data group enter: 'string'.")
print("To end the programe enter: 'END'.\n")

#makes the input console and implements the kill condition 
while True:
    user_input = input("Enter a data set: ")
    #kill condition for the loop
    if user_input == "END":
        break

    #detects if user input = dict
    if user_input == 'dict':
        while True:
            user_input2 = input("Enter: 'BACK' to select a differnt data set\nEnter a state Ex: 'North_Dakota' 'Minnesota': ")
            if user_input2 == 'BACK':
                break
            #Indexes the data dictionary
            if user_input2 in dataDict:
                print(f"{user_input2}: {dataDict[user_input2]}")
            
            else:
                print("Invalid entry")

    #chooses which data group to edit according to the user input
    if user_input == 'data_1970':
        while True:
            user_input2= input("Enter 'BACK' to choose a data set again\nEnter commands here: ")
            if user_input2 == 'BACK':
                break
            else:
                user_input2 = user_input2.split()
            #codes the new name command
            if user_input2[0] == 'new_name':
                data_1970.set_name(user_input2[1])
                print(f"data group name successfully changed to {user_input2[1]}")
        
            #codes the new year command
            elif user_input2[0] == 'new_year':
                data_1970.set_year(user_input2[1])
                print(f"data group year successfully changed to {user_input2[1]}")
        
            #finds the mean of a data set and prints it
            elif user_input2[0] == 'mean':
                data = data_1970.get_data()
                print(f"Mean of data groups is {mean(data):.2f}. ")
        
            #finds the median of a data set and prints it 
            elif user_input2[0] == 'median':
                data = data_1970.get_data()
                print(f"Median of data groups is {median(data):.2f}. ")
        
            #find the range of a data set and prints it 
            elif user_input2[0] == 'range':
                data = data_1970.get_data()
                print(f"Mean of data groups is {range(data):.2f}. ")
        
            #prints the source data for a data set
            elif user_input2[0] == 'source':
                data = data_1970.source_data
                print(data)
        
            #prints the data of a data set
            elif user_input2[0] == 'data':
                data = data_1970.data
                print(data)
        
            #prints the string of a data set
            elif user_input2[0] == 'string':
                print(data_1970)
            
            else:
                print("Invalid Entry")
    
    #chooses which data group to edit according to the user input
    if user_input == 'data_2020':
        while True:
            
            user_input2= input("Enter 'BACK' to choose a data set again\nEnter commands here: ")
            if user_input2 == 'BACK':
                break
            else:
                user_input2 = user_input2.split()
            #codes the new name command
            if user_input2[0] == 'new_name':
                data_2020.set_name(user_input2[1])
                print(f"data group name successfully changed to {user_input2[1]}")
        
            #codes the new year command
            elif user_input2[0] == 'new_year':
                data_2020.set_year(user_input2[1])
                print(f"data group year successfully changed to {user_input2[1]}")
        
            #finds the mean of a data set and prints it
            elif user_input2[0] == 'mean':
                data = data_2020.get_data()
                print(f"Mean of data groups is {mean(data):.2f}. ")
        
            #finds the median of a data set and prints it 
            elif user_input2[0] == 'median':
                data = data_2020.get_data()
                print(f"Median of data groups is {median(data):.2f}. ")
        
            #find the range of a data set and prints it 
            elif user_input2[0] == 'range':
                data = data_2020.get_data()
                print(f"Mean of data groups is {range(data):.2f}. ")
        
            #prints the source data for a data set
            elif user_input2[0] == 'source':
                data = data_2020.source_data
                print(data)
        
            #prints the data of a data set
            elif user_input2[0] == 'data':
                data = data_2020.data
                print(data)
        
            #prints the string of a data set
            elif user_input2[0] == 'string':
                print(data_2020)

            else:
                print("Invalid Entry")
    else:
        print("Invalid Enty")