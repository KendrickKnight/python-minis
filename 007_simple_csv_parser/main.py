#########################
####### ATTEMPT 1 #######
#########################

# open CSV file --> Read CSV file
# split the file by the line (rows)
# Split the lines by commas (columns)


#file = open("customers-100.csv","r")
#fileContent = file.read()
#file.close()

# print(fileContent.split("\n"))
# print(len(fileContent.split("\n")))

#data = [] 
#for row in fileContent.split("\n"):
#    row_list = []
#    row = row.strip()

#    column_data = ""
#    quotes = False 

#    for char in row:
#        if char == '"':
#            quotes = False if quotes else True
#            column_data += char
#        elif char == "," and not quotes:
#            row_list.append(column_data)
#            column_data = ""
#        else:
#            column_data += char

#    data.append(row_list)

# print(data)

#########################
####### ATTEMPT 2 #######
#########################

with open("customers-100.csv") as fart:
    content = fart.read()
    data = []
    in_quotes  = False

    for row in content.split("\n"):
        row_list = []
        field = ""

        for char in row:
            if char == '"':
                field +=  '"'
                in_quotes = False if in_quotes else True
            elif char == "," and not in_quotes:
                row_list.append(field)
                field = ""
            else: field += char

        row_list.append(field)
        data.append(row_list)
        row_list = []
    
    print(content.split("\n")[-2])
    print(data[-2])

