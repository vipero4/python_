# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string = input("Enter a word: ")

list = []
list_2 = []

for x in string:
    list.append(x)
    list_2 = list[::-1]

if list == list_2:
    print("Word is palindrome.")
else:
    print("Word is not palindrome.")
