# to given the string first occurance of the substring value find() 
# if the value not availble returns -1
word="python is a high level programming launguage"
sub_string="h"
find_substring=word.find(sub_string)
print(find_substring)


#with input()
char=input("enter the char:")
subString=input("enter the subString:")
result=char.find(subString)
print(result)

value=input("enter the value:")
subString=input("enter the subString:")
start=int(input("enter the nbr:"))
end=int(input("enter the nbr:"))
result =value.find(subString,start,end)
print(result)