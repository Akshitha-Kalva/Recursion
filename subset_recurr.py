def fun(arr,k,i=0,res=[]):
    if i==len(arr):
        if sum(res)==k:
            print(res)
        return
    fun(arr,k,i+1,res+[arr[i]])
    fun(arr,k,i+1,res)
l=[1,2,3,6]
k=5
fun(l,k)                       