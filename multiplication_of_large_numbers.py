def convert_to_list(x):
    y=[]
    for i in x:
        y.append(int(i))
    return y

def final_addition(l):
    carry=0
    f=0
    i=0
    total_len=0
    m=[0]*len(l)
    while i<len(l):
        f=1
        l[i]+=carry
        curr=l[i] % 10
        carry=l[i]//10
        m[i]=curr
        i+=1
        total_len+=1
    while(carry>0):
        total_len+=1
        m[i]=carry%10
    m=m[::-1]
    m=''.join([str(e) for e in m]) 
    return m,total_len

def curr_list(a, digit):
    l=[]
    carry=0
    for i in a:
        curr=digit*i + carry
        l.append(curr%10)
        carry=curr//10
    while carry>0:
        l.append(carry%10)
        carry//=10
    return l

def solve(a,b): 
    dp=[0]*100
    a=(convert_to_list(a))[::-1]
    b=(convert_to_list(b))[::-1]
    pos=0
    for i in b:
        curr = curr_list(a,i)
        j=0
        while j<len(curr):
            dp[j+pos]+=curr[j]
            j+=1
        pos+=1
        total_len=pos+len(curr)
    total_len,f=final_addition(dp[0:total_len])[::-1]
    print(f)

a=input()
b=input()
solve(a,b)
