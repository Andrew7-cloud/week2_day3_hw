"""  Create a function that given a string as a parameter of upper/lower case letters and empty space characters (" "),
 return the length of the last word. 
 Meaning, the word that appears far most to the right if we loop through the words.
"""

# Example Input: "Hello World"
# Example Output: 5


# Example Input: "Today is Tuesday"
# Example Output: 7


input_response = input("Please send a message: ")

input_response_length = len(input_response)
print(input_response_length)


# for item in input_response:
#    if item = "":

""" Solution below
def find_word(string):
    lista = string.split()
    return len(lista[-1])
print(find_word("Hello World"))
print(find_word("Today is Tuesday"))

"""
