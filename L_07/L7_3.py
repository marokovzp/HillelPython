def second_index(text, some_str):
  ind = text.find(some_str, text.find(some_str) + 1)

  if ind >= 0: return (ind)
  else: return


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
