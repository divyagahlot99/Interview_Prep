def solve(n, l):
    o = 0
    e = 0
    for i in range(len(l)):
        if l[i]%2 != 0:
            o += 1
        else:
            e += 1
    o_arr = []
    e_arr = []
    if o == 0:
        i = 3
        while i < len(l):
            print(i, i+1)
            i +=2
        return
    if o%2 == 0:
        count = 0
        for i in range(len(l)):
            if l[i]%2 != 0:
                count += 1
                if count > 2:
                    o_arr.append(i)
            else:
                e_arr.append(i)
        i = 0
        while i < len(o_arr):
            print(o_arr[i] + 1, o_arr[i+1] + 1)
            i += 2
        i = 0
        while i < len(e_arr):
            print(e_arr[i] + 1, e_arr[i+1] + 1)  
            i += 2     
    else:
        c1 = 0
        c2 = 0
        o_arr = []
        e_arr = []
        for i in range(len(l)):
            if l[i]%2 != 0:
                c1+=1
            if l[i]%2 == 0:
                c2+=1
            if (l[i]%2 != 0 and c1 > 1):
                o_arr.append(i)
            if (l[i]%2 == 0 and c2 > 1):
                e_arr.append(i)        
        i = 0
        while i < len(o_arr):
            print(o_arr[i]+1, o_arr[i+1]+1)
            i += 2
        i = 0
        while i < len(e_arr):
            print(e_arr[i]+1, e_arr[i+1]+1)
            i += 2       
 
 
t = int(input())
for we in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    solve(n, l)
