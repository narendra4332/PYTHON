#file handling consepts

#reading text files by line by lines

# file = open('demofile.txt', 'r')
# file = open("C:/Users/ASUS/Desktop/narendra.txt", 'r')

# line = file.read()
# print(line)

# error
# lines = file.readlines()
# print(lines)

# with open('school.txt', 'r') as file:

json_obj={
    'name':'narendra',
    'city':'bhipal'
}

with open('sample.txt', 'w') as file:
    for  eliment in json_obj:
        print(json_obj[eliment])
        to_store = json_obj[eliment]
        file.write(f"{to_store}\n")
    file.close()

    
