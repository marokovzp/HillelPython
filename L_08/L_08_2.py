import string

def is_palindrome(text):
    new_text = text
    for el in text:
        for i, el_punc in enumerate(string.punctuation):
            if el == el_punc or el == " ":
                new_text = new_text.replace(el, "").lower()
    new_text_revert = new_text[::-1]

    return new_text == new_text_revert

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")