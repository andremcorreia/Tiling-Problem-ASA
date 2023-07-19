lastLine = 0
mem = {}

#python superiority
def square(size,l,v):
    nV = []
    for n in range(len(v)):
        nV += [v[n]] 
        if (n >= l and n < l+size):
            nV[n] -= size
    nV = simplify(nV)
    return nV

def simplify(v):
    if len(v) == 1:
        return []
    v[-1] = v[-2]
    for n in range(len(v)-1):
        if n == 0:
            if v[n+1] < v[n]:
                v[n] = v[n+1]
        elif v[n+1] < v[n] and v[n-1] < v[n]:
            v[n] = max(v[n+1],v[n-1])
        
        if v[n] == 1:
            v[n] = 0
    v[-1] = v[-2]
    return v    

def endPoint(vector):
    for l in vector:
        if l > 1:
            return False
    return True

def process(vector,recurso):
    global lastLine
    if not recurso:
        if int(''.join([str(n) for n in vector])) in mem:
            return mem[int(''.join([str(n) for n in vector]))]
    res = 0
    l = 0
    maxVal = 0
    for i in range(len(vector)-1):
        if vector[i] > maxVal:
            maxVal = vector[i]
            l = i
    if recurso == 1:
        lastLine = l
    size = min(len(vector)-l, vector[l])
    valid = False
    while size > 1 and not valid:
        valid = True
        for i in range(l,l + size):
            if vector[i] < vector[l]:
                valid = False
                size -= 1

    while size > recurso:
        newVector = square(size ,l,vector)
        if not endPoint(newVector):
            res += process(newVector,0)
        else:
            res += 1
        size -= 1
    if not recurso:
            mem[int(''.join([str(n) for n in vector]))] = res
    return res

def control(vector):
    total = 0
    while not endPoint(vector):
        total += process(vector,1)
        n = lastLine
        vector[n] -= 1
        if vector[n] == 1:
            vector[n] = 0
        if n == len(vector)-1:
            vector[len(vector)-1] = 0
        vector[-1] = vector[-2]
    print(total+1)

n = int(input())
m = int(input())
v = [int(input()) for i in range(n)]
if v[-1] == 0:
    print(0)
else:
    v = simplify(v)
    v = [i for i in v if i != 0]
    control(v)
