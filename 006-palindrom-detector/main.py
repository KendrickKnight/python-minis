# Get input
# Clean the input 
# check if text length is odd or even
#   if odd -> text length - 1
#   if even -> text length 
#   or just round it down...
# check if first {text-length/2} letters are 
#   the same with the last {text-length/2} letters, backwards
# 


def detectPalindromes(text:str):
#Cleaning the input text
    text = text.strip().casefold()
    text = "".join(char for char in text if char.isalnum())

    half_len = len(text) // 2

    return text[:half_len] == text[-1:-(half_len)-1:-1]


