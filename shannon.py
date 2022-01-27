# Prompt 1: Missing Num
# a list of numbers from 1 to max num (inclusive)
# one of the numbers will be missing from the list 
# write a function that takes the list & finds the missing number (return it, not print)

# examples: 
l1 = [1, 4, 3]
# missing num should be 2
# >>> missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
# 8
l2 = [2, 1, 4, 3, 6, 5, 7, 10, 9]

# so the actual CORRECT list for l1 [1,2,3,4]
# if you add all the numbers together, then it adds up to 10
# & the l1 with the missing number [1,4,3] only adds up to 8
# the missing num is just 10 - 8 = 2

# so in my function which takes the list AND the max_num (in this case, 4) as the params 
# i would need to get the correct SUM (10) so i can subtract the sum of all the nums in 
# l1 from it (8) to get the missing_num which is (2)

# i would have to get the sum by using the sum method (allowed)
# & also the range method
# Use the range method to get the full correct list
# by having the range use 1 as the start & because it is NOT inclusive
# the end has to be max_num (4) PLUS one

# since the l1 is misisng a number, cant use range to get its sum
# so i have to set a variable called actual_sum equal to 0
# & for each num in the list
# add it to actual_sum

# & then i return the result of this full_sum minus actual_sum

def missing_num(list,max_num):
    actual_sum = 0
    for num in list:
        actual_sum += num
    
    full_sum = sum(range(1, max_num+1))
    return full_sum - actual_sum


print(missing_num(l1,4))
#should return 2 -> YES
print(missing_num(l2,10))
#should return 8 -> YES

# Prompt 2: 
# write a function to encode text using a rotary cypher with a variable shift 

# given string might have whitespace or special characters, dont touch those 
# params are an integer or a string 
# the integer is how much you shift the letters 
# returns a new string

# [abcdefghijklmnopqrstuvwxyz]
# [defghijklmnopqrstuvwxyzabc]
# have a list of all the letters from A to Z (max index of 27)
# if the integer is 3 & if the string has a Z in it, i would have replace that Z with the letter C
# change index 27 (aka Z) to index 3 somehow (which is C)
# take the list of ABC letters 
# slice it up into 2 pieces & add them together to make the cipher ABC list 
# use the given integer to slice
# so it would CIPHER_ABC = abc[given_integer+1:] + abc[:given_integer]

# make a new variable called coded_string, which is an empty string "" so i can return it later

# then i use enumerate on both the given string & the CIPHER ABC list 
# so for the index of given string,
# check if the value of that index is in the cipher ABC list
# if it i🇸nt, then just append it to the coded_string normally
# if it IS,
# then find the index of that value from the ABC list using the index method
# use that index on the cipher list
# append the value of the cipher list index to the empty string

def make_a_cipher(string, int):
    ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    CIPHER_ABC = ABC[int+1:] + ABC[:int]
    coded_string = ""

    for char_index, char in enumerate(string):