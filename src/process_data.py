from arvoreB.btree import BTree

def process_file(input_file, output_file, t):
    b_tree = BTree(t)

    with open(input_file, 'r') as f:
        for line in f:
            key = int(line.strip())
            b_tree.insert(key)
            
    with open(output_file, 'w') as f:
        _write_traverse(b_tree.root, f)

def _write_traverse(node, f):
    i = 0
    for i in range(len(node.keys)):
        if not node.leaf:
            _write_traverse(node.children[i], f)
        f.write(str(node.keys[i]) + "\n")
    if not node.leaf:
        _write_traverse(node.children[i + 1], f)