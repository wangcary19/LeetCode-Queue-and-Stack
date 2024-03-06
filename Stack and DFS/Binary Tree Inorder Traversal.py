# March 6th, 2024

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    output = []
    return self.in_dfs(root, output)


def in_dfs(self, root: Optional[TreeNode], master: List[int]) -> List[int]:
    if not root:
        return
    else:
        self.in_dfs(root.left, master)
        master.append(root.val)
        self.in_dfs(root.right, master)
        return master