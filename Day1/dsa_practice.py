#Reversing the string
text= "python"
reversed=""
for i in text:
    reversed=i+reversed
print(reversed)


#Largest number

num=[10,25,40,93,88,20]
larg=num[0]
for n in num:
    if n>larg:
        larg=n
print(larg)