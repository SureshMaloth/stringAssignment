#comparing strings
word_1=input("enter The word1:")
word_2=input("enter the word2:")
if word_1>word_2:
    print(word_1)
elif word_2>word_1:
    print(word_2)


#print the greater total value with ascii
name_1=input("enter the name1:")
name_2=input("enter the name2:")
split_name_1=list(name_1)
total_name_1=0
for i in split_name_1:
    num=ord(i)
    total_name_1+=num
split_name_2=list(name_2)
total_name_2=0
for i in split_name_2:
    num=ord(i)
    total_name_2+=num
if total_name_1>total_name_2:
    print(name_1)
else:
    print(name_2)


#comparing Numbers
num_1=int(input("enter the num1:"))
num_2=int(input("enter the num2:"))
if num_1==num_2:
    print("is Same")
elif num_1>num_2:
    print(num_1)
elif num_2>num_1:
    print(num)