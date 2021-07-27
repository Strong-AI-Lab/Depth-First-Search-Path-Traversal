# -*- coding: utf-8 -*-
import pandas as pd


def get_path(start, child_father_dict):
    """
    Starting from the leaf node, traverse continuously to the root node to get the path from all leaf nodes to the root node.
    :param start:
            eg: 'c'
    :param child_father_dict:
            eg: {'c': {'d', 'b'}, 'd': {'a'}, 'b': {'a'}}
    :return: all_path:
            eg: [[['c', 'b', 'a'], ['c', 'd', 'a']]]
    """

    def _dfs(node, path, res):
        path.append(node)
        if node not in child_father_dict:
            res.append(path.copy())
            path.pop()
            return
        for ni in child_father_dict[node]:
            _dfs(ni, path, res)
        path.pop()

    all_path = []
    if start in child_father_dict:
        _dfs(start, [], all_path)
    return all_path


if __name__ == '__main__':
    df = pd.DataFrame({'father': ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                       'child': ['b', 'c', 'd', 'e', 'f', 'f', 'g', 'g', 'h']})
    father_set = set(df['father'])
    child_set = set(df['child'])
    # The set of leaf node
    leaf_node_set = child_set - father_set
    # The dictionary of child and father node
    chi_fat_dict = df.groupby('child').agg({'father': set}).to_dict()['father']
    # Starting from the leaf node, traverse continuously to the root node to get the path from all leaf nodes to the root node.
    all_paths = [get_path(son, chi_fat_dict) for son in leaf_node_set]
    print(all_paths)