# The whole point of this exercise is to NOT use list slices or [::-1]
# Also ye, im over engineering this a bit xD

# well this method also removes whitespaces lol
def reverseString(inp: str) -> str:
    str_output = ''

    for char in inp.split():
        str_output = char + str_output

    return str_output

# This method doesn't work since split() removes whitespaces!
def reverseString2(inp: str) -> str:
    arr_inp = inp.split()
    arr_inp.reverse()
    return ''.join(arr_inp)


def reverseString3(inp: str) -> str:
    arr_inp = list(inp)
    arr_inp.reverse()
    return ''.join(arr_inp)

print("Hi! Gimme a sentence or string, and i will reverse it for you!")
user_input = input()
if isinstance(user_input, str):
    print("The reverse of your string is:")
    print(reverseString3(user_input))
else:
    print('Invalid input! Try again!')
