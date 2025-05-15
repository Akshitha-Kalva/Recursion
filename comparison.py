li=list(map(int,input().split()))
max=0
count=0
for i in li:
    if i>max:
        max=i
        count+=1
print(count)        
    
    