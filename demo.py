def swap(string, i, j):
    lst=list(string)
    lst[i],lst[j]=lst[j],lst[i]
    return ''.join(lst)
def permute(string,left,right):
    if left==right:
        print(string)
    else:
        for i in range(left,right+1):
            string=swap(string,left,i)
            permute(string,left+1,right)
            string=swap(string,left,i)
s="ABC"
n=len(s)
permute(s,0,n-1)