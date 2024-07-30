from .node import BTreeNode

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def insert(self, k):
        if len(self.root.keys) == (2 * self.t) - 1:
            s = BTreeNode(self.t, False)
            s.children.append(self.root)
            self._split_child(s, 0)
            self.root = s
        self._insert_non_full(self.root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t]
