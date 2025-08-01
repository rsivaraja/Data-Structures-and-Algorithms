class Treenode():
    def __init__(self,v):
        self.value=v
        self.right=None
        self.left=None
def Preorder(root):
    #root left right
    if root is None:
        return
    print(root.value,end=' ')
    Preorder(root.left)
    Preorder(root.right)

def Inorder(root):
    #left root right
    if root is None:
        return
    Inorder(root.left)
    print(root.value, end=' ')
    Inorder(root.right)

def Postorder(root):
    #left right root
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.value,end=' ')
 

def insert(root,value):
    if root is None:
        return Treenode(value)
    if value>root.value:
        root.right=insert(root.right,value)
    if value<root.value:
        root.left=insert(root.left,value)
    return root

def search(root,value):
   # if root is None:
   #     return -1
    if root.value==value:
        return True
    elif root.value<value:
        if root.right is not None:
            return search(root.right,value)
        else:
            return False
    elif root.value>value:
        if root.left is not None:
            return search(root.left,value)
        else:
            return False
    else:
        return False
def Inordersuccessor(root):
    current=root
    while current.left is not None:
        current=current.left
    return current

def delete(root,value):
    if root is None:
        return root
    if value<root.value:
        root.left=delete(root.left,value)
    elif value>root.value:
        root.right=delete(root.right,value)
    else:
        #root has one child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        #root has two children
        else:
            temp=Inordersuccessor(root)
            t=root.data
            root.data=temp.data
            temp.data=t
            root.right=delete(root.right,temp.data)


root=None
root=insert(root,6)
root=insert(root,89)
root=insert(root,1)
root=insert(root,6)
root=insert(root,90)
root=insert(root,5)
root=insert(root,78)
root=insert(root,15)
# data=search(root,63)
# if data==False:
#     print('Value not found')
# else:
#     print('Value found')

delete(root,78)
Inorder(root)    
Preorder(root)