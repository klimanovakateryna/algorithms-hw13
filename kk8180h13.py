# Find the lowest cost match of the TARGET string anywhere in the book

# Create a 2D array, where i - position in the TARGET string, and j - positon in the book

# It will store the min alignment cost for the substring of the book from 0 to j, and the substring of the TARGET string from 0 to i

# The match can start anywhere in the book, and we need to check every final cell where the last character of the TARGET is aligned

# And find the minimum cost one

# Once found, we need to print the cost, show where the match starts, print the character alignment

