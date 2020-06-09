# Program to count the number of each vowels in a string
import yaml

# string of vowels
vowels = 'aeiou'
  
def count(string):
    # make it suitable for caseless comparisions
    string = string.casefold()

    # make a dictionary with each vowel a key and value 0
    count = {}.fromkeys(vowels,0)

    # count the vowels
    for char in string:
        if char in count:
            count[char] += 1
    return count

# Load strings from yaml file
with open(r'strings.yml') as file:
    list_of_strings = yaml.load(file, Loader=yaml.FullLoader)

# Iterate through list of strings in file  
for string in list_of_strings["strings"]:
    total_count = count(string)
    print(total_count)
