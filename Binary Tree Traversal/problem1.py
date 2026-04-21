class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order traversal
def pre_order(node):
    result = []

    def dfs(node):
        if node is None:
            return
        result.append(node.data)
        left_order = dfs(node.left)
        right_order = dfs(node.right)

    dfs(node)
    return result


# In-order traversal
def in_order(node):
    result = []

    def dfs(node):
        if not node:
            return
        left_order = dfs(node.left)
        result.append(node.data)
        right_order = dfs(node.right)

    dfs(node)
    return result


# Post-order traversal
def post_order(node):
    result = []

    def dfs(node):
        if not node:
            return
        left_order = dfs(node.left)
        right_order = dfs(node.right)
        result.append(node.data)

    dfs(node)
    return result

