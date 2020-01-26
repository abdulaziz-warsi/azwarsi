from random import randint

class Node(object):
    def __init__(self,key, priority):
        self.key = key
        self.size = 1
        self.cnt = 1
        self.priority = randint(1,50)
        self.left = None
        self.right = None

    def rotate_left(self):
        x = self
        y = x.right
        x.right = y.left
        y.left = x
        x = y
        y = x.left
        y.size = y.left_s() + y.right_s() + y.cnt
        x.size = x.left_s() + x.right_s() + x.cnt
        return x

    def rotate_right(self):
        x = self
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        y = x.right
        y.size = y.left_s() + y.right_s() + y.cnt
        x.size = x.left_s() + x.right_s() + x.cnt
        return x

    def left_s(self):
        if self.left is None:
            return 0
        else:
            return self.left.size

    def right_s(self):
        if self.right is None:
            return 0
        else:
            return self.right.size

    def __repr__(self):
        return "<node key: %s priority:%f size:%d left:%s right:%s>" % (str(self.key), self.priority,self.size,str(self.left),str(self.right))

class Treap(object):
    def __init__(self):
        self.root = None

    def _insert(self,u,key,priority=None):
        if u is None:
            u = Node(key,priority)
            return u
            u.size = u.size + 1
        if key < u.key:
            u.left = self._insert(u.left,key,priority)
            if u.left.priority < u.priority:
                u = u.rotate_right()
        elif key >= u.key:
            u.right = self._insert(u.right,key,priority)
            if u.right.priority < u.priority:
                u = u.rotate_left()
        return u

    def insert(self,key,priority=None):
        self.root = self._insert(self.root,key,priority)

    def _find(self, u,key):
        if u == None:
            return None
        if u.key == key:
            return u
        if key < u.key:
            return self._find(u.left,key)
        else:
            return self._find(u.right,key)

    def find(self,key):
        return self._find(self.root,key)

    def _delete(self,u,key):
        if u is None:
            return False
        if u.key == key:
            if u.left is None and u.right is None:
                return None
            elif u.left is None:
                return u.right
            elif u.right is None:
                return u.left
            else:
                if u.left.priority < u.right.priority:
                    u.rotate_right()
                    u.right = self._delete(u.left,key)
                else:
                    u = u.rotate_left()
                    u.left = self._delete(u.left,key)
        elif key < u.key:
            u.left = self._delete(u.left,key)
        else:
            u.right = self._delete(u.right,key)
        u.size = u.left_s() + u.right_s() + u.cnt
        return u

    def delete(self,key):
        if self.find(key) is None:
            return "\nNo such node with key: {} exist".format(key)
        self.root = self._delete(self.root,key)
        return "\nNode with key: {} succesfully deleted".format(key)

    def find_kth(self,k):
        if k <= 0 or k > self.size():
            return "\nNo such Node with key: {} exist you want to search".format(k)
        print( "\nTraversing of key you entered\n")
        return self._find_kth(self.root, k)

    def _find_kth(self,u,k):
        if u is None:
            return None
        if k <= u.left_s():
            return self._find_kth(u.left,k)
        if k > u.left_s() + u.cnt:
            return self._find_kth(u.right , k - u.left_s() - u.cnt)
        return u

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size



    def _traverse(self,u):
        if u == None:
            return self._traverse(u.left)
        print(u.key,self._traverse(u.right))

    def traverse(self):
        self._traverse(self.root)

    def __repr__(self):
        return str(self.root)

    def __preorder(self,x):
        if x:
            print(x.key,x.priority)
            self.__preorder(x.left)
            self.__preorder(x.right)

    def preorder(self):
        return self.__preorder(self.root)

    def inorder(self):
        return self.__inorder(self.root)

    def __inorder(self, x):
        if x:
            self.__inorder(x.left)
            print(x.key,x.priority)
            self.__inorder(x.right)

    def postorder(self):
        return self.__postorder(self.root)

    def __postorder(self, x):
        if x:
            self.__postorder(x.left)
            self.__postorder(x.right)
            print(x.key,x.priority)
def Test():
    t = Treap()
    t.insert(3)
    t.insert(1)
    t.insert(0)
    t.insert(5)
    t.insert(4)
    t.insert(9)
    t.insert(7)
    t.insert(6)
    t.insert(8)
    t.insert(2)
    print(t.find_kth(4))

    
    print(t.delete(2))
    print("\n\t\t\tTraversing whole tree")
    print(t.traverse)
    print("\n\t\t\tPREORDER SERACH")
    t.preorder()
    print("\n\t\t\tINORDER SERACH")
    t.inorder()
    print("\n\t\t\tPOSTORDER SERACH")
    t.postorder()
Test()    









            
