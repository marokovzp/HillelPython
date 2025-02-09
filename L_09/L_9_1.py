def popular_words (text, words):
    text = " " + text.lower() + " "
    amount_lst = []
    my_dict = {}
    for el in words:
        el_new = " " + el + " "
        amount = text.count(el_new)
        amount_lst.append(amount)
        my_dict.update({el: amount})
    return my_dict


# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1' print('OK')

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')