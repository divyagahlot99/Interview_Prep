class Node:
    def __init__(self, data=None):
        self.data=data
        self.lc=None
        self.rc=None
        self.lp=None
        self.rp=None

def solve(curr, nodes):
    moves=[]
    while curr.lp or curr.rp:
        if curr.lp:
            moves.append("lc")
            curr=curr.lp
        else:
            moves.append("rc")
            curr=curr.rp
    # print(moves)
    return moves[::-1], curr

def mirror(moves, curr):
    for i in range(len(moves)):
        cont=0
        if moves[i]=="lc" and curr.lc:
            curr=curr.lc
            cont=1
        if moves[i]=="rc" and curr.rc:
            curr=curr.rc
            cont=1
        if cont==0:
            return -1
    return curr

def main():
    n,q=map(int, input().split())
    nodes=[Node(1)]
    nodes[0].data='1'
    query=[]
    for i in range(1,n):
        p,c,r=input().split()
        nodes.append(Node(c))
        for j in nodes:
            if j.data==p:
                if r=='R':
                    j.rc=nodes[i]
                    nodes[i].lp=j
                else:
                    j.lc=nodes[i]
                    nodes[i].rp=j
    for i in range(q):
        query.append(input())
    for w in range(q):
        moves=[]
        node=None
        for r in nodes:
            if r.data==query[w]:
                moves,node=solve(r, nodes)
                m = mirror(moves,node)
                if m==-1:
                    print(m)
                else: 
                    print(m.data)

if __name__=='__main__':
    main()
