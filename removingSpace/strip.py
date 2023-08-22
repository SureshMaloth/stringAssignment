word ="  thi is strip method "
value=word.strip()
print(value)

#particular  left side deletion
word ="  thi is strip method "
value=word.lstrip()
length=len(value)
print(value)
print(length)
print(len(word))

#particular  right side deletion
word ="   thi is strip method    "   
value=word.rstrip()
length=len(value)
print(value)
print(length)
print(len(word))
      


# particular char removes

word="@#! python is a programming language *^"
result=(word.strip("@#!*^ "))
print(result)
print(len(word))
print(len(result))