def correct_sentence(text):
  lst = text.split()

  if (len(lst)) == 2:
    text_1 = str(lst[0]).title()
    text_2 = lst[1]
    for i, el in enumerate(lst[0]):
      if i == (len(lst[0]) - 1):
        if el == ".":
          text_2 = str(lst[1]).title()
    text = text_1 + " " + text_2
  else:
    text = text.title()

  if text[len(text)-1] != ".":
    text += "."
  return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')