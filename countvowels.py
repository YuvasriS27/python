string="Yuvasri"
vowels=('a','e','i','o','u')
count=0
for s in string:
    for v in vowels:
        if(s==v):
            count=count+1
print(count)
    
