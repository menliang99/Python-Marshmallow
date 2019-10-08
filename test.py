
def fab(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    else:
        ret = fab(n-1)
        ret.append(ret[-1] + ret[-2])
        return ret

def fab2(n):
    ret = [1]
    if n > 1:
        ret.append(1)
    while n > 2:
        ret.append(ret[-1] + ret[-2])
        n = n - 1
    return ret

seq = [1, 1]
def fabgen():
    yield seq[0]
    yield seq[1]
    while True:
        seq.append(seq[-1] + seq[-2])
        seq.pop(0)
        yield seq[-1]

gen = fabgen()


def similaritycmp(s, t):

    return False if len(s) != len(t)

    dicS = {}
    dicT = {}

    for i in range (len(s)):
        a = dicS.get(s[i])
        b = dicT.get(t[i])
        if not a and not b:
            dicS[s[i]] = t[i]
            dicT[t[i]] = s[i]
        elif a != t[i] or b != s[i]:
            return False

    return True

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbor = []

 def cloneGraph(node):

     dic = {}
     q = [node]

     Newnode = Node(node.val)
     dic[node] = Newnode

     while q:
         tmp = q.pop(0)
         for node in tmp.neighbor:

            if node not in dic:
                q.append(node)
                tmpnode = Node(node.val)
                dic[tmp].neighbor.apped(tmpnode)
                dic[node] = tmpnode
            else:
                dic[tmp].neighbor.append(dic[tmp])
     return dic[node]


def ReverseList(head):

    if head == None or head.next == None:
        return head

    second = head.next
    revsec = ReverseList(second)
    second.next = head
    head.next = None

    return revsec

