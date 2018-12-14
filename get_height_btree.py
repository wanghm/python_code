class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root==None:
            return 0
        else:
            return max(self.getHeight1(root.left, 0), self.getHeight1(root.right,0))


    def getHeight1(self,root,height):
        if root==None:
            return height;
        else:
            return max(self.getHeight1(root.left, height+1), self.getHeight1(root.right, height+1))


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
