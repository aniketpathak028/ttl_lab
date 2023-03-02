# Write a program that reads two strings from keyboard and prints the common words. Your program should convert input string to lower case
# Read two strings from keyboard
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Convert both strings to lowercase
str1 = str1.lower()
str2 = str2.lower()

# Split the strings into lists of words
list1 = str1.split()
list2 = str2.split()

# Find the common words in the two lists
common_words = set(list1) & set(list2)

# Print the common words
if len(common_words) == 0:
    print("There are no common words.")
else:
    print("Common words: ")
    for word in common_words:
        print(word)