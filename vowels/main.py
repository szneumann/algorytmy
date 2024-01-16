def vowels(string):
    vowels_str = 'aeiou'
    result = ''
    for char in string.lower():
        if char in vowels_str:
            result += char
    return len(result)


#print(vowels('123aea'))