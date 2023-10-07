def linear_search(lst,x):
    flag=0
    for i in range(len(lst)):
        if x==lst[i]:
            flag=1
            return i
    if flag==0:
        return -1
lst=list(map(int,input().split()))
x=int(input())
r=linear_search(lst,x)
if r==-1:
    print("element not found")
else:
    print("found at",r,"index")