# Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to 
# decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

#code = input("Borze code: ")

def translate(code):
    borze_dict = {'.':'0', '-.':'1', '--':'2'}
    borze_msg = ''
    translation = ''

    for char in code:
        borze_msg += char
        if borze_msg in borze_dict.keys():
            translation += borze_dict[borze_msg]
            borze_msg = ''


    return translation

print(translate(input()))                 