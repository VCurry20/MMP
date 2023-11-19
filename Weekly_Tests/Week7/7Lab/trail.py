
# Open file in read mode
file = open("test.txt", "r", encoding="utf8")

# Read the content of file
data = (file.read(-1))

# Get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)