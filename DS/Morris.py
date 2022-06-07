class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Morris中序遍历
# 建立一种机制，对于没有左子树的节点只到达一次，对于有左子树的节点会到达两次
# 后续遍历是在中序遍历的基础上修改而成的

# 对于每个树：
#
# 在第一次遍历到左子树的最右节点 (记为pre)时，将该节点的right指向父节点root (pre->right = root)，
# 然后进入左子树(root = root->left)， 作为一个独立树开始。
#
# 在第二次遍历到该左子树的最右节点时（此时right已经指向了父节点root），说明左子树已经遍历完成，
# 则断开对父节点的连接(pre->right = nullptr)，开始进入右子树开始独立树遍历(root = root->right)。


class Solution(object):

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        res = []

        while root:
            # 左子树存在，找到左子树的最右节点
            # 如果最右节点pre还没有指向root（第一次找到该点），则pre.right = root,下一循环进入左子树
            # 如果最右节点pre.right指向root（第二次找到该点），
            # 则说明左子树已经遍历完成，断开链接，添加root.val, 进入右子树
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                # 此时pre为左子树的最右节点

                if not pre.right:
                    # 第一次到达该节点，pre.right = root
                    pre.right = root
                    root = root.left  # 进入左子树

                if pre.right == root:
                    # 左子树遍历完成，断开链接，添加root.val,进入右子树
                    pre.right = None
                    res.append(root.val)
                    root = root.right  # 进入右子树

            else:
                #  左子树不存在，添加root.val,进入右子树
                res.append(root.val)
                root = root.right
        return res


if __name__ == '__main__':
    tree = [1, None, 2, 3]
    s = Solution()
    print(s.inorderTraversal(tree))
