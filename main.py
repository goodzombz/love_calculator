
def value(name):
    rarity = 0
    sum = 0
    from text import letters,letter_num
    for i in name:
        rarity += letters[i]
    for i in name:
        sum += letter_num[i]
    return sum/rarity
name1 = input('what is the first kid?')
name2 = input('what is the second?')
print((20 - (abs(value(name1) - value(name2))))*5)
