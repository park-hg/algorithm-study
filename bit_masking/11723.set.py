import sys
sys.stdin = open('input.txt', 'r')

m = int(sys.stdin.readline())
S = 0

def add(x):
    global S
    if not S & (1 << x-1):
        S += (1 << x-1)

def remove(x):
    global S
    if S & (1 << x-1):
        S -= (1 << x-1)

def check(x):
    global S
    if S & (1 << x-1):
        return 1
    else:
        return 0

def toggle(x):
    global S
    if S & (1 << x-1):
        S -= (1 << x-1)
    else:
        S += (1 << x-1)

def all():
    return (1 << 20) - 1

def empty():
    return 0

for _ in range(m):  
    func = sys.stdin.readline().split()
    if func[0] == 'add':
        add(int(func[1]))
    elif func[0] == 'remove':
        remove(int(func[1]))
    elif func[0] == 'check':
        print(check(int(func[1])))
    elif func[0] == 'toggle':
        toggle(int(func[1]))
    elif func[0] == 'all':
        S = all()
    elif func[0] == 'empty':
        S = empty()