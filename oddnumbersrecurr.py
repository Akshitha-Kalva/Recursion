def odd(n):
    if n>100:
        return
    if n%2!=0:
        print(n,end=" ")
    odd(n+1)
n=int(input())
odd(n)