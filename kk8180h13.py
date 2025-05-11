# Find the lowest cost match of the TARGET string anywhere in the book

# Create a 2D array, where i - position in the TARGET string, and j - positon in the book

# It will store the min alignment cost for the substring of the book from 0 to j, and the substring of the TARGET string from 0 to i

# The match can start anywhere in the book, and we need to check every final cell where the last character of the TARGET is aligned

# And find the minimum cost one

# Once found, we need to print the cost, show where the match starts, print the character alignment

import sys
import string
import numpy as np

#target = sys.argv[1]
#book = sys.stdin.read()

target = "T e"
book = "test"

# 2D array to store the cost of matching the target string with the book
dp = np.zeros((len(target) + 1, len(book) + 1), dtype=int)




def cost_match(char1, char2):
    if char1 == char2:
        return 0
    elif char1 in string.printable and char2 in string.printable:
        return 3
    elif (char1 in string.printable) != (char2 not in string.printable) :
        return 5
    else: 
        return 3 #both non-printable, but a match
    

    
# test

print(cost_match('a', 'a'))
print(cost_match('a', '/b'))
print(cost_match('a', 'a')) 
        