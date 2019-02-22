filename = input("File to read: ")
name_counts = {}

#with open(filename, 'r') as open_file:
#    all_text = open_file.read()

with open(filename, 'r') as open_file:
  	line = open_file.readline()
  	while line:
          line = line.strip()
          if line in name_counts:
              name_counts[line] += 1
              line = open_file.readline()
          else:
              name_counts[line] = 1
              line = open_file.readline()

print(name_counts)