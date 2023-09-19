class BinaryTree:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def preorder(self):
        print(self.data,end='')
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
    def midorder(self):
        if self.left != None:
            self.left.midorder()
        print(self.data,end='')
        if self.right != None:
            self.right.midorder()
    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        print(self.data,end='')
    def height(self):
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1+self.right.height()
        elif self.right is not None and self.right is None:
            return 1+self.left.height()
        else:
            return 1+max(self.left.height(),self.right.height())

layer3_2 = BinaryTree(2,BinaryTree(7),BinaryTree(4))
layer2_5 = BinaryTree(5,BinaryTree(6),layer3_2)
layer2_1 = BinaryTree(1,BinaryTree(0),BinaryTree(8))
layer1_3 = BinaryTree(3,layer2_5,layer2_1)

layer1_3.preorder()
print()
layer1_3.midorder()
print()
layer1_3.postorder()
print()
print(layer1_3.height())




