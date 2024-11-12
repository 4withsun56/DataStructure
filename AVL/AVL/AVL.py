from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)
  
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_avl(parent, key):
    if parent is None:
        return parent
    
    if key < parent.key:
        parent.left = delete_avl(parent.left, key)
    elif key > parent.key:
        parent.right = delete_avl(parent.right, key)
    else:

        if parent.left is None:
            temp = parent.right
            parent = None
            return temp
        elif parent.right is None:
            temp = parent.left
            parent = None
            return temp

        temp = find_min(parent.right)
        parent.key = temp.key
        parent.right = delete_avl(parent.right, temp.key)

    if parent is None:
        return parent

    return reBalance(parent)

from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)



if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]

    root = None
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = insert_avl(root, n)

        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()
    min_node = find_min(root)
    print("\n최솟값 제거: ", min_node.key)
    root = delete_avl(root, min_node.key)

    print("최솟값 제거 후 AVL 트리: ")
    levelorder(root)
    print()
    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))


