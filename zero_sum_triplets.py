def zerosumtriplets(l,n):
    t=[]
    for i in range(n-1): 
        s=set() 
        for j in range(i+1,n): 
            if -(l[i]+l[j]) in s: 
                t.append([-(l[i]+l[j]),l[i],l[j]]) 
            else: s.add(l[j])
    return t
    
n=int(input())
l=list(map(int, input().split()))
print(zerosumtriplets(l,n))
