#12. Create a function, is_palindrome, 
# to determine if a supplied word is the same if the letters are reversed.

def is_palindrome(your_text):

    new_text=""

    for letters in your_text[::-1]:
        new_text+=letters
    
    if new_text==your_text:
        print("'{}' is a palindrom".format(new_text))
    else:
        print("'{}' is not a palindrom".format(new_text))

is_palindrome("level")