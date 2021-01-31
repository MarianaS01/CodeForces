# Given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

year = int(input("Year: "))
    
not_founded = True

while (not_founded):
    year += 1
    # set can use a string and convert it to a set separating each element of the string
    if len(set(str(year))) == len(str(year)):
        not_founded = False
        print(year)   