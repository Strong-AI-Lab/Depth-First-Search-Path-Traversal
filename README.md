# Depth First Search Path Traversal
## Target
For the tree structure in the figure below, traverse and output the path from all leaf nodes to the root node.
<img src="tree_structure.PNG" width="600" />

## The process of traversal
    :param start:
            eg: 'c'
    :param child_father_dict:
            eg: {'c': {'d', 'b'}, 'd': {'a'}, 'b': {'a'}}
    :return: all_path:
            eg: [[['c', 'b', 'a'], ['c', 'd', 'a']]]

## Output
`[[['h', 'd', 'a']], [['f', 'c', 'a'], ['f', 'b', 'a']], [['e', 'b', 'a']], [['g', 'c', 'a'], ['g', 'd', 'a']]]`

# Acknowledgement
深度搜索算法（python实现）获取所有叶子节点到根节点的路径

https://www.codeleading.com/article/21464801118/
