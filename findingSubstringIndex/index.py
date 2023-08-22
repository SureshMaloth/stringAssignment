# to given the string first occurance of the substring value find() 
# if the value not availble returns value error
word="python is a high level programming launguage"
sub_string="h"
find_substring=word.index(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.index(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.index(subString,start,end)
print(result)