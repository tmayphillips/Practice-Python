first_file = "ex23-1.txt"
second_file = "ex23-2.txt"

first_list = []
second_list = []
overlapping = []

with open(first_file, 'r') as open_file:
  	line = open_file.readline()
  	while line:
          line = line.strip()
          first_list.append(line)
          line = open_file.readline()

with open(second_file, 'r') as open_file:
  	line = open_file.readline()
  	while line:
          line = line.strip()
          second_list.append(line)
          line = open_file.readline()

for i in first_list:
    if i in second_list:
        if i in overlapping:
            next
        else:
            overlapping.append(i)
    
print(overlapping)