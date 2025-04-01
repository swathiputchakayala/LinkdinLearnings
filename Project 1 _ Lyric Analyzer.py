#Splitting a string
text = '''
Student of the Year 2 is a 2019 Indian Hindi-language sports romantic comedy film directed by Punit Malhotra and produced Karan Johar's Dharma Productions. A standalone sequel to the 2012 film Student of the Year, it stars Tiger Shroff, Tara Sutaria, Ananya Panday, and Aditya Seal. It marks the debuts of both Panday and Sutaria in Hindi cinema.

Student of the Year 2 was released in on 10 May 2019. Upon its release the film was panned by critics, with criticism directed at the script, unreal situations and unrealistic depiction of Indian schools and colleges, although Shroff's action sequences were praised. Holding a rating of 6% on Rotten Tomatoes, it is among the lowest-rated Indian films. It did an average business at the box office with a worldwide collection of ₹98.16 crore against its ₹65 crore budget.
'''
print(text)
print(len(text)) #No. of words
print(len(text.split())) # No of Words because split.() gives no of letters that are seperated by space.

# Printing how many times each letter is repeated.

letters = 'a a d n s n s b y g f d a d h u s b'
print((letters.split()))
letter_count = {}
for letter in letters.split():
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count)

# Printing how many times each word is repeated in above big paragraphs.

print((text.split()))
word_count = {}
for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
    
############################                Lyric Analyzer                ############################                Lyric Analyzer                ############################



