#1

a=[2,10,15,45,90]
count=0
for i in a:
    if(i>0):
        count=count+1
print("The Total no in array",count,"all are positive")


#2

print(" ")
a=[-2,10,15,-45,90]
count=0
count1=0
for i in a:
    if(i>0):
        count=count+1
    if(i<0):
        count1=count1+1
print("The Total no in array",count," are positive","\nThe total no in array",count1,"are negative")

