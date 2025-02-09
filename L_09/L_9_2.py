def popular_words(text, words):
    text = text.lower().split()  # Convert to lowercase and split into words
    print( {word: text.count(word) for word in words})
    return {word: text.count(word) for word in words}  # Count occurrences

# Test case
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',    ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')