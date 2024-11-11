class CircularQueue:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.array=[None]*capacity
        self.front=0
        self.rear=0

    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1)%self.capacity
    def enqueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%self.capacity
            self.array[self.rear]=item
        else:
            pass
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.capacity
            delete=self.array[self.front]
            self.array[self.front]=None
            return delete
        else: 
            pass
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
    
def myLineEditor():
    q=CircularQueue(10)
    while True:
        command=input("[메뉴선택] e-입력, d-삭제, q-종료=> ")
        if command=='e':
            num=int(input("입력: "))
            q.enqueue(num)
            print(q.array)
        elif command=='d':
            q.dequeue()
            print(q.array)
        elif command=='q':
            return

myLineEditor()
