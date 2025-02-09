# Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 
# 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.
# Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether 
# number n is a nearly lucky number.

def nearly_lucky(number):
    lucky_count = number.count('4') + number.count('7')

    if lucky_count == 4 or lucky_count == 7:
        return 'YES'
    else:
        return 'NO'

print(nearly_lucky(input()))                
