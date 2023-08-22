word="Iam Indian"
replace_word="Hindhu"
result=word.replace("Indian",replace_word)
print(result)


word_2="hii hii all of how are you hi what are"
replace_word_2="hello"
final_word=word_2.replace("hii",replace_word_2,2)
print(final_word)


word_3=input("enter the value:")
orginal_word=input("enter the changeWord:")
replace_word_3=input("enter the replaceword:")
occurance_value=int(input("enter the nbr"))
final_word=word_3.replace(orginal_word,replace_word,occurance_value)
print(final_word)