# Write a program that accepts a string and change its lowercase vowels to special character as given below.
# a # e @ i s
# 0 % u!
input_str = input("Enter a string: ")
output_str = ""
for char in input_str:
    if char in "aeiou":
        if char == "a":
            output_str += "#"
        elif char == "e":
            output_str += "@"
        elif char == "i":
            output_str += "$"
        elif char == "o":
            output_str += "0"
        elif char == "u":
            output_str += "!"
    else:
        output_str += char
print("Modified string:", output_str)