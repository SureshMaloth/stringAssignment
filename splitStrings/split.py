word="o cheliya naa priya sakiya"
result=word.split()
print(result)

second_result=word.split("a")
print(second_result)

word_2="ma@lo@th@Su@re@sh"
split_word=word_2.split("@")
print(split_word)

text="hello,i am suresh,25 years old,"
split_text=text.split(",")
print(split_text)

#max separation 
txt="sureshMalothHowareYou"
txt_sep=txt.split("o",2)
print(txt_sep)
