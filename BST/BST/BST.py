class BSTNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
    def isLeaf(self):
        return self.left is None and self.right is None
def search_bst(n,key):
    if n==None:
        return None
    elif key==n.key:
        return n
    elif key<n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)
def search_value_bst(n, value) :
    if n == None :
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None :
       return res
    return search_value_bst(n.right, value)
def search_min_bst(n):
    while n!=None and n.left!=None:
        n=n.left
    return n
def search_max_bst(n):
    while n!=None and n.right !=None:
        n=n.right
    return n
def insert_bst(root,node):
    if root==None:
        return node
    if node.key==root.key:
        return root
    if node.key<root.key:
        root.left=insert_bst(root.left,node)
    else:
        root.right=insert_bst(root.right,node)
    return root
def delete_bst(root,key):
    if root==None:
        return root
    if key<root.key:
        root.left=delete_bst(root.left,key)
    elif key>root.key:
        root.right=delete_bst(root.right,key)
    else:
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left
        succ=search_min_bst(root.right)
        root.key=succ.key
        root.value=succ.value
        root.right=delete_bst(root.right,succ.key)
    return root

class BSTMap():
    def __init__(self):
        self.root=None
    def isEmpty(self):
        return self.root==None
    def findMax(self):
        return search_max_bst(self.root)
    def findMin(self):
        return search_min_bst(self.root)
    def search(self,key):
        return search_bst(self.root,key)
    def searchValue(self,value):
        return search_value_bst(self.root,value)
    def insert(self,key,value=None):
        n=BSTNode(key,value)
        self.root=insert_bst(self.root,n)
    def delete(self,key):
        self.root=delete_bst(self.root,key)
    def display(self,msg='BSTMap :',order=''):
        
        if(order=='1'):
            print(msg,end='')
            inorder(self.root)
            print()
        if(order=='2'):
            print(msg,end='')
            preorder(self.root)
            print()
        if(order=='3'):
            print(msg,end='')
            postorder(self.root)
            print()
def preorder(n) :
    if n is not None :
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=' ')
        


data=[35,18,7,26,12,3,68,22,30,99]
value=["삼오","일팔","영칠","이육","일이","영삼","육팔","이이","삼영","구구"]

map=BSTMap()
map.display("[삽입 전] : ")
for i in range(len(data)):
    map.insert(data[i],value[i])
    map.display("[삽입 %2d]: "%data[i],'1')

print('[최대 키]:',map.findMax().key)
print('[최소 키]:',map.findMin().key)
print('[탐색 26]:','성공' if map.search(26)!=None else '실패')
print('[탐색 25]:','성공' if map.search(25)!=None else '실패')
print('[탐색 일팔]:','성공' if map.searchValue("일팔")!=None else '실패')
print('[탐색 일칠]:','성공' if map.searchValue("일칠")!=None else '실패')

map.delete(3)
map.display("[삭제 3]:",'1') #중위순회
map.delete(3)
map.display("[삭제 30]:",'2')#전위순회
map.delete(3)
map.display("[삭제 68]:",'3')#후위순회