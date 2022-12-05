
def str_list(word1, word2):
   str1 = ""
   str2 = ""
   for x in word1:
      str1 = str1 + x
   for y in word2:
      str2 = str2 + y
   return (str1 == str2)


word1 = str(input())
word2 = str(input())

print(str_list(word1,word2))

