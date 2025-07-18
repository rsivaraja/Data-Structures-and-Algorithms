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
root=Treenode(6)
root.left=Treenode(3)
root.right=Treenode(10)
root.left.left=Treenode(13)
root.right.right=Treenode(15)
root.right.left=Treenode(14)
root.left.right=Treenode(18)
#Preorder(root)
#Inorder(root)
Postorder(root)