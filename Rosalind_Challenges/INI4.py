# Rosalind INI4 "Conditions and Loops"
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

a = 4807
b = 9467

sum = 0
for int in range(a, b + 1, 1):
    if int % 2 == 1:
        sum += int
print(sum)