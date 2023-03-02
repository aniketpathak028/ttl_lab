# Write a program that reads a string from keyboard and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation or anything other than the letters a-z.

import string
input_str = input("Enter a string: ")
lower_str = input_str.lower()
letter_freq = {}
for char in lower_str:
    if char in string.ascii_lowercase:
        letter_freq[char] = letter_freq.get(char, 0) + 1
sorted_letters = sorted(letter_freq, key=letter_freq.get, reverse=True)
print("Letters in decreasing order of frequency:")
for letter in sorted_letters:
    print(f"{letter}: {letter_freq[letter]}")