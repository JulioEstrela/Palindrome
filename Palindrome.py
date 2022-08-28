import string

alphabet = frozenset(string.ascii_lowercase)

text = input()
text = text.lower()

textWithoutSpace = text.replace(' ', '')
invertedTextWithoutSpace = textWithoutSpace[::-1]

textWithoutFormat = ""
for char in textWithoutSpace:
    if not set(char).issubset(alphabet):
        char = '' 
    textWithoutFormat += char
    
invertedTextWithoutFormat = textWithoutFormat[::-1]
    
if textWithoutFormat == invertedTextWithoutFormat:
    print(textWithoutFormat, "=", invertedTextWithoutFormat)
    print("Palindrome")
else:
    print(textWithoutFormat, "≠", invertedTextWithoutFormat)
    print("Non-palindrome")