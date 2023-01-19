# WAP to input a number and print in words using UDF

def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' ' + number_to_words(n % 100))
    else:
        return 'Number is too large to be spelled out.'

num = int(input("Enter a number between 1 and 999: "))
print(number_to_words(num))