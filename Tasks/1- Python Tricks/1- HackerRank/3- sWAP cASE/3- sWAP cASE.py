def swap_case(s):
    #swapped = s.swapcase()
    
    swapped = ''
    for letter in s:
        if letter==' ': swapped += ' '
        elif letter==letter.upper(): swapped += letter.lower()
        elif letter==letter.lower(): swapped += letter.upper()
        
    return swapped

