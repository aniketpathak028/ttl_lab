# WAP to find the sum of the digits of a number using UDF

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

number = int(input("Enter a number: "))
result = sum_of_digits(number)
print("The sum of digits is", result)