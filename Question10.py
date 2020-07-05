#10. Write a function that takes camel-cased strings 
# (i.e. ThisIsCamelCased), and converts them to snake case 
# (i.e. this_is_camel_cased). Modify the function by adding an argument, separator, 
# so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def string_converter(strings,seperators):

    new_string=strings[0].lower()

    for letter in strings[1:]:
        if letter.isupper(): #checking whether the letter is upper or not
            new_string+=seperators+letter.lower()
        
        else:
            new_string+=letter.lower()
    print(new_string)

kebab_case='-'

snake_case='_'

print('\nThis is kebab case: ')
string_converter('ThisIsCamelCased',kebab_case)

print('\nThis is snake case: ')
string_converter('ThisIsCamelCased',snake_case)