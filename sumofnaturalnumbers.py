# def sum(n):
#     if n==1:
#         return 1
#     return n+sum(n-1)
# n=int(input())
# print(sum(n))
#parameterised recursion
def fun(n,sum):
    if n<1:
        print(sum)
        return
    fun(n-1,sum+n)
n=5
fun(n,sum=0)