# 1. Write a program that reads a string from keyboard and prints the unique words.
# Your program should convert input string to lower case.

input_str = input("Enter a string: ")
lower_str = input_str.lower()

words = lower_str.split()
unique_words = set(words)

print("Unique words:")
for word in unique_words:
    print(word)