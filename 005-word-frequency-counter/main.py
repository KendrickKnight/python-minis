# Get input file 
# Turn into str
# remove ". , / \ ? < > ! @ etc..."
# loop on each word
#   if word not in dictionary --> add it in 
#   if word in dictionary --> add to its count
# return list

text = str('')

#open, read and close the file 
text_file = open("text-sample.txt","r")
text = text_file.read()
text_file.close()

# prepping the text 
text = text.strip()
text = text.casefold()
text = "".join(char for char in text if char.isalnum() or char == " ") # remove marks

# counting
word_counter = {}

for word in text.split(" "):
    if word in word_counter:
        continue
    else:
        word_counter[word] = text.count(word)

print(word_counter)

def frequencyCounter (text: str) -> dict:
    text = text.strip()
    text = text.casefold()
    text = "".join(char for char in text if char.isalnum() or char == " ") # remove marks

    word_counter = {}

    for word in text.split(" "):
        if word in word_counter:
            continue
        else:
            word_counter[word] = text.count(word)

    return word_counter

