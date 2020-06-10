# read animals.txt
# and write animals_new.txt
file = open("animals.txt", "r")
animals = file.readlines()
file_new = open("animals_new.txt", "w")
for line in animals:
    file_new.write(line.rstrip())
    file_new.write(" ")
file.close()
file_new.close()
