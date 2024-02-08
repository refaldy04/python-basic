print("""Ini adalah
multi line string
pada python""")

print('apa itu looping?\n' * 20)

# ADVINCE

my_name = 'Health'
print(my_name[0]) # first letter
print(my_name[-1]) # last letter

sentence = 'This is sentence'
print(sentence[:4])
print(sentence.split()[0])

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money\""
print(quote)

to_much_space = "              hello               "
print(to_much_space.strip())

print("A" in "Apple") # True
print("a" in "Apple") # False

letter = 'A'
word = 'Apple'
print(letter.lower() in word.lower())

movie = 'The Hangover'
print('My favorite movie is {}.'.format(movie))
print('My favorite movie is %s.' % movie)
print(f'My favorite movie is {movie}.')