

def say_hi(name, age):
  my_str_1 = "Hi. My name is "
  my_str_2 = name
  my_str_3 = " and I'm "
  my_str_4 = str(age)
  my_str_5 = " years old"
  return my_str_1 + my_str_2 + my_str_3 + my_str_4 + my_str_5

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')

print(say_hi("Slava", 40))