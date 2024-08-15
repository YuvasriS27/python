name="Yuvasri is a good girl"
word=name.split()
string=word
count=0
for s in word:
    for n in string:
        if(s==n):
            count=count+1
print("The count of words in given string is:",count)
