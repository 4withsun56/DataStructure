class Stack:
    def __init__(self):
        self.top=[]

    def isEmpty(self): return len(self.top)==0
    def size(self): return len(self.top)
    def clear(self): self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top)

map=[['1','1','0','1','1','1','1','1','1','1'],
     ['1','1','0','0','0','0','0','0','0','1'],
     ['1','1','1','1','0','1','1','0','1','1'],
     ['1','1','1','1','0','1','1','0','1','1'],
     ['1','1','1','1','0','1','1','0','1','x'],
     ['1','1','1','0','0','1','1','0','0','0'],
     ['1','1','1','1','0','1','1','0','1','1'],
     ['1','0','1','1','0','1','1','0','0','1'],
     ['e','0','0','0','0','1','1','1','1','1'],
     ['1','0','1','1','1','1','1','1','1','1']]

MAZE_SIZE=10


def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x]=='0'or map[y][x]=='x'


def DFS():
    stack=Stack()
    stack.push((0,8))
    print('DFS:  ')
    move=0
    
    while not stack.isEmpty():
        here=stack.pop()
        print(here,end='->')
        (x,y)=here
        if(map[y][x]=='x'):
            return True,move
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):
                stack.push((x,y-1))
                move+=1
            if isValidPos(x,y+1):
                stack.push((x,y+1))
                move+=1
            if isValidPos(x-1,y):
                stack.push((x-1,y))
                move+=1
            if isValidPos(x+1,y):
                stack.push((x+1,y))
                move+=1
        print(' 현재스택: ',stack)
    return False


result,move=DFS()


if result: 
    print('--> 미로탐색 성공')
    print("이동거리 = ",move)
else: print('-->  미로탐색 실패')

