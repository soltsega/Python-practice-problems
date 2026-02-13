import csv
file_name = 'C:/Users/My Device/Desktop/pythonWorkspace/file_management/csvFile.csv'
with open(file_name, 'r') as file:
    content = csv.reader(file)
    print(content)  # it will print the address of the content
    # we need to iterate over the contents to dispaly the contents
    for line in content:
        print(line)  # It will print all of the contents line by line including the heading
        # we can also print the specific column in the csv file
    index = 1
    print(line[index])
print(file.closed)