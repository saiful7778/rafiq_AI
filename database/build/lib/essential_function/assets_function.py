import os

# convert srting sentence to list
def tokenize(sentence):
    li = list(sentence.split(" "))
    return li

# convert list to srting
def list_to_str(sentence):
    return str(' '.join(sentence))

# find the matching items between those lists
def find_common(list_1, list_2):
    word = [element for element in list_1 if element in list_2]
    return str(''.join(word))

# last occurrence of an item
def last_word(list, word):
    return int(len(list)-list[::-1].index(word)-1)

# root file location
def dirlocation():
    return os.getcwd()