# WORD COUNT 

# given a phrase, PRINT the word count in ascending order

# >>> word_count("berry cherry cherry cherry berry apple")
# apple: 1
# berry: 2
# cherry: 3

# >>> word_count("hey hi hello")
# hello: 1
# hey: 1
# hi: 1

# >>> word_count("hi Hi hi")
# Hi: 1
# hi: 2

# create empty dictionary to hold word: count
# split given phrase .split()
# if word not in dictionary, add it in +1 count
# if word in dictionary, just add +1 count
# sort() dictionary
# print dictionary,
#.get(key, starting value)

def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""
    word_count = {}
    words = phrase.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)

    counts = [ (count, word) for word, count in word_count.items()]
    counts.sort()
    
    for count, word in counts:
        print(f"{word}: {count}")
    
print (word_count("berry cherry cherry cherry berry apple"))








