#13. Write a function to write a comma-separated value (CSV) file. 
# It should accept a filename and a list of tuples as parameters. 
# The tuples should have a name, address, and age. 
# The file should create a header row followed by a row for each tuple.

import csv


def comma_CSV(filename, list_tuple):
    csv_file = open(filename, mode='w', newline='')
    header = ('name', 'address', 'age')
    list_tuple = [header, *list_tuple]
    obj = csv.writer(csv_file)
    obj.writerows(list_tuple)
    csv_file.close()
    
    
list_tuple = [('George', '4312 Abbey Road', 22),
              ('John', '54 Love Ave', 21)]
comma_CSV('file.csv',list_tuple)

# Read CSV file
csvfile=open('file.csv','r', newline='')
obj=csv.reader(csvfile)

print([row for row in obj])