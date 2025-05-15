def freq(l,t,i=0):
    if i==len(l):
        return 0
    if l[i]==t:
        return 1+freq(l,t,i+1)
    return freq(l,t,i+1)
l=[1,1,1,1,2,2,2,3]
t=2
print(freq(l,t))