# Sung Byun
# replace excercises
def replace(original, old, new):
    """ Start with initial value checking; that
        if original is empty or the object that you wanna transfom are not valid,
        just return the original strings
        Transform the original script into list and when there's string you wanna manipulate,
        treat them accordingly and store in new variable
    """
    if len(original) < 1 or old not in original or len(old) < 1:
        return original

    i = 0
    while i < len(original):
        original = list(original)
        # print(i, original[i])
        if original[i] == old:
            # print('>>>>', i, type(original))
            original.remove(original[i]) # you can't chain the methods
            original.insert(i, new)
            # print(type(original))
            newString = ''.join(original)
            # print(type(newString))
        i += 1
    return newString

def main():
    """ Prompt users to put the strings to fiddle with,
        and return the newString
    """
    original = input('Provide string(s) you wanna play with: ')
    old = input('Provide string that you wanna replace: ')
    new = input('How do you wanna change? ')

    newString = replace(original, old, new)
    print(newString)

main()
