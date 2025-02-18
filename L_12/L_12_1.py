import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()

      lst = html.split("\n")
      new_lst = []
      for text in lst:
          mytext = text.lstrip()
          new_lst.append(mytext)
      string = ''.join(new_lst)
      new_string = string.replace(">", ">,\n")

      temp_list = []
      inside_tag = False
      for char in new_string:
          if char == "<":
              inside_tag = True
          elif char == ">":
              inside_tag = False
          elif not inside_tag:
              temp_list.append(char)
      all_text = ''.join(temp_list)

      lst = all_text.split(",\n")
      new_lst = []
      for char in lst:
          if char != "":
              new_lst.append(char)
      final_text = '\n'.join(new_lst)

      print(final_text)

      result = codecs.open(result_file,"w", 'utf-8')
      result.write(final_text)
      result.close()

delete_html_tags("draft.html", "cleaned.txt")