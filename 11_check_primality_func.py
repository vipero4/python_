# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def is_prime():
    number = int(input("Give me a number: "))
    return number


check_prime = is_prime()
new_list = []

for i in range(2, check_prime):
    if check_prime % i == 0:
        new_list.append(i)

if len(new_list) >= 1:
    print('Not prime')
else:
    print('Prime')
